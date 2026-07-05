# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The official website and download host for **MochiKey**, a Windows shortcut-manager app. This repo contains only the site and the distributable — **not** the app's source code:

- `index.html` — the entire site: a single self-contained landing page (all CSS is inline in a `<style>` block, no JS, no build step, no frameworks). Theme colors are defined as CSS variables in `:root`.
- `server.py` — a minimal Flask server that serves the repo root as static files and adds security headers (nosniff, X-Frame-Options, HSTS) to every response.
- `MochiKey.exe` — the ~42 MB product binary, committed directly and served via the page's download link. Its source lives elsewhere; never attempt to edit or regenerate it.
- `shortcuts.json` — an empty `{}` placeholder config for the app.
- `logo_new.png` — the logo referenced by the page (`logo.png` and `favicon.png` are older/smaller assets).

## Running the site

```bash
pip install flask   # only dependency; there is no requirements.txt
python server.py    # serves on http://localhost:8080
```

There are no tests, linters, or build commands.

## Conventions

- All user-facing site text is Korean (`<html lang="ko">`); keep new copy in Korean to match.
- The production domain is `http://mochikey.com` (referenced in the canonical link, meta description, and footer).
- Keep `index.html` self-contained: edit styles inside its `<style>` block rather than adding external CSS/JS files.
- Because `MochiKey.exe` is unsigned, the page includes a user guide for bypassing browser/SmartScreen/antivirus warnings — preserve this section when restructuring the page.
