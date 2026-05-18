# Project notes

Static HTML/CSS portfolio site for Amber Hamersfeld. Plain HTML + CSS only, no build step (one small Python script for the slideshow).

## Contact

- Email: amber@hamersfeld.com
- Formspree endpoint: https://formspree.io/f/maqkyjlz (used by the contact form on contact.html)
- Instagram handle: not yet provided. Placeholder `your_instagram_handle` is in contact.html and the nav `Instagram` link in every page is still `href="#"`. Update both once known.

## Structure

- `index.html` — home with CSS slideshow + project grid
- `about.html` — about page (editable text block inside `<div class="about-page__content">` with `white-space: pre-wrap`)
- `contact.html` — Formspree contact form + Instagram DM link
- Per-project pages: `alchemy.html`, `bloomed.html`, `brumbys.html`, `mrs_matcha.html`, `bloom_cosmetics.html`, `blitz_bar.html`, `still_life.html`
- `styles.css` — shared styles
- `fonts/` — local Caslon + Sackers Gothic
- `hero/` — per-project tile thumbnails (4:3 currently)
- `slideshow/` — homepage hero slideshow images (managed by update-slideshow.py)
- Per-project image folders: `alchemy/`, `bloomed/`, `brumbys/`, `mrs_matcha/`, `bloom_cosmetics/`, `blitz_bar/`, `still_life/`

## Slideshow

`./update-slideshow.py` scans the `slideshow/` folder and rewrites the slideshow markup in index.html between the `<!-- SLIDESHOW:START -->` / `<!-- SLIDESHOW:END -->` markers. Recalculates animation timing for any number of images. Run after dropping new images in the folder.

## Type system

- Sackers Gothic Std Heavy (caps-only) — primary body, nav, labels, tile metas, eyebrows, footer
- Caslon Graphique D — only on big display titles: hero tagline, project H1, next-project title, about title, contact title

## Deploy

GitHub repo via `gh`. Vercel auto-deploys on push if connected. Git workflow:

```
git add . && git commit -m "..." && git push
```

## Folders that ship with the site but aren't linked

These were source/staging folders. Still present in the repo, untouched:
- `portfolio /` (trailing space) — original source mockups + project brief PDFs
- `VERTICAL IMAGES FOR EACH SHOWCASE /` — vertical mockup sources
- `hero images landing page /` — hero image sources
- `campaign-image-finds/` — rendered portfolio PDF pages with project text
- `project.html` — original detail template, unused
- `AGENTS.md`, `untitled folder/` — leftover

Ask before deleting any of these.
