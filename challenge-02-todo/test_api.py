"""
Starter API test script for the AcmeTodo backend.

Run with:
    python3 test_api.py

Requires:
    pip install requests

The script must run against a freshly-started stack (no todos yet).
Add your own assertions below. Use plain `assert` statements; do not
introduce pytest or any other test framework.

Each test should print a one-line description of what it checks before
running, so the output reads like a checklist.
"""

import requests

BASE_URL = "http://localhost:5050/api"


def test_health():
    print("GET /api/health returns 200 and {ok: true}")
    res = requests.get(f"{BASE_URL}/health")
    assert res.status_code == 200, f"expected 200, got {res.status_code}"
    assert res.json() == {"ok": True}, f"unexpected body: {res.json()}"


# ---------------------------------------------------------------------------
# Add your assertions below. Refer to SPEC.md for expected behavior.
#
# Suggested areas to cover (you do not have to use all of these — pick the
# ones you think are most important and structure them however you like):
#
#   - POST /api/todos with a valid title
#   - POST /api/todos with an empty / whitespace-only title
#   - POST /api/todos with a very long title
#   - POST /api/todos trims leading/trailing whitespace
#   - GET /api/todos with no filter
#   - GET /api/todos?completed=true / ?completed=false
#   - PATCH /api/todos/<id>
#   - PATCH /api/todos/<id> on a non-existent id
#   - DELETE /api/todos/<id>
#   - DELETE /api/todos/<id> on a non-existent id
#   - DELETE /api/todos?completed=true (bulk-delete completed)
#   - The shape and types of the response body
#   - The format of the created_at timestamp
# ---------------------------------------------------------------------------


def main():
    test_health()
    # Call your own test functions here.
    print("\nAll assertions passed.")


if __name__ == "__main__":
    main()
