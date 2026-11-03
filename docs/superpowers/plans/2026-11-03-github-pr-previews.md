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

- [x] Add and test a static-site packager, including exclusion of repository metadata and symlink rejection.
- [x] Add the workflow for PR open/reopen/update/close, main pushes, and manual root refresh; preserve `pr-preview/` when updating the live root.
- [x] Replace external preview documentation with native Pages links and setup/rollback instructions.
- [x] Review workflow permissions, event conditions, cleanup, and deployment isolation; run local checks.
- [x] Push to the current branch. Wait for `gh-pages` to contain the unchanged live site and PR preview before switching Pages source from `main` to `gh-pages`.
- [x] Verify Actions completion, both public pages, original site preservation, and the PR deployment link.

## Verification record

- First preview workflow and initial Pages publication succeeded. A subsequent push published automatically, verified using the public `preview-commit.txt` against branch HEAD.
- PR #8 displays an active `pr-preview-8` deployment and a **View deployment** link.
- All three packaging tests pass on GitHub's Linux runner. The symlink test is skipped locally on Windows because creating a symlink requires additional OS privileges.
- Actionlint 1.7.12 passes with only its unsupported `concurrency.queue` diagnostic ignored. `queue: max` is supported by current GitHub documentation and accepted by the successful Actions runs; it preserves queued cleanup events.
- Independent review corrected Pages-read permissions and queuing. Closed-PR cleanup bypasses packaging/tests and root publication so unrelated build failures cannot block removal.
- Both public Home/About HTML files match their respective `main` and PR sources byte-for-byte. Mobile About has no horizontal overflow at 390px; relative navigation and the original GIFs work on the native preview URL.
- Pages source is now `gh-pages / (root)`. Activation verified the live and preview Git blob hashes before switching. The first publication needed an explicit Pages build request; subsequent publishing-branch updates triggered Pages automatically.
- No source changes were merged to `main`, and no PR comments were posted. Fork PRs, closing a PR, and merging into `main` were reviewed in the workflow but not exercised against real PR lifecycle events during setup.
