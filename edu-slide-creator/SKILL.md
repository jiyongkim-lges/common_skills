---
name: edu-slide-creator
description: Use when creating, assembling, or verifying educational slide decks from image-generated PNGs, or when applying a requested cute / cuty / 큐티, “실사 스타일” / photorealistic engineering-poster, or “LG스타일” / “LG style” visual preset.
---

# Edu Slide Creator

## Overview

Use this skill when a user has a set of educational slide PNGs and wants a single PDF deck. The default workflow preserves the existing PNG visuals, orders the deck explicitly, creates a 16:9 PDF, and verifies the result by rendering representative PDF pages back to PNG.

When the user asks for a similar educational slide style, inspect the bundled example PNGs under `assets/examples/` before creating or arranging new slides.

## Cute Style Selection

When the request includes “cute”, “cuty”, “큐티”, or “귀여운 스타일”, use the saved visual reference `assets/cute-style/infographic-reference.png` and apply this educational style. This named preset takes priority over the general examples under `assets/examples/`.

- Use friendly toy-like 2D/3D characters, with a small battery or cell mascot when the subject is batteries.
- Give the main title a bold dimensional treatment. Place concise content in soft pastel-gradient cards with colorful dimensional number or bullet markers.
- Add small UI-like buttons and cartoon accents such as arrows, sparkles, heat waves, or magnifying-glass details when they support the subject.
- Group the lesson into a few numbered stages and show their relationship with a clear visual flow. Keep labels legible, contrast strong, and decorative elements clear of technical content.
- Keep equations, circuit symbols, plots, units, and technical labels accurate and crisp. Use the reference for visual direction only; preserve the current lesson’s content and do not copy the reference’s wording or claims.
- Carry the same palette, dimensional title, card treatment, and character cues across cover, contents, and technical slides, adapting the composition to each slide’s purpose.

Use image generation for final PNGs, supplying this reference image when the image tool supports references.

## LG Style Selection

When the request contains `LG스타일`, `LG 스타일`, or `LG style`, use the bundled LG-style resources instead of the default examples:

- Use `assets/lg-style/template-slide.png` as the body-slide template.
- Use `assets/lg-style/template-slide-reference.png` to match content density and hierarchy.
- Read `references/lg-style.md` before creating or editing any LG-style slide.
- Select semantically appropriate line icons from `assets/lg-style/icons/aliases/`.
- Preserve icon proportions and line style. Do not redraw or distort the icons.
- Use image generation for the final PNG and provide the template, reference slide, and selected icons as visual references when the image tool supports them.
- Apply the LG visual system to cover and table-of-contents slides as well, while adapting their composition to their function.

The explicit LG-style request overrides the general examples under `assets/examples/`.

## Realistic Engineering Poster Style (실사)

When the user asks for “실사”, “실사 스타일”, “realistic style”, or “photorealistic” slides, use the saved realistic engineering-poster preset:

- Read `references/anode-potential-poster-style.md` and use the supplied style-reference assets.
- For a cover, use `assets/reference-style/cover-reference.png` as the main reference: dark graphite, cinematic lighting, and a photorealistic cell cutaway.
- For technical pages, use `assets/reference-style/technical-reference.png` as the main layout reference: warm ivory engineering poster, copper takeaway rail, aligned panels, and a graphite equation strip.
- Render physical battery materials and hero objects realistically. Keep equations, circuits, plots, gauges, and signal-chain diagrams crisp and schematic so technical relationships remain readable.
- Preserve the task’s claims, formulas, units, and page order; take only visual direction from the references.

The “실사” preset is distinct from the bundled LG-style preset. If the user explicitly requests both, combine realistic physical imagery with the requested LG layout and icon rules where they fit.

## User-provided slide style references

When the user provides slide images and asks to extract or reuse their visual style, read `references/anode-potential-poster-style.md` as a reusable profile when relevant. Use the user's actual images as generation references when available. Apply the profile as visual direction only: do not reuse example slide wording, technical claims, or numeric thresholds as source facts. Preserve the current task's content, formulas, units, and ordering.

## Slide PNG Creation Rule

When creating new slide PNGs, **do not directly render slides yourself**. 절대로 직접 렌더링하지 말고, 이미지생성으로 만들어줘.

- Use image generation for the final slide PNGs.
- Do not create final slide PNGs with HTML/SVG/CSS/browser screenshots, Python drawing, canvas, presentation export, Mermaid export, or other deterministic direct-rendering pipelines.
- Do not use code-native layouts as final slide artwork. Use them only as private planning notes if needed.
- Keep deterministic tools for PDF assembly and PDF verification only, after the image-generated PNGs already exist.

## Workflow

1. **Confirm the page order**
   - Prefer explicit order when the deck has a cover or table of contents.
   - For numbered decks, use lexicographic/natural order only after checking it puts pages in the intended sequence.
   - Typical order: cover `00`, table of contents `00_목차`, then `01` through the last numbered slide.

2. **Create or collect image-generated slide PNGs**
   - If the PNGs do not already exist, generate each slide with image generation.
   - Save every final generated slide PNG into the project/workspace folder before PDF assembly.
   - Use the bundled examples as visual references for composition, density, white background, technical linework, and bottom-left references.

3. **Create the PDF**
   - Prefer `scripts/png_deck_to_pdf.py` for deterministic conversion.
   - Use 16:9 page size by default: `960 x 540 pt`.
   - Preserve every PNG as a full-page image. Do not crop, add margins, or add page numbers unless the user asks.

4. **Verify the PDF metadata**
   - Run `pdfinfo <output.pdf>`.
   - Check `Pages`, `Page size`, encryption status, and file size.
   - The expected page count must equal the number of PNG inputs.

5. **Verify visual PDF output**
   - Render at least the first page, the table-of-contents page when present, and the last page:
     ```bash
     pdftoppm -png -r 144 -f 1 -l 2 deck.pdf /tmp/deck-front
     pdftoppm -png -r 144 -f <last> -l <last> deck.pdf /tmp/deck-last
     ```
   - Inspect the rendered PNGs visually when image viewing is available.
   - Look for clipping, wrong aspect ratio, black pages, unreadable text, and unexpected page order.

6. **Report the result**
   - Give the final PDF path.
   - Summarize page count and ordering.
   - Mention which pages were visually checked.

## Script Usage

Use the bundled script from the skill directory:

```bash
python <skill-dir>/scripts/png_deck_to_pdf.py \
  --input-dir posters/extended-ecm-slides \
  --pattern 'Extended_ECM_회로도와_수식_설명_*.png' \
  --out posters/extended-ecm-slides/Extended_ECM_회로도와_수식_설명.pdf \
  --title 'Extended ECM 회로도와 수식 설명' \
  --expected-pages 18
```

For stricter control, pass image paths explicitly:

```bash
python <skill-dir>/scripts/png_deck_to_pdf.py \
  --out deck.pdf \
  cover.png toc.png slide-01.png slide-02.png
```

## Example References

Use these bundled examples as visual references when creating or reviewing slide images:

- `assets/examples/cover-example.png`: title slide pattern with centered title, small bottom-left references, white background, restrained technical characters, and light schematic elements.
- `assets/examples/toc-example.png`: table-of-contents pattern with a top title, one head-message box, four grouped sections, full slide list, and small bottom visual strip.
- `assets/examples/technical-slide-example-02.png`: technical body-slide pattern for circuit diagrams, equations, labeled terms, black linework, white background, and sparse accent colors.

Keep these examples as references, not mandatory templates. Match their ordering, visual density, white background, readable typography, and verification discipline unless the user requests a different style.

## Good Defaults

- Output filename: reuse the deck title stem, e.g. `{title}.pdf`.
- Page size: `960 x 540 pt` for widescreen slides.
- Author metadata: `Codex`, unless the user specifies another author.
- Temporary render checks: use `<temp-dir>/<deck>-pdf-check` for the current operating system.
- Final PDF location: keep it beside the slide PNGs unless the user names another destination.

## Failure Handling

- If dependencies are missing, call the bundled workspace dependencies first when available. Use `reportlab`, `Pillow`, `pdfinfo`, and `pdftoppm`.
- If a command fails because it needs browser, GUI, network, or filesystem permissions, request the smallest necessary escalation and retry.
- If page count or visual checks fail, do not deliver the PDF as complete. Fix the input order, regeneration, or conversion issue first, then re-run verification.
