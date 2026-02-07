"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import TodoCard from "@/components/TodoCard";
import TodoForm from "@/components/TodoForm";
import { Todo } from "@/lib/types";

type FormTodo = {
  id?: string;
  title: string;
  description?: string;
  completed?: boolean;
};

// Helper to call backend with JWT token
async function apiFetch(path: string, options: RequestInit = {}) {
  const token = localStorage.getItem("token");
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      ...(options.headers || {}),
    },
  });

  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || "API error");
  return data;
}

export default function TodosPage() {
  const router = useRouter();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(false);
  const [fetching, setFetching] = useState(true);

  // Modal state
  const [showForm, setShowForm] = useState(false);
  const [editTodo, setEditTodo] = useState<FormTodo | null>(null);

  // 🔹 Fetch todos
  const fetchTodos = async () => {
    try {
      setFetching(true);
      const data = await apiFetch("/todos/");

      // Response could be array or wrapped object
      if (Array.isArray(data)) {
        // Ensure API response conforms to our local Todo type
        const normalizedTodos = data.map((todo: any) => ({
          id: todo.id,
          title: todo.title || '',
          description: todo.description || '',
          completed: todo.completed || false
        }));
        setTodos(normalizedTodos);
      } else if (Array.isArray(data.todos)) {
        // Ensure API response conforms to our local Todo type
        const normalizedTodos = data.todos.map((todo: any) => ({
          id: todo.id,
          title: todo.title || '',
          description: todo.description || '',
          completed: todo.completed || false
        }));
        setTodos(normalizedTodos);
      } else {
        setTodos([]);
      }
    } catch (err: any) {
      console.error("Failed to load todos:", err.message);
      setTodos([]);
    } finally {
      setFetching(false);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  // 🔹 Add / Edit todo handler
  const handleSubmit = async (todo: FormTodo) => {
    try {
      if (todo.id) {
        // Edit
        await apiFetch(`/todos/${todo.id}`, {
          method: "PUT",
          body: JSON.stringify(todo),
        });
      } else {
        // Add new
        await apiFetch("/todos/", {
          method: "POST",
          body: JSON.stringify(todo),
        });
      }

      fetchTodos();
      setShowForm(false);
      setEditTodo(null);
    } catch (err: any) {
      alert("Failed to save todo: " + err.message);
    }
  };

  // 🔹 Toggle completed directly from card
  const toggleTodo = async (id: string, completed: boolean) => {
    try {
      await apiFetch(`/todos/${id}`, {
        method: "PUT",
        body: JSON.stringify({ completed }),
      });
      fetchTodos();
    } catch (err) {
      console.error("Failed to toggle todo:", err);
    }
  };

  // 🔹 Delete todo
  const deleteTodo = async (id: string) => {
    if (!confirm("Delete this todo?")) return;
    try {
      await apiFetch(`/todos/${id}`, { method: "DELETE" });
      fetchTodos();
    } catch (err) {
      console.error("Failed to delete todo:", err);
    }
  };

  // 🔹 Check token
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) router.push("/login");
  }, []);

  return (
    <div className="max-w-5xl mx-auto px-6 py-10 relative">
      {/* Header */}
      <h1 className="text-4xl font-bold text-[#4a6fa5] mb-2">Todos</h1>
      <p className="text-gray-600 mb-8">Keep your work clean and organized</p>

      {/* Add Todo Button */}
      <button
        onClick={() => setShowForm(true)}
        className="mb-6 px-6 py-3 rounded-xl bg-[#4a6fa5] text-white font-semibold shadow-[0_8px_20px_rgba(74,111,165,0.4)] hover:shadow-[0_12px_28px_rgba(74,111,165,0.6)] transition"
      >
        Add Todo
      </button>

      {/* Todos Grid */}
      {fetching ? (
        <p className="text-center text-gray-500">Loading todos...</p>
      ) : todos.length > 0 ? (
        <div className="grid md:grid-cols-2 gap-6">
          {todos.map((todo) => (
            <TodoCard
              key={todo.id}
              todo={todo}
              onToggle={toggleTodo}
              onDelete={deleteTodo}
              onEdit={() => {
                // Convert Todo to FormTodo when setting edit state
                setEditTodo({
                  id: todo.id,
                  title: todo.title,
                  description: todo.description,
                  completed: todo.completed
                });
                setShowForm(true);
              }}
            />
          ))}
        </div>
      ) : (
        <p className="text-center text-gray-500 mt-10">No todos yet ❄️</p>
      )}

      {/* Modal Todo Form */}
      {showForm && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <TodoForm
            initialTodo={editTodo || undefined}
            onSubmit={handleSubmit}
            onClose={() => {
              setShowForm(false);
              setEditTodo(null);
            }}
          />
        </div>
      )}
    </div>
  );
}