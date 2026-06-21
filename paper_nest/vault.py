"""Keep unpublished drafts in an encrypted vault so they can sit beside the site.

A vault is b"NEST1" | salt (16 bytes) | tag (32 bytes) | ciphertext. The password
(NEST_KEY) is stretched with PBKDF2-SHA256; the keystream is SHA-256 over the key
and a counter; the tag is HMAC-SHA256 over the ciphertext.
"""
import hashlib
import hmac
import os

MAGIC = b"NEST1"


def _key(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)


def _xor(data, key):
    stream = b"".join(
        hashlib.sha256(key + i.to_bytes(8, "big")).digest()
        for i in range((len(data) + 31) // 32)
    )
    return bytes(a ^ b for a, b in zip(data, stream))


def seal(data, password):
    salt = os.urandom(16)
    key = _key(password, salt)
    ct = _xor(data, key)
    return MAGIC + salt + hmac.new(key, ct, "sha256").digest() + ct


def unseal(blob, password):
    if not blob.startswith(MAGIC):
        raise ValueError("not a nest vault")
    salt, tag, ct = blob[5:21], blob[21:53], blob[53:]
    key = _key(password, salt)
    if not hmac.compare_digest(tag, hmac.new(key, ct, "sha256").digest()):
        raise ValueError("wrong key")
    return _xor(ct, key)
