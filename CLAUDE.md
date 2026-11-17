# Many Hands site

Static marketing site for Many Hands (practical AI for small businesses in NY, NJ and CT). Hosted on Netlify, which deploys from the `main` branch.

## How it's built
- Plain HTML, CSS and inline SVG. No framework, no build step. `index.html` is the whole page; `thanks.html` is the form landing page.
- Motion is CSS only: keyframes for the illustrations and scroll-driven reveals (`animation-timeline: view()`), with a `prefers-reduced-motion` block that turns everything off. Keep it that way unless a change truly needs JavaScript.
- The contact form uses Netlify Forms (`data-netlify="true"`, form name `contact`, honeypot `company_url`). Don't rename fields without updating Netlify notifications.

## Style rules
- No em dashes anywhere. Sentence case headings. Plain, peer-to-peer tone, no hype.
- Palette: background #FAF7F2, ink #1E2A24, green #2C5A47, deep green #22463A, sand #EFE4D2, sage #D5E2D1, sky #D3E2EA, peach #F3D9C8, butter #F3D18A, mustard #E3B04B.
- Type: Fraunces (headings, weight 500) and DM Sans (body).
- Illustrations: thin line art (1.7px stroke, #26332D) over soft flat color shapes offset a few pixels. Calm, not cartoonish.

## Before you push
Check the page at 1440px and 390px wide, and confirm the form still has `name="contact"` and `data-netlify="true"`.
