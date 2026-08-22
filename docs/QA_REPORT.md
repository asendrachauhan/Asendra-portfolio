# Production QA — Asendra Portfolio

## Scope
Final single-page static portfolio build for GitHub Pages / Netlify.

## Verified
- JavaScript syntax passes `node --check`.
- All 163 `data-i18n` keys are present in all six language dictionaries: English, Hindi, Spanish, French, German, Japanese.
- Theme state is global and persisted with `localStorage`.
- Language state is persisted with `localStorage`.
- Dynamic KiteSuite gallery is translated and uses local screenshots.
- Gallery images open in an accessible lightbox and close via button, backdrop, or Escape.
- Responsive navigation has keyboard-visible focus states.
- Active desktop navigation follows the visible section.
- Reduced-motion preference disables decorative animation.
- Resume and portfolio assets referenced by the HTML exist.
- Favicon, manifest, 404 page, robots.txt and sitemap are present.
- Sitemap points to the actual GitHub Pages portfolio path.
- Security headers are configured in `netlify.toml`.
- No invented KiteSuite business metrics were added. Resume/project metrics are explicitly labeled historical claims.

## Evidence boundary
Portfolio facts are derived from the supplied resume/project material. KiteSuite is described as contribution work, not ownership. No confidential product internals are exposed beyond the screenshots and high-level system surfaces supplied for the portfolio.

## Design principles applied
- One coherent design system across the entire page.
- Light/dark theme changes the complete UI rather than individual sections independently.
- Strong editorial typography and grid rhythm.
- Motion is used to reinforce hierarchy and interaction, not as decoration alone.
- Mobile-first responsive behavior.
- Case-study storytelling over a generic project-card wall.
- Proof is separated from claims and labeled by source context.
- Technical names remain recognizable as technology/product names; descriptive interface copy is localized.
