# ANCL RISEx Workshop 2026

Static website for the PX4 + ROS 2 Drone Control workshop at the University of Alberta.

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
