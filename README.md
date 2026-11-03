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
- `assets/`: existing demonstrations and portraits, plus the static ANCL logo extracted from the animation's final frame. The original animation is retained.

Both pages use relative links and local images, so they can be served directly through GitHub Pages. Inter is loaded from Google Fonts with system-font fallbacks.
