# 실사 스타일 — graphite cover + engineering plate

Preset name: **실사** (realistic / photorealistic engineering poster). Trigger this profile when a user asks for 실사, 실사 스타일, realistic style, or photorealistic slides.

Source: two user-supplied slides for the NCM/graphite anode-potential monitoring deck. This profile describes their visual language; the example slide's technical claims and wording are not reusable content.

## Design system

- **Two-mode deck:** cinematic dark cover, then warm off-white technical pages. The cover uses a charcoal/graphite texture, dramatic battery-cell cutaway, cream headline, and amber highlights. Body pages use a lightly textured ivory field, near-black text, fine warm-gray borders, and sparse accent colors.
- **Palette:** charcoal/graphite, ivory, amber/copper, muted teal/green for safe or nominal states, and red only for risk, threshold, or derating. Keep colors semantic and restrained.
- **Typography:** oversized bold condensed sans-serif title at the top left; compact Korean/English technical labels in clean sans-serif; equations in a high-contrast mathematical serif or monospaced treatment. Retain common engineering abbreviations such as I, V, T, SOC, ECM, and BMS where useful.
- **Body-slide hierarchy:** small page number at top right; large numbered title; a full-width, thin-bordered objective/takeaway band with a copper left rail; dense but aligned body grid; a narrow source or note footer at bottom left.
- **Diagram language:** combine one large physical cutaway or circuit with a left-to-right signal chain. Use bordered cards, circular instrument/processor/gauge icons, thin connector arrows, and short labels. Keep reading order clear: physical system → measured values → estimator → risk margin → control output.
- **Technical callouts:** place a dark graphite-texture equation strip near the bottom for the governing equation and calibration constants. Use small red markers only for risk margins and critical thresholds. Use green gauge arcs for acceptable operation.
- **Information density:** engineering-poster density is acceptable, but each page should have one primary conclusion, one dominant equation or model, and a few supporting panels. Keep labels brief and avoid paragraphs inside diagrams.
- **Visuals:** use realistic, detailed cell materials for the hero cutaway; use crisp schematic linework for circuits, state chains, gauges, and plots. Distinguish conceptual artwork from measured data; label illustrative curves or values.

## Cover profile

- Dark charcoal graphite surface with a high-detail NCM/graphite cell cutaway on the left.
- Large cream title on the right, with one smaller explanatory line.
- A four- or five-step circular signal chain below the title, joined by arrows; amber describes the fast-charge mode and red marks plating risk.
- A slim source/version footer. Do not reuse the example's exact wording or claims.

## Technical-page profile

- Warm ivory background; title and page number at the top; bold takeaway band directly below.
- Use a two-column or 55/45 grid. Let the physical cell/circuit and safety gauges occupy the left; estimator/signal-chain cards and metadata occupy the right.
- When a page has one important model, make its formula legible in a charcoal strip at the bottom. Keep formulas and units exact; do not invent numeric limits.
- Reuse accent colors by meaning: green = within margin, amber = operating input or caution, red = threshold/risk, teal = estimated state.

## Image-generation prompt guidance

Use both supplied reference slides as style references when available: image 1 for the dark cover and image 2 for the light technical-page grid. Ask the image model to preserve exact title, takeaway, equation, units, and symbols verbatim; avoid copying the reference slide's content. Prefer a single clear engineering diagram, short labels, and no invented thresholds. Review every generated slide for formula fidelity and legibility before PDF assembly.
