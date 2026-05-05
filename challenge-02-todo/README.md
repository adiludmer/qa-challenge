# Challenge 02 — Find the Bugs in the Todo App

Welcome to challenge 02. Like challenge 01, this is about how you **think about quality**, not how much you can code. The new twist: the app has a **frontend and a backend**, and some of the bugs are only catchable through the UI, while others are only catchable by talking to the API directly.

## Prerequisites

- **Docker Desktop** installed and running. ([Download here](https://www.docker.com/products/docker-desktop/) if you don't have it.)
- **Python 3.9+** installed, with the `requests` library available (`pip install requests`).
- A modern browser (Chrome, Firefox, Safari, or Edge).

If `docker --version` and `python3 --version` both work in your terminal, you're set.

## What you're given

- `docker-compose.yml`, `backend/`, `frontend/` — the full app, ready to run.
- `SPEC.md` — the product specification. **This is your source of truth** for expected behavior.
- `TEMPLATE.md` — the template for bug reports.
- `test_api.py` — a starter Python script for your automated API tests. It already runs and passes one trivial assertion; your job is to add more.

> **Important:** Do not read the source code under `backend/` or `frontend/`. Test the app like a user (and like an API client). Reading the source defeats the purpose of the exercise and we will be able to tell.

## Running the app

From the `challenge-02-todo/` folder:

```bash
docker compose up --build
```

When you see logs from both `backend` and `frontend`, the app is up:

- Frontend: <http://localhost:8080>
- Backend API base URL: <http://localhost:5050/api>

To stop: press `Ctrl+C`, then optionally `docker compose down` to remove the containers.

A quick sanity check:

```bash
curl http://localhost:5050/api/health
# {"ok": true}
```

> The backend stores data **in memory**. Restarting the backend container wipes all todos. This is intentional — see `SPEC.md`.

## What you have to do

The app contains **multiple intentional bugs** — places where the implementation does not match `SPEC.md`. Your job has four parts.

### Part 1 — Test Plan (do this first, *before* exploring the app)

Read `SPEC.md` carefully. Write a list of **8 to 12 test cases** you think should be run against this app, covering both the UI and the API. For each one, write:

- A short title
- Whether you'd run it through the **UI** or the **API** (or both)
- The steps you'd take
- What you'd expect to see if the app is correct

Save this as `test-plan.md`. **Do not edit it later** — we want to see what you'd test before you've seen the app behave.

### Part 2 — Manual Bug Reports

Use the **UI** in your browser. Try things. Try to break it. Compare what you observe against the spec.

For every bug you find through the UI, fill out one entry in `TEMPLATE.md`. Be precise — a developer should be able to reproduce the bug from your steps without asking you any questions.

Save this as `bugs.md`.

### Part 3 — Automated API Tests

Open `test_api.py`. It already imports `requests`, defines `BASE_URL`, and contains one trivial assertion (the `/api/health` endpoint).

Add **at least 5 more assertions** that exercise the API endpoints described in `SPEC.md`. Aim for assertions that catch behavior the spec is explicit about — status codes, validation, response bodies, filter behavior, and so on.

Rules for your script:

- It must run as `python3 test_api.py` against a freshly-started stack (i.e., starting with no todos).
- It must use only the Python standard library plus `requests`. No `pytest`, no test frameworks — just `assert` statements. We want to read your assertions, not framework output.
- If an assertion fails, the script should exit with a non-zero exit code (the default behavior of a failed `assert` is fine).
- Print a one-line message before each assertion explaining what it tests, e.g., `print("POST /api/todos with empty title returns 400")`.

Submit your script as `test_api.py` (overwriting the starter). Each failing assertion in your script counts as evidence of a bug — list those bugs in `bugs.md` too, alongside your UI bugs, but tag each bug as `[UI]`, `[API]`, or `[both]` so we can see which surface caught it.

### Part 4 — Reflection

In `reflection.md`, write a short paragraph (4–8 sentences) answering:

> *Which bugs would you have missed if you had only tested the UI? Which would you have missed if you had only tested the API? What does that tell you about how to plan testing for an app like this in the future?*

## Time

Plan to spend about **90 to 120 minutes** total. If you find yourself spending much more, stop and submit what you have.

## What we're evaluating

| | |
|---|---|
| **Coverage** | Did you find a good fraction of the bugs across both surfaces? |
| **Report quality** | Can a developer reproduce each bug from your steps alone? Is severity sensible? |
| **Test planning** | Did your plan show structured thinking, including both UI and API cases? |
| **Automation literacy** | Are your assertions clear, focused, and aligned with the spec? Does your script run cleanly? |
| **Honesty** | Did you mark uncertain areas as uncertain? Did you avoid claiming bugs that aren't actually bugs? |

## Tips

- **Don't read the source.** Test the app like a user and like an API client.
- **Use the spec.** A bug is anything that contradicts `SPEC.md` — wording, behavior, status codes, response shape, layout.
- **Test both layers.** Some bugs only show up in the UI. Some only show up when you talk to the API. Some show up in both.
- **Use your browser's developer tools.** The Network tab is especially useful for seeing what the UI is actually sending and receiving.
- **`curl` is your friend** for poking at the API by hand before you formalize an assertion in your script. Example:
  ```bash
  curl -i -X POST http://localhost:5050/api/todos \
       -H 'Content-Type: application/json' \
       -d '{"title":"buy milk"}'
  ```
- **Don't try to find every single bug.** A clear, well-organized report of most of them beats a sprawling, sloppy one.

Good luck.
