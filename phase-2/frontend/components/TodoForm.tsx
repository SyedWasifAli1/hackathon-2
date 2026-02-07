"use client";

import { useState, useEffect } from "react";
import { Todo } from "@/lib/types";

type FormTodo = {
  id?: string;
  title: string;
  description?: string;
  completed?: boolean;
};

type TodoFormProps = {
  initialTodo?: FormTodo; // if editing
  onSubmit: (todo: FormTodo) => Promise<void>;
  onClose?: () => void; // for modal close
};

export default function TodoForm({ initialTodo, onSubmit, onClose }: TodoFormProps) {
  const [title, setTitle] = useState(initialTodo?.title || "");
  const [description, setDescription] = useState(initialTodo?.description || "");
  const [completed, setCompleted] = useState(initialTodo?.completed || false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (initialTodo) {
      setTitle(initialTodo.title);
      setDescription(initialTodo.description || "");
      setCompleted(initialTodo.completed || false);
    }
  }, [initialTodo]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    setLoading(true);
    try {
      // Ensure all required fields are provided
      const todoToSubmit: FormTodo = {
        id: initialTodo?.id,
        title,
        description: description || "",
        completed: completed || false
      };
      
      await onSubmit(todoToSubmit);
      // reset form if adding new
      if (!initialTodo) {
        setTitle("");
        setDescription("");
        setCompleted(false);
      }
      onClose?.();
    } catch (err) {
      console.error(err);
      alert("Failed to save todo");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="glass rounded-2xl p-6 shadow-[0_16px_40px_rgba(74,111,165,0.25)] max-w-md mx-auto">
      <h2 className="text-2xl font-bold text-[#4a6fa5] mb-4">
        {initialTodo ? "Edit Todo" : "Add Todo"}
      </h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          type="text"
          placeholder="Todo Title"
          maxLength={100}
          required
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="px-4 py-3 rounded-xl border border-[#c0c0c0] focus:ring-2 focus:ring-[#4a6fa5] outline-none"
        />

        <textarea
          placeholder="Description (optional)"
          maxLength={1000}
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="px-4 py-3 rounded-xl border border-[#c0c0c0] focus:ring-2 focus:ring-[#4a6fa5] outline-none resize-none"
        />

        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={completed}
            onChange={() => setCompleted(!completed)}
            className="w-5 h-5 accent-[#4a6fa5]"
          />
          <span className="text-gray-700">Completed</span>
        </label>

        <div className="flex justify-between items-center mt-4">
          {onClose && (
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-xl bg-gray-200 hover:bg-gray-300 transition"
            >
              Cancel
            </button>
          )}
          <button
            type="submit"
            disabled={loading}
            className="px-6 py-2 rounded-xl bg-[#4a6fa5] text-white font-semibold shadow-[0_8px_20px_rgba(74,111,165,0.4)] hover:shadow-[0_12px_28px_rgba(74,111,165,0.6)] transition"
          >
            {loading ? "Saving..." : initialTodo ? "Update Todo" : "Add Todo"}
          </button>
        </div>
      </form>
    </div>
  );
}