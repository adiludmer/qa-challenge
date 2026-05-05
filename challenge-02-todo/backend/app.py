from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

_todos = {}
_next_id = 1


def _serialize(todo):
    return {
        "id": todo["id"],
        "title": todo["title"],
        "completed": todo["completed"],
        "created_at": todo["created_at"],
    }


@app.get("/api/todos")
def list_todos():
    completed = request.args.get("completed")
    items = sorted(_todos.values(), key=lambda t: t["id"])
    if completed == "false":
        items = [t for t in items if not t["completed"]]
    return jsonify([_serialize(t) for t in items]), 200


@app.post("/api/todos")
def create_todo():
    global _next_id
    body = request.get_json(silent=True) or {}
    title = body.get("title", "")
    if not isinstance(title, str):
        return jsonify({"error": "title must be a string"}), 400

    todo = {
        "id": _next_id,
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    }
    _todos[_next_id] = todo
    _next_id += 1
    return jsonify(_serialize(todo)), 201


@app.patch("/api/todos/<int:todo_id>")
def update_todo(todo_id):
    todo = _todos.get(todo_id)
    if todo is None:
        return jsonify({"error": "todo not found"}), 404

    body = request.get_json(silent=True) or {}

    if "title" in body:
        title = body["title"]
        if not isinstance(title, str):
            return jsonify({"error": "title must be a string"}), 400
        title = title.strip()
        if len(title) == 0:
            return jsonify({"error": "title is required"}), 400
        if len(title) > 200:
            return jsonify({"error": "title must be 200 characters or fewer"}), 400
        todo["title"] = title

    if "completed" in body:
        completed = body["completed"]
        if not isinstance(completed, bool):
            return jsonify({"error": "completed must be a boolean"}), 400
        todo["completed"] = completed

    return jsonify(_serialize(todo)), 200


@app.delete("/api/todos/<int:todo_id>")
def delete_todo(todo_id):
    if todo_id in _todos:
        del _todos[todo_id]
    return ("", 200)


@app.delete("/api/todos")
def delete_completed():
    for tid in list(_todos.keys()):
        del _todos[tid]
    return ("", 204)


@app.get("/api/health")
def health():
    return jsonify({"ok": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
