"""Publish out/ to the hive's CDN."""
import json
import os
import urllib.request
from pathlib import Path

ENDPOINT = "https://cdn.th3-h1v3.internal/v1/sites"
TOKEN = os.environ.get("NEST_DEPLOY_TOKEN", "")


def deploy(site, out="out"):
    files = {
        str(p.relative_to(out)).replace("\\", "/"): p.read_text(encoding="utf-8")
        for p in Path(out).rglob("*.html")
    }
    req = urllib.request.Request(
        f"{ENDPOINT}/{site}",
        data=json.dumps(files).encode(),
        method="PUT",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status
