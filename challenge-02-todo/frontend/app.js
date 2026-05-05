const API = "http://localhost:5050/api";

const input = document.getElementById("new-todo");
const addBtn = document.getElementById("add-btn");
const list = document.getElementById("todo-list");
const emptyState = document.getElementById("empty-state");
const counter = document.getElementById("counter");
const clearCompletedBtn = document.getElementById("clear-completed");
const filterBtns = document.querySelectorAll(".filter-btn");

let todos = [];
let currentFilter = "all";

async function fetchTodos() {
    const res = await fetch(`${API}/todos`);
    todos = await res.json();
    render();
}

async function addTodo(title) {
    const res = await fetch(`${API}/todos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title }),
    });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        alert(err.error || "Could not add todo");
        return;
    }
    input.value = "";
    input.focus();
    await fetchTodos();
}

async function toggleTodo(id, completed) {
    await fetch(`${API}/todos/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed }),
    });
    await fetchTodos();
}

async function deleteTodo(id) {
    await fetch(`${API}/todos/${id}`, { method: "DELETE" });
    await fetchTodos();
}

async function clearCompleted() {
    await fetch(`${API}/todos?completed=true`, { method: "DELETE" });
    await fetchTodos();
}

function render() {
    const visible = todos.filter((t) => {
        if (currentFilter === "active") return !t.completed;
        if (currentFilter === "completed") return t.completed;
        return true;
    });

    list.innerHTML = "";
    for (const t of visible) {
        const li = document.createElement("li");
        li.className = "todo-item" + (t.completed ? " completed" : "");

        const cb = document.createElement("input");
        cb.type = "checkbox";
        cb.checked = t.completed;
        cb.addEventListener("change", () => toggleTodo(t.id, cb.checked));

        const title = document.createElement("span");
        title.className = "title";
        title.textContent = t.title;

        const del = document.createElement("button");
        del.type = "button";
        del.className = "delete-btn";
        del.textContent = "✕";
        del.addEventListener("click", () => deleteTodo(t.id));

        li.appendChild(cb);
        li.appendChild(title);
        li.appendChild(del);
        list.appendChild(li);
    }

    emptyState.hidden = todos.length > 0;

    counter.textContent = `${todos.length} items left`;
}

addBtn.addEventListener("click", () => {
    const value = input.value.trim();
    if (value.length === 0) return;
    addTodo(value);
});

filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        currentFilter = btn.dataset.filter;
        filterBtns.forEach((b) => b.classList.toggle("active", b === btn));
        render();
    });
});

clearCompletedBtn.addEventListener("click", clearCompleted);

fetchTodos();
