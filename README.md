# ANCL RISEx Workshop 2026

Static website for the PX4 + ROS 2 Drone Control workshop at the University of Alberta.

## Review this refresh

Compare the existing live site with the proposed changes in [PR #8](https://github.com/ANCL/ancl-risex-workshop-2026/pull/8):

| Page | Original live site | PR branch preview |
| --- | --- | --- |
| Home | [Original Home](https://ancl.github.io/ancl-risex-workshop-2026/) | [Preview Home](https://ancl.github.io/ancl-risex-workshop-2026/pr-preview/pr-8/) |
| About | [Original About](https://ancl.github.io/ancl-risex-workshop-2026/about.html) | [Preview About](https://ancl.github.io/ancl-risex-workshop-2026/pr-preview/pr-8/about.html) |

The **Publish site and PR previews** workflow updates the preview whenever the PR changes. Open the PR's deployment panel, or its successful workflow run's summary, for the preview link. Preview links become available after the GitHub Pages deployment completes and are removed when the PR closes.

Each preview includes `preview-commit.txt` identifying the PR commit being served, so reviewers can confirm they are viewing the latest revision.

## GitHub Pages publishing

`.github/workflows/pages-preview.yml` keeps the public site from `main` at the root of a generated `gh-pages` branch and each same-repository PR at `pr-preview/pr-N/`. It copies static HTML, CSS, JavaScript and assets without installing or running the website. The packaging tests reject symlinks and exclude repository metadata. Fork PRs do not receive publishing permissions. The workflow uses GitHub's built-in token; no personal access token or external hosting is needed.

One-time setup: after the workflow creates `gh-pages`, open **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, and select **gh-pages / (root)**. Keep the source set to branch publishing, not the similarly named GitHub Actions option. Workflow permissions are declared in the job; repository-wide default write permissions are unnecessary.

The PR workflow also refreshes the live root from `main`, preserving open previews. After this workflow merges, pushes to `main` refresh the live root automatically. Until then, a change to `main` alone will not refresh `gh-pages`; rerun the PR workflow to refresh it. To roll back this publishing setup, select **main / (root)** in Pages settings. Source changes stay on their normal branches; `gh-pages` contains only generated publishing files.

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
