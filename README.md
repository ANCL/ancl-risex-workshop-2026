# ANCL RISEx Workshop 2026

Static website for the PX4 + ROS 2 Drone Control workshop at the University of Alberta.

## Review this refresh

Compare the existing live site with the proposed changes in [PR #8](https://github.com/ANCL/ancl-risex-workshop-2026/pull/8):

| Page | Original live site | PR branch preview |
| --- | --- | --- |
| Home | [Original Home](https://ancl.github.io/ancl-risex-workshop-2026/) | [Preview Home](https://raw.githack.com/ANCL/ancl-risex-workshop-2026/codex/website-content-refresh/index.html) |
| About | [Original About](https://ancl.github.io/ancl-risex-workshop-2026/about.html) | [Preview About](https://raw.githack.com/ANCL/ancl-risex-workshop-2026/codex/website-content-refresh/about.html) |

The preview is served by the third-party raw.githack service from the public PR branch. On your first visit, select **Open the page** on its source-confirmation screen. Branch updates normally appear within minutes, though caching may take longer. These are review links, not GitHub Pages deployments; the original live site is unaffected. The preview requires the branch to remain available.

## Local preview

Run from the repository root:

```sh
python -m http.server 8000
```

Open `http://localhost:8000/` in your browser. There is no build step or package installation.

## Files

- `index.html`: event details, demonstrations, organisers, and contact information.
- `about.html`: programme, learning outcomes, and reference links.
- `style.css`: shared styling and responsive layouts.
- `assets/`: optimized WebP portraits, the original looping GIF demonstrations, and the static ANCL logo. Original portrait files are retained as source assets.

Both pages use relative links and local images, so they can be served directly through GitHub Pages. Inter is loaded from Google Fonts with system-font fallbacks.

On phones, the header is compact, navigation stays visible, and the content uses a single column. Biographies retain their complete original wording and are left-aligned on small screens. Demonstrations retain the original continuously looping GIFs. No JavaScript is needed.
