# Workshop Website Refresh Implementation Plan

> Execute in this session using the approved previews. Review the completed change before pushing.

**Goal:** Transfer the approved visual design to the original static site and push a new branch.

**Architecture:** Keep `index.html`, `about.html`, and one shared `style.css`. Use the existing local media and add one static logo frame. No build tools or runtime dependencies.

**Tech stack:** HTML and CSS.

**Spec:** `docs/superpowers/specs/2026-11-03-website-refresh-design.md`

## Constraints and review focus

Preserve biographies verbatim, use relative links and local assets, retain 1,280px page caps and matching titles, and keep narrow screens free of horizontal overflow. Check missing assets, keyboard navigation, heading structure, accidental localhost links, and unintended content loss. This is a static presentation change: use structural checks and browser verification without adding a test framework.

## Tasks

- [x] Transfer the approved HTML to the two existing pages, remove mockup-only scripts, add document metadata and main-content navigation, and consolidate the styles into `style.css`.
- [x] Add the static ANCL image, use local media URLs, preserve full biographies, and document local preview usage in `README.md`.
- [x] Verify preserved copy, local links/assets, 1,280px desktop layout, consistent titles, 360px layout, and navigation between pages. Review the complete diff.

## Verification record

- All three biographies match the original revision verbatim.
- Both HTML documents have balanced elements, one main landmark and one h1; local assets, page links, and fragment targets resolve.
- The static logo pixels match the final animation frame.
- Desktop inspection confirms 1,280px page widths, 48px titles on both pages, loaded local images, and full-column justified biographies.
- At a 360px viewport neither page overflows horizontally; About body text remains 18px and biographies become left-aligned.
- Navigation works between pages, with a visible current-page indicator; browser error logs are empty.
- About durations are 40, 20, and 30 minutes. No preview-only URLs or runtime remain.
- Independent code review found no critical or important issues. Its two minor CSS findings were corrected and verified in the browser.

Delivery: commit the site and design record, push `codex/website-content-refresh` to `origin`, and verify the remote branch matches the local commit. No merge or deployment is requested.
