# AcmeTodo — Product Specification

This is the requirements document the development team worked from. Use it as the **source of truth** for what the app is *supposed* to do. Any behavior that deviates from this spec is potentially a bug.

The app is a single-user todo list. There is no authentication. The frontend is a single page that talks to the backend over HTTP.

## Architecture

- **Frontend** is served at `http://localhost:8080`.
- **Backend** is served at `http://localhost:5050`. All API endpoints are under the `/api` prefix.
- The backend stores todos **in memory only**. Data is lost when the backend container restarts. (This is intentional for the challenge — you do not need to test persistence.)

## Data Model

A `Todo` has the following fields:

| Field | Type | Notes |
|---|---|---|
| `id` | integer | Auto-assigned by the server. Starts at 1, increments by 1 for each new todo. |
| `title` | string | The text of the todo. Required. |
| `completed` | boolean | Defaults to `false` for new todos. |
| `created_at` | string | ISO 8601 timestamp in **UTC** (e.g., `2026-05-05T14:30:00Z`). Set by the server when the todo is created. |

## API

All request and response bodies are JSON. The backend must send `Content-Type: application/json` on every JSON response.

### `GET /api/todos`

Returns all todos as a JSON array, in ascending order by `id`.

Optional query parameter:
- `completed=true` — return only completed todos.
- `completed=false` — return only active (not-completed) todos.
- (no parameter) — return all todos.

Response: `200 OK` with the array (possibly empty: `[]`).

### `POST /api/todos`

Creates a new todo.

Request body: `{"title": "<string>"}`

Validation:
- `title` is **required**. Missing or empty `title` (after trimming) must be rejected.
- `title` is automatically **trimmed** of leading and trailing whitespace before storing.
- `title` after trimming must be **between 1 and 200 characters**. Longer titles must be rejected.

On success: `201 Created` with the new todo as the response body.
On validation failure: `400 Bad Request` with a JSON body `{"error": "<message>"}`.

### `PATCH /api/todos/<id>`

Updates an existing todo. The request body may contain either or both fields:

```json
{"title": "<new title>", "completed": true}
```

Validation rules for `title` are the same as for `POST`. `completed` must be a boolean if present.

- On success: `200 OK` with the updated todo.
- If no todo with that `id` exists: `404 Not Found` with `{"error": "<message>"}`.
- On validation failure: `400 Bad Request` with `{"error": "<message>"}`.

### `DELETE /api/todos/<id>`

Deletes the todo with the given id.

- On success: `204 No Content` (empty body).
- If no todo with that `id` exists: `404 Not Found`.

### `DELETE /api/todos?completed=true`

Deletes **only** completed todos. Active (not-completed) todos must not be affected.

- On success: `204 No Content` (empty body).
- The query parameter `completed=true` is required for this bulk-delete form. Calling `DELETE /api/todos` with no parameter must be rejected with `400 Bad Request`.

## Frontend Behavior

### Layout

- A header titled **"AcmeTodo"**.
- A text input and an **Add** button for creating todos.
- A list of todos. Each row shows: a checkbox, the title, and a delete (✕) button.
- Below the list: a **counter** and a **filter row** (All / Active / Completed) and a **Clear completed** button.

### Adding a todo

- Typing in the input and pressing **Enter** must add the todo (equivalent to clicking Add).
- Clicking Add must add the todo.
- After a successful add, the input must be cleared and focus must remain in the input.

### Toggling completion

- Clicking a todo's checkbox toggles its `completed` state. Completed todos are visually distinct (e.g., strikethrough).

### Deleting

- Clicking the ✕ button on a row deletes that todo.
- Clicking **Clear completed** deletes all completed todos in one action.
- The **Clear completed** button must be **hidden** when there are no completed todos.

### Filtering

- **All** shows every todo.
- **Active** shows only not-completed todos.
- **Completed** shows only completed todos.
- The currently selected filter must be visually highlighted.

### Counter

- The counter shows the number of **active** (not-completed) todos, e.g., `3 items left` or `1 item left` (singular when exactly 1).

### Empty state

- When there are no todos at all, the list area shows the text: **"No todos yet — add your first one above."**

### Long titles

- Titles longer than the row width must wrap onto multiple lines. Nothing should overflow horizontally or be clipped.

### Responsiveness

- The page must remain usable from 320px to 1440px viewport width.

## Out of scope

- Authentication, multi-user support.
- Persistence across backend restarts.
- Edit-in-place of existing todos in the UI. (The `PATCH` endpoint exists in the API spec for the test script to exercise; the UI only needs to support toggle and delete.)
