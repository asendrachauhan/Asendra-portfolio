# Asendra Chauhan — Portfolio (Futuristic Cyber Edition)

Single-file static site (`index.html` + `assets/`). Zero build step, zero dependencies, deployable directly anywhere.

## Key Features & Architecture
1. **Resume-Aligned Identity & Profile** — Fully updated with Asendra Chauhan's exact credentials: Full-Stack Developer (MEAN/MERN & GenAI Applications), 2+ years experience building production SaaS end-to-end (Angular 17+, React, TypeScript, Node.js, Express.js, NestJS, MongoDB, Groq/Llama), based in Mohali, Punjab, India (Phone: `+91 6375318789`), education at Sri Balaji College of Engineering & Technology (RTU, GPA 8.6/10), and complete work history across Rudra Innovative Software and Sumedha Softtech.
2. **Dual-System 3D Holographic Architecture Viewport** — Interactive multi-system command center:
   - **System 01 (`SYS://FULLSTACK-AI.v26`)**: 3D isometric view of the full-stack core (Angular/React frontend, Node/NestJS backend, Neural Groq AI core, MongoDB/Redis data tier, and CI/CD pipelines).
   - **System 02 (`SYS://AUTOAPPLY-ENGINE.v10`)**: 3D isometric pipeline of the solo-engineered AutoApply AI SaaS platform (Laser resume parser, Groq LPU 94% match analysis, dynamic resume tailoring, and multi-board job dispatch).
   - **Interactive SVG Dynamic Conduits**: Glowing animated energy conduits connecting architecture layers with traveling pulse beams.
   - **Web Audio Sci-Fi Synthesizer (SFX)**: Procedural Web Audio API sound synthesizer with futuristic audio blips and chords for pin inspections and system toggles, complete with an SFX toggle button.
   - **3D Card Parallax Tilt & Specular Sheen**: Real-time cursor-tracking perspective tilt with a dynamic radial specular sheen simulating obsidian glass reflection.
   - **Real-Time Diagnostic Gauges & Terminal Log**: Live P95 latency, throughput, uptime (99.99%), cache hit ratio, and an automated event stream ticker.
3. **AutoApply AI Solo-Engineered Flagship SaaS Showcase** — Comprehensive case study for AutoApply AI with 6-stage architectural pipeline, 9 screenshot gallery cards, and high-definition diagram lightboxes.
4. **KiteSuite Enterprise Workspace Showcase** — Production workspace multi-module architecture with interactive screenshot modal.
5. **Interactive Career Dossier & ATS Resume Panel** — Role-filterable interactive dossier with ATS plaintext switcher, copy-to-clipboard, and print-ready PDF export.
6. **100% 6-Language Localization (666 Translation Keys)** — Comprehensive translations across English, हिन्दी (Hindi), Español (Spanish), Français (French), Deutsch (German), and 日本語 (Japanese) without page reload.
7. **Free & Unlimited Email Delivery System (No 50/Month Quota Limits)**:
   - **Pre-configured with FormSubmit.co**: 100% free and unlimited submissions directly to `asendrachauhan176@gmail.com`.
   - **Zero Formspree Limits**: Replaced Formspree (which had a strict 50 submissions/month limit) with an unlimited endpoint.
   - **Asynchronous AJAX Submission**: Smooth user feedback with inline loading spinner, emerald success state, form reset, and graceful fallback to `mailto:` if network fails.
   - **Smart Visitor Telemetry Throttling**: Visitor notifications are throttled to at most once per session (`sessionStorage`), and completely suppressed during local development (`localhost`), keeping your inbox clean.
   - **Optional 100% Self-Hosted Google Apps Script Backend**: Included `google-apps-script-mailer.js` for free direct Gmail API delivery (up to 500 emails/day) with zero third parties.

---

## Activating FormSubmit.co (1-Minute, 1-Click Setup)

FormSubmit is active by default. Here is how it works:
1. Submit the contact form once from your live site (or send a test message).
2. Check your inbox at `asendrachauhan176@gmail.com` for an email from FormSubmit with the subject:
   **"Action Required: Please Confirm Your Email"**.
3. Click the **"Activate Form"** button inside the email.
4. **Done!** From that moment forward, every message submitted on your portfolio will instantly land in your Gmail inbox, completely free with no monthly submission limits.

---

## Deploy options (pick one)

### GitHub Pages (matches the canonical URL already in the meta tags)
1. Push this folder's contents to your repo (`Asendra-portfolio`).
2. Repo Settings → Pages → Deploy from branch → `main` / root.
3. Live at `https://<username>.github.io/<repo>/`.

### Netlify / Vercel (drag-and-drop)
1. Go to Netlify "Deploys" (or vercel.com/new), drag this whole folder in.
2. Done — no build command needed, it's static HTML.

### Any static host (S3, Cloudflare Pages, Firebase Hosting, your own server)
Just upload `index.html` and `assets/` as-is, preserving the folder structure.

---

## Custom Email Configuration (Optional)

Near the top of `index.html` (lines 70-76), you will find:
```html
<script>
  window.ASENDRA_CONTACT_EMAIL = "asendrachauhan176@gmail.com";
  window.ASENDRA_CUSTOM_ENDPOINT = ""; // Paste your Google Apps Script URL here if preferred
  window.ASENDRA_VISITOR_NOTIFY = true; // Set to false to disable visitor alerts
</script>
```

- If you want to use the free **Google Apps Script** endpoint instead of FormSubmit:
  1. Follow the step-by-step instructions in [`google-apps-script-mailer.js`](google-apps-script-mailer.js).
  2. Paste your Google Apps Script Web App URL into `window.ASENDRA_CUSTOM_ENDPOINT`.
