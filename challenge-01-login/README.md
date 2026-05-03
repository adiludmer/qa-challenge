# Challenge 01 — Find the Bugs in the Login Page

Welcome! This is the first challenge in the QA series. Its goal is to evaluate how you **think about quality**, not how much you can code.

## What you're given

- `index.html` — a working login page for "AcmePortal". Open it in any modern browser (just double-click the file).
- `SPEC.md` — the product specification the developers were supposed to implement. This is your source of truth for *expected* behavior.
- `TEMPLATE.md` — the template you'll use to write your bug reports.

## What you have to do

The login page in `index.html` contains **multiple intentional bugs** — places where the implementation does not match the specification. Your job:

### Part 1 — Test Plan (do this first, *before* exploring the app)

Read `SPEC.md` carefully. Write a list of **5 to 10 test cases** you think should be run against this page. For each one, write:

- A short title
- The steps you'd take
- What you'd expect to see if the page is correct

Save this as `test-plan.md`. **Do not edit it later** — we want to see what you'd test before you've seen the app behave.

### Part 2 — Bug Reports

Now actually use the page. Try things. Try to break it. Compare what you observe against the spec.

For every bug you find, fill out one entry in `TEMPLATE.md`. Be precise — a developer should be able to reproduce the bug from your steps without asking you any questions.

Save your bug list as `bugs.md`.

### Part 3 — Reflection

In `reflection.md`, write a single short paragraph (3–6 sentences) answering:

> *Which test cases from your test plan turned up no bugs? Why does that still matter, and how confident are you that there are no bugs in those areas?*

## Time

Plan to spend about **60 to 90 minutes** total. If you find yourself spending much more, stop and submit what you have — we'd rather see your honest output than a polished, padded one.

## What we're evaluating

| | |
|---|---|
| **Coverage** | Did you find a good fraction of the bugs? Did you cover the spec systematically? |
| **Report quality** | Can a developer reproduce each bug from your steps alone? Is severity sensible? |
| **Test planning** | Did your plan show structured thinking, or was it ad-hoc? |
| **Honesty** | Did you mark uncertain areas as uncertain? Did you avoid claiming bugs that aren't actually bugs? |

## Tips

- Don't read the source code of `index.html`. Test it like a user.
- A bug isn't only a crash. Anything that contradicts the spec — wording, behavior, layout, accessibility — is a bug.
- Test edge cases: empty inputs, very long inputs, special characters, copy-paste, repeated submits, narrow window widths.
- Keep your browser's developer tools open. The console may surface errors that aren't visible in the UI.

Good luck.
