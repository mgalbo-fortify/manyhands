# Many Hands site (static, Netlify-ready)

Plain HTML, CSS and inline SVG. No build step, no framework.

- index.html: the whole page. Motion is CSS only (keyframes plus scroll-driven reveals) and turns off for visitors who ask for reduced motion.
- thanks.html: where the contact form lands after submit.
- netlify.toml: publish settings.

## Deploy
1. Drag this folder onto app.netlify.com/drop, or connect a GitHub repo holding it.
2. In the site dashboard go to Forms and select Enable form detection, then deploy the folder again (detection only takes effect on the next deploy).
3. Add an email alert under Forms > Submission notifications > Add notification. The recipient must be a member of your Netlify team.
4. Add the custom domain under Domain management.

## Edit
Open the folder in Claude Code and describe the change. Keep the house rules: no em dashes, sentence case headings.
