#!/usr/bin/env python3
"""
Scans the slideshow/ folder and rewrites the slideshow block in index.html
between the <!-- SLIDESHOW:START --> and <!-- SLIDESHOW:END --> markers.

Run this after adding or removing images:
    ./update-slideshow.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SLIDESHOW_DIR = ROOT / "slideshow"
INDEX_FILE = ROOT / "index.html"

PER_SLIDE = 5
FADE = 1
EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def collect_images() -> list[Path]:
    if not SLIDESHOW_DIR.is_dir():
        sys.exit(f"Slideshow folder not found: {SLIDESHOW_DIR}")
    files = [
        p for p in SLIDESHOW_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in EXTS and not p.name.startswith(".")
    ]
    files.sort(key=lambda p: p.name.lower())
    return files


def build_block(images: list[Path]) -> str:
    count = len(images)
    total = count * PER_SLIDE
    fade_pct = FADE / total * 100
    visible_end_pct = (PER_SLIDE - FADE) / total * 100
    slide_end_pct = PER_SLIDE / total * 100

    slides = "\n".join(
        f'    <div class="slideshow__slide" style="animation-delay: {i * PER_SLIDE}s">'
        f'<img src="slideshow/{img.name}" alt=""></div>'
        for i, img in enumerate(images)
    )

    return (
        "<!-- SLIDESHOW:START -->\n"
        "    <style>\n"
        f"      .slideshow__slide {{ animation-duration: {total}s; }}\n"
        "      @keyframes slideshow-fade {\n"
        "        0% { opacity: 0; }\n"
        f"        {fade_pct:.3f}% {{ opacity: 1; }}\n"
        f"        {visible_end_pct:.3f}% {{ opacity: 1; }}\n"
        f"        {slide_end_pct:.3f}% {{ opacity: 0; }}\n"
        "        100% { opacity: 0; }\n"
        "      }\n"
        "    </style>\n"
        f"{slides}\n"
        "    <!-- SLIDESHOW:END -->"
    )


def main() -> None:
    images = collect_images()
    if not images:
        sys.exit(f"No images found in {SLIDESHOW_DIR}")

    block = build_block(images)
    html = INDEX_FILE.read_text()
    pattern = re.compile(r"<!-- SLIDESHOW:START -->.*?<!-- SLIDESHOW:END -->", re.DOTALL)
    if not pattern.search(html):
        sys.exit("Slideshow markers not found in index.html")

    html = pattern.sub(lambda _: block, html)
    INDEX_FILE.write_text(html)
    print(f"Updated slideshow with {len(images)} image(s):")
    for img in images:
        print(f"  - {img.name}")


if __name__ == "__main__":
    main()
