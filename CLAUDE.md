# CLAUDE.md — QA Challenges Repo

Notes for any Claude session working on this repo.

## What this repo is

A series of take-home challenges for candidates applying to QA roles. Each challenge lives in its own `challenge-NN-<topic>/` directory and contains:

- **Candidate-facing files** (committed): `README.md`, `SPEC.md`, `TEMPLATE.md`, the artefact under test, etc.
- **Interviewer-only files** (gitignored): everything under `_interviewer/` — answer keys, grading rubrics, planted-bug catalogues.

The `**/_interviewer/` pattern in `.gitignore` keeps interviewer materials out of the public repo. They will eventually live in a separate **private** repo; until then, see the backup section below.

## Where interviewer-only files live

There are **two locations** for any `_interviewer/` directory:

1. **In-repo (working copy):** `challenge-NN-<topic>/_interviewer/` — gitignored, used while authoring or grading. **Vulnerable to workspace resyncs:** because these files are untracked and ignored, a Conductor workspace reset or fresh clone will silently delete them.

2. **Backup (authoritative):** `~/qa-interviewer-materials/challenge-NN-<topic>/_interviewer/` — outside the workspace, on local disk only. This is the source of truth until the private repo is set up.

## Rules for Claude

When **creating a new challenge**:
1. Author candidate-facing files in `challenge-NN-<topic>/` as usual.
2. Author interviewer-only files in `challenge-NN-<topic>/_interviewer/` as usual.
3. **Immediately mirror** the `_interviewer/` directory to `~/qa-interviewer-materials/challenge-NN-<topic>/_interviewer/`. Treat this as part of the same task — not a follow-up.

When **editing existing interviewer files** (rubric tweaks, new bug variants, scoring changes):
1. Edit them in-repo.
2. **Sync the change** to `~/qa-interviewer-materials/<same-path>/` immediately afterwards. Use `cp` or rewrite — whichever is simpler. Do not let the two copies drift.

When **the in-repo `_interviewer/` directory is missing** (workspace was reset):
1. Restore it by copying from `~/qa-interviewer-materials/<challenge-folder>/_interviewer/`.
2. Do not regenerate from memory — the backup is authoritative.

When the **private repo is eventually set up**:
- Update this CLAUDE.md to point at the private repo's clone path.
- The `~/qa-interviewer-materials/` backup directory can be retired at that point.
