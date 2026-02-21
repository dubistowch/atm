# AE2 Guide offline mirror + zh-TW (繁體中文／台灣) pipeline (Node only)

Mirrors <https://guide.appliedenergistics.org/1.21.1/> into:

- `atm/docs/external/ae2-guide/1.21.1/`

Constraints respected:
- no `wget`
- no `pip`
- Node.js only (uses built-in `fetch`)

## Quick start (prototype: index + 1 page)

From repo root (`atm/`):

```bash
node tools/ae2-guide-mirror/mirror-ae2-guide.mjs --limit 2
```

This will:
- crawl routes from `__NEXT_DATA__` navigation tree
- download 2 pages (the index plus 1 additional route)
- download required `/_next/static/...` assets referenced by those pages
- rewrite absolute links to relative
- translate **only** the `<article>` content to **繁體中文（台灣）** via a conservative HTML-aware text-node mapper

## Full mirror (all routes)

```bash
node tools/ae2-guide-mirror/mirror-ae2-guide.mjs
```

## Notes / knobs

- Output root: `atm/docs/external/ae2-guide/1.21.1/`
- Base URL: `https://guide.appliedenergistics.org`
- Base path: `/1.21.1/`

### Translation

This repo intentionally avoids external dependencies and external translation APIs.

The included translator is:
- **safe-by-default**: preserves tags, keeps `<code>/<pre>` unchanged, avoids translating `namespace:id`-style IDs
- **minimal**: uses a small built-in glossary + passthrough for unknown text (so output remains readable and correct, but not fully translated)

To plug in a real translator later, edit `translateText()` in `mirror-ae2-guide.mjs`.

### Resourcepack glossary (optional)

If you want to expand the glossary from existing zh-TW packs, the script has a stub for scanning:

- `~/All The Mon/尋星之夢_繁體漢化_unzipped/minecraft/resourcepacks/*.zip`

…but parsing ZIPs without deps is non-trivial. The stub currently **skips** zip reading.

## Output structure

The mirror writes directories mirroring the site:

- `/1.21.1/` → `.../1.21.1/index.html`
- `/1.21.1/foo/bar/` → `.../1.21.1/foo/bar/index.html`

Assets:
- `/_next/static/...` → `.../1.21.1/_next/static/...`

