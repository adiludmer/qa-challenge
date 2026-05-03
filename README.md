# QA Challenges

A series of take-home challenges for candidates applying to QA roles with **very basic programming knowledge**. Each challenge is designed to evaluate a different aspect of the QA mindset — observation, structured reporting, adversarial thinking, automation literacy — without requiring deep coding skill.

## How to use

If you're a **candidate**: open the folder for the challenge you've been assigned and read its `README.md`. Everything you need is in that folder.

If you're an **interviewer**: each challenge folder contains a candidate-facing portion (committed here) and an interviewer-only portion with answer keys and grading rubrics. The interviewer materials are kept in a separate private repository — they are excluded from this repo via `.gitignore`.

## Challenges

| # | Folder | Focus | Approx. time |
|---|---|---|---|
| 01 | [`challenge-01-login/`](./challenge-01-login/) | Black-box exploratory testing of a buggy login page; bug reports and test planning | 60–90 min |

More challenges will be added over time, building toward automation, API testing, and test design.

## Repo layout

```
.
├── README.md               # this file
├── .gitignore              # excludes interviewer-only materials
└── challenge-NN-<topic>/
    ├── README.md           # candidate instructions
    ├── SPEC.md             # requirements / source of truth
    ├── TEMPLATE.md         # bug report or submission template
    ├── index.html          # the artefact under test (varies by challenge)
    └── _interviewer/       # gitignored — answer key, rubric
```
