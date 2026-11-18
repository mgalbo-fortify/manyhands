# Many Hands site

Static marketing site for Many Hands (practical AI for small businesses in NY, NJ and CT). Hosted on Netlify, which deploys from the `main` branch.

## How it's built
- Plain HTML, CSS, inline SVG and one small script. No framework.
- `index.html` is generated: edit `tools/build.py`, then run `python3 tools/build.py` from the repo root. Don't hand-edit `index.html`.
- `story.js` runs the motion. Two rules: drawn things jump (illustrations move in steps, lines "boil" through three SVG filters), UI glides (cards and text ease). Scroll drives the story: the Maria section and How it works are pinned and read their scroll progress (0 to 1), so scrolling up reverses everything.
- Visitors with `prefers-reduced-motion` get the static page: no pinning, Maria's final scene, all text visible. Keep that path working.
- `thanks.html` is the form landing page.
- The contact form uses Netlify Forms (`data-netlify="true"`, form name `contact`, honeypot `company_url`). Don't rename fields without updating Netlify notifications.

## Style rules
- No em dashes anywhere. Sentence case headings. Plain, peer-to-peer tone, no hype.
- Palette: background #FAF7F2, ink #1E2A24, green #2C5A47, deep green #22463A, sand #EFE4D2, sage #D5E2D1, sky #D3E2EA, peach #F3D9C8, butter #F3D18A, mustard #E3B04B.
- Type: Fraunces (headings, weight 500) and DM Sans (body).
- Illustrations: hand-drawn line art (#26332D, 2 to 2.4px outlines, 1.4 to 1.8px details) roughened with the `rough` filter, over soft flat color shapes offset a few pixels. People have faces and hands. Calm and warm, not cartoonish.
- The story character is Maria, who runs a small window and door shop. Helping hands lift her paperwork away. Keep her consistent if you add scenes.

## Before you push
Rebuild, then check the page at 1440px and 390px wide, scroll through the Maria story both directions, and confirm the form still has `name="contact"` and `data-netlify="true"`.
