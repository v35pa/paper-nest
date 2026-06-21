# paper-nest

Paper-thin static sites. Markdown in, HTML out, nothing else.

    python -m paper_nest build src out

## Watching

    python -m paper_nest watch src out

Rebuilds whenever anything under `src/` changes.

## Drafts

Drafts that aren't ready to leave the nest stay sealed in `.nest/` (git ignores it):

    NEST_KEY=... python -m paper_nest vault seal draft.md > .nest/drafts.vault
    NEST_KEY=... python -m paper_nest vault open .nest/drafts.vault
