# Asendra Chauhan — Portfolio

Single-file static site (`index.html` + `assets/`). No build step, no dependencies to install.

## What was fixed in this build
1. **JS crash on every load** — `hideLoader()` referenced a removed `#loader` element, throwing a ReferenceError. Removed the dead code.
2. **System-flow diagram broken on all screen sizes** — a leftover CSS override forced the hero diagram into a mismatched CSS Grid layout, pushing the "Product UI," "Data layer," and "Realtime" nodes completely off-screen on mobile. Restored the correct flex-based layout — verified on both desktop and mobile, all 8 nodes visible with connector lines intact.
3. **Light theme was broken** — the default `:root` color tokens had been overwritten with dark values, so toggling the theme button did nothing visible. Restored the correct cream/light palette. The site still **defaults to dark** (matching the design), and the toggle now genuinely switches themes, with the choice persisted via localStorage.
4. **Stat counters (2.2+, 9+, 20+) crashed on scroll** — the scroll-triggered counter animation observed the wrong element, throwing an error the first time it scrolled into view on any screen size. Fixed to animate all three counters correctly.
5. **"Systems I Build" section didn't match the design at all** — the design shows a compact 3-column row (3D isometric layered stack graphic → Technical Skills icon rows → "Practical AI, Not AI Theatre" cards). The code instead had three unrelated, much larger sections (a plain 10-card text list, a 9-card skills grid, a 3-card GenAI writeup). Rebuilt this as a real 3-column section matching the design pixel-for-pixel: a CSS 3D layered stack (6 animated slabs — Product Surface / API Layer / Data Layer / Integrations / AI Layer / Production) with a matching side list, a compact Technical Skills card grouped exactly like the design (Frontend / Backend & APIs / Data & Storage / DevOps & Tools / AI-GenAI), and a 4-item Practical AI card list. The previous detailed content (full 10-layer breakdown, 9-category skill chips, GenAI production-concerns list) is kept directly below as an expanded deep-dive, so nothing was lost — just reordered so the top-level view matches your design first.
6. **13 new icon assets generated** (`assets/icons/*.svg`, `assets/tech-mini/sass.svg`, `assets/tech-mini/vector.svg`, `assets/tech-mini/prompt.svg`, `assets/tech-mini/automation.svg`, `assets/tech/aws-icon.svg`, `assets/tech/docker-icon.svg`) to fill gaps the design needed but the codebase didn't have — the 6 system-layer icons, 4 "Practical AI" icons, a proper Sass logo, and small-format AWS/Docker icons (the originals were oversized placeholder badges with rendered text, illegible at icon size).
7. **New section wasn't translated** — after rebuilding the 3-column row above, switching the site to Hindi/Spanish/French/German/Japanese left that entire section in English while everything else translated correctly. Added full translations for all new copy (column headers, 6 layer names + descriptions, 5 skill-row labels, 4 Practical-AI titles + descriptions) across all 6 supported languages, wired through the site's existing i18n system. Verified in all 6 languages with no errors.
8. **Hero "System Flow" diagram didn't match the design** — rebuilt it to match the reference precisely: correct node layout (Users → Product UI → Integrations/AI Layer → API Layer → Data Layer/Realtime → Deployment), 8 custom icons matching the design's per-node accent colors, and real directional connector arrows with arrowheads — including curved double-headed arrows and pulsing "data flow" dashed lines — computed dynamically in JS from actual node positions so they stay correctly aligned at every screen size and on window resize.
9. **"Systems I Build" graphic didn't match the design** — replaced the earlier rounded-rectangle slab stack with actual glowing isometric diamond platforms (matching the reference's stacked-diamond visual), each with a centered icon, per-layer glow color, and a subtle 3D sway animation on the whole stack.
10. **Icons rendering solid black instead of colored** — both new diagrams initially used `<img src="icon.svg">` for per-node coloring via CSS, but browsers can't apply CSS `color` to an `<img>`-referenced SVG's `currentColor` fills (it's treated as an opaque embedded resource). Fixed by inlining all 14 icon instances as literal `<svg>` markup so per-instance coloring actually works. Confirmed fixed in both diagrams, both themes.

Verified: zero console/JS errors, no horizontal overflow on mobile (390px) or desktop (1440px) in English/Hindi/Japanese, arrows redraw correctly on window resize, all images load, theme toggle + persistence works in both dark and light mode, all asset references resolve.

## Deploy options (pick one)

### GitHub Pages (matches the canonical URL already in the meta tags)
1. Push this folder's contents to a repo (e.g. `Asendra-portfolio`).
2. Repo Settings → Pages → Deploy from branch → `main` / root.
3. Live at `https://<username>.github.io/<repo>/`.

### Netlify / Vercel (drag-and-drop)
1. Go to Netlify "Deploys" (or vercel.com/new), drag this whole folder in.
2. Done — no build command needed, it's static HTML.

### Any static host (S3, Cloudflare Pages, Firebase Hosting, your own server)
Just upload `index.html` and `assets/` as-is, preserving the folder structure.

## Notes
- Fonts (Inter, DM Mono) load from Google Fonts via CDN — needs internet access to render exactly as designed. This is standard practice and works automatically once deployed publicly.
- Update the canonical URL, `og:url`, and `og:image` meta tags near the top of `index.html` if you deploy to a different domain than `asendrachauhan.github.io/Asendra-portfolio`.
- Contact form currently opens the visitor's email client (mailto) rather than submitting to a backend — check the `contact.sending` / form-submit JS near the bottom of the file if you want to wire it to a real form service (Formspree, Netlify Forms, etc.).
