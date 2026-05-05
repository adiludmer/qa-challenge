# CLAUDE.md — QA Challenges (Public Repo)

Notes for any Claude session working on this repo.

## What this repo is

The **public** repo of QA take-home challenges. Each challenge is a self-contained folder (`challenge-NN-<topic>/`) with candidate-facing materials: `README.md`, `SPEC.md`, `TEMPLATE.md`, and the artefact under test (a static page, a docker-compose stack, etc.).

Interviewer-only materials (answer keys, rubrics) live in the **private** counterpart repo at `qa-challenge-interviewer`. They must never be committed here.

## Companion repo

| | |
|---|---|
| Local path | `~/conductor/repos/qa-challenge-interviewer/` |
| Remote | `git@github.com:adiludmer/qa-challenge-interviewer.git` |
| Layout | one folder per challenge, mirroring this repo's `challenge-NN-<topic>/` naming, containing `ANSWER_KEY.md` and `RUBRIC.md` |

The companion repo also has its own `CLAUDE.md` describing where interviewer files belong and how candidate submissions are graded — read it before editing anything there.

## Rule: keep interviewer materials in lockstep

**Whenever you create or modify a challenge in this repo, the corresponding interviewer materials must stay in sync.** This is non-negotiable — a challenge without an answer key is not gradable, and a stale answer key produces wrong grades.

### When you create a new challenge

1. Author the candidate-facing files here in `challenge-NN-<topic>/`.
2. Update the top-level `README.md` table to advertise the new challenge.
3. **In the same session**, switch to `~/conductor/repos/qa-challenge-interviewer/`, branch from `main`, and create:
   - `challenge-NN-<topic>/ANSWER_KEY.md` — every planted bug, with severity, the spec section it violates, the source location, a one-line repro, and common candidate misses.
   - `challenge-NN-<topic>/RUBRIC.md` — scoring sections that match the deliverables this challenge asks for. Don't blindly copy the previous challenge's rubric; adjust section weights when a new deliverable is introduced (e.g., an automation script).
   - Update the interviewer repo's top-level `README.md` to list the new challenge.
4. Open **two PRs in parallel** — one in this repo for the candidate-facing change, one in the interviewer repo for the answer key + rubric. Cross-reference is not required, but landing them in the same window keeps reviewers honest.

### When you modify an existing challenge

If you change the spec, the artefact under test, or the candidate's deliverables in any way that could shift which bugs are valid, which severities apply, or how submissions are graded:

1. Re-read the matching `ANSWER_KEY.md` and `RUBRIC.md` in the interviewer repo.
2. Apply whatever updates are needed there in the same session — new bug entries, removed entries, severity changes, rubric weight changes.
3. If the interviewer materials don't yet exist for that challenge (e.g., someone authored a challenge here without the matching answer key), **stop and create them before continuing**. Do not leave the public repo ahead of the private one.
4. Open a PR in the interviewer repo for the update — even if it's a one-line tweak. The history matters for grading consistency.

### Branch naming

Use parallel branch names across the two repos so a reviewer can find the matching pair:

- Public repo: `adiludmer/challenge-N-<short-topic>`
- Interviewer repo: `adiludmer/challenge-N-answer-key`

### Smoke checks before opening the public PR

Before opening a PR here, confirm:

- [ ] The candidate-facing files build and run as the candidate would experience them. For containerized challenges that means `docker compose up --build` succeeds and the seeded bugs reproduce against the live stack.
- [ ] No interviewer-only material is in the diff. The `.gitignore` excludes `**/_interviewer/`, but verify with `git status`.
- [ ] The matching interviewer-repo PR is open (or already merged).

## What does NOT belong here

- Answer keys, rubrics, planted-bug catalogues, grading notes — those live in the interviewer repo.
- Specific candidate submissions or evaluations — those also live in the interviewer repo under `candidates/`.
- Solutions to challenges in any form, including hint files or worked examples.
