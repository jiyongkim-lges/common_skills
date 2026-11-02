# LG Style Reference

Use these rules whenever the user requests `LG스타일`, `LG 스타일`, or `LG style`.

## Required assets

- Body template: `assets/lg-style/template-slide.png`
- Completed reference: `assets/lg-style/template-slide-reference.png`
- Icon library: `assets/lg-style/icons/aliases/`

Resolve these paths relative to the `edu-slide-creator` skill directory.

## Fixed layout

- Canvas: 16:9, 1672 × 941 px
- Background: pure white
- Palette: black, white, and cyan/teal only
- Title band: approximately 100 px high from the top edge to the cyan rule
- Title: handwritten Korean style at the reference size; reduce padding rather than font size
- Title accents: short cyan vertical bar at upper left and a thin cyan horizontal rule
- Head message: nearly full-width white box with a thin black outline and subtle corner radius
- Head-message icon: one black line icon selected by meaning from the bundled aliases
- Head-message text: one bold sentence; never add the literal label `HEAD MESSAGE`
- Body: keep content between the message box and bottom baseline; avoid the page-number and decoration zones
- Page number: two digits inside the outlined circle at bottom left
- Bottom-right decoration: retain the small approved cyan/teal group at about two-thirds of the original source size, anchored 25–30 px from the right and bottom edges

## Content rules

1. Replace the title, head message, icon, and page number first.
2. Choose the icon by the slide's meaning, not decoratively.
3. Prefer diagrams, equations, charts, and concise labels over dense paragraphs.
4. Preserve the template geometry and whitespace unless the user explicitly asks to change it.
5. Keep all Korean text legible and verify the final PNG is 16:9.
6. Use image generation only for final slide artwork; deterministic tools are allowed only for assembly and verification.
