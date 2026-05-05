# CLAUDE.md — QA Challenges Repo (public)

Notes for any Claude session working on this repo.

## What this repo is

The **public** half of a paired setup: take-home challenges for QA candidates. Each challenge lives in its own `challenge-NN-<topic>/` directory and contains:

- **Candidate-facing files** (committed here): `README.md`, `SPEC.md`, `TEMPLATE.md`, the artefact under test, etc.
- **Interviewer-only files** (gitignored under `_interviewer/`): answer keys, grading rubrics, planted-bug catalogues. These are working copies — the source of truth lives in the private interviewer repo (see below).

The `**/_interviewer/` rule in `.gitignore` keeps interviewer materials from leaking into this public repo. Do not remove it.

## The private interviewer repo

Authoritative home for all interviewer-only materials:

- **Remote:** `git@github.com:adiludmer/qa-challenge-interviewer.git`
- **Canonical local clone:** `~/conductor/repos/qa-challenge-interviewer/`
- **Active Conductor workspaces:** `~/conductor/workspaces/qa-challenge-interviewer/<workspace-name>/`

Layout there mirrors this repo: one `challenge-NN-<topic>/` folder per challenge, containing `ANSWER_KEY.md` and `RUBRIC.md`.

## Rules for Claude

When **creating a new challenge**:
1. Author candidate-facing files here under `challenge-NN-<topic>/`.
2. Author `ANSWER_KEY.md` and `RUBRIC.md` in the **interviewer repo**, in `challenge-NN-<topic>/`. Open or use an existing workspace under `~/conductor/workspaces/qa-challenge-interviewer/` to make the change, then commit and push as a normal PR.
3. Optionally also write a working copy under `challenge-NN-<topic>/_interviewer/` here for convenience while authoring or grading. Treat it as a scratch copy — the interviewer repo wins on conflict.

When **editing existing interviewer files** (rubric tweaks, new bug variants, scoring changes):
1. Edit them in the interviewer repo and commit there.
2. If a `_interviewer/` working copy exists in this repo, sync it from the interviewer repo immediately to avoid drift.

When **the in-repo `_interviewer/` directory is missing** (workspace was reset, files wiped):
1. Restore by copying from the interviewer repo's working tree at `~/conductor/repos/qa-challenge-interviewer/<challenge>/` (or whichever workspace is current).
2. Do not regenerate from memory — the interviewer repo is authoritative.

## Retired locations

`~/qa-interviewer-materials/` was an interim local backup before the private repo existed. It is now redundant and should not be used. Safe to delete once you've confirmed everything is mirrored in the interviewer repo.
