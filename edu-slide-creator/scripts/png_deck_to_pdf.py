#!/usr/bin/env python3
"""Combine ordered PNG slide images into a widescreen PDF deck."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def natural_key(path: Path) -> list[object]:
    parts = re.split(r"(\d+)", path.name)
    key: list[object] = []
    for part in parts:
        if part.isdigit():
            key.append(int(part))
        else:
            key.append(part)
    return key


def collect_images(args: argparse.Namespace) -> list[Path]:
    images = [Path(p) for p in args.images]

    if args.input_dir:
        input_dir = Path(args.input_dir)
        matches = list(input_dir.glob(args.pattern))
        if args.natural_sort:
            matches.sort(key=natural_key)
        else:
            matches.sort()
        images.extend(matches)

    if not images:
        raise SystemExit("No PNG images were provided.")

    missing = [str(p) for p in images if not p.exists()]
    if missing:
        raise SystemExit("Missing input image(s):\n" + "\n".join(missing))

    non_png = [str(p) for p in images if p.suffix.lower() != ".png"]
    if non_png:
        raise SystemExit("Only PNG inputs are supported:\n" + "\n".join(non_png))

    return images


def draw_full_page(pdf: canvas.Canvas, image_path: Path, page_w: float, page_h: float) -> None:
    with Image.open(image_path) as image:
        if image.mode in ("RGBA", "LA") or (
            image.mode == "P" and "transparency" in image.info
        ):
            background = Image.new("RGB", image.size, "white")
            background.paste(image.convert("RGBA"), mask=image.convert("RGBA").getchannel("A"))
            rgb = background
        else:
            rgb = image.convert("RGB")

        pdf.drawImage(
            ImageReader(rgb),
            0,
            0,
            width=page_w,
            height=page_h,
            preserveAspectRatio=False,
            mask="auto",
        )


def build_pdf(
    images: list[Path],
    out_path: Path,
    title: str,
    author: str,
    page_w: float,
    page_h: float,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(out_path), pagesize=(page_w, page_h), pageCompression=1)
    pdf.setTitle(title)
    pdf.setAuthor(author)

    for image_path in images:
        draw_full_page(pdf, image_path, page_w, page_h)
        pdf.showPage()

    pdf.save()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Combine PNG slide images into a 16:9 PDF deck."
    )
    parser.add_argument("images", nargs="*", help="Explicit PNG image paths in page order.")
    parser.add_argument("--input-dir", help="Directory to scan for PNG slide images.")
    parser.add_argument(
        "--pattern",
        default="*.png",
        help="Glob pattern used with --input-dir. Default: *.png",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output PDF path.",
    )
    parser.add_argument(
        "--title",
        default="Educational Slide Deck",
        help="PDF title metadata.",
    )
    parser.add_argument(
        "--author",
        default="Codex",
        help="PDF author metadata.",
    )
    parser.add_argument(
        "--page-width",
        type=float,
        default=960,
        help="PDF page width in points. Default: 960.",
    )
    parser.add_argument(
        "--page-height",
        type=float,
        default=540,
        help="PDF page height in points. Default: 540.",
    )
    parser.add_argument(
        "--expected-pages",
        type=int,
        help="Fail unless the collected image count matches this value.",
    )
    parser.add_argument(
        "--no-natural-sort",
        action="store_false",
        dest="natural_sort",
        help="Use plain lexicographic sort for --input-dir matches.",
    )
    parser.set_defaults(natural_sort=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    images = collect_images(args)

    if args.expected_pages is not None and len(images) != args.expected_pages:
        raise SystemExit(
            f"Expected {args.expected_pages} page(s), but collected {len(images)} image(s)."
        )

    out_path = Path(args.out)
    build_pdf(
        images=images,
        out_path=out_path,
        title=args.title,
        author=args.author,
        page_w=args.page_width,
        page_h=args.page_height,
    )

    print(f"Created PDF: {out_path}")
    print(f"Pages: {len(images)}")
    print("Image order:")
    for index, image_path in enumerate(images, start=1):
        print(f"{index:02d}: {image_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
