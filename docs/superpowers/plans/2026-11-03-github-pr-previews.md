# GitHub PR Previews Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement and verify this plan.

**Goal:** Publish PR #8 through GitHub Pages and show its URL in GitHub's deployment panel; keep all source changes in the current PR.

**Architecture:** A GitHub Actions workflow copies static files from `main` into the root of `gh-pages` and maintains each same-repository PR under `pr-preview/pr-N/`. The existing live root stays sourced from `main`. GitHub Pages publishes the deployment branch; no change is merged into `main` during setup.

**Tech Stack:** GitHub Actions, GitHub Pages, pinned checkout/deploy/PR-preview actions, Python standard library.

**Spec:** User-approved GitHub workflow preview with all updates in PR #8.

## Constraints and review focus

- Preserve the live site until the PR is merged; preserve other previews during root deployment.
- No website code execution or dependency installation; package only static site files, rejecting symlinks. The workflow and packager are trusted code supplied by same-repository collaborators.
- Do not run publishing jobs for fork PRs; use `pull_request`, never `pull_request_target`.
- Remove a PR preview when its PR closes; serialize writes and do not force-push.
- Show a GitHub environment URL and workflow summary; do not post unsolicited PR comments.

## Steps

- [ ] Add and test a static-site packager, including exclusion of repository metadata and symlink rejection.
- [ ] Add the workflow for PR open/reopen/update/close, main pushes, and manual root refresh; preserve `pr-preview/` when updating the live root.
- [ ] Replace external preview documentation with native Pages links and setup/rollback instructions.
- [ ] Review workflow permissions, event conditions, cleanup, and deployment isolation; run local checks.
- [ ] Push to the current branch. Wait for `gh-pages` to contain the unchanged live site and PR preview before switching Pages source from `main` to `gh-pages`.
- [ ] Verify Actions completion, both public pages, original site preservation, and the PR deployment link.
