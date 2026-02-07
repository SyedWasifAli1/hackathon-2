"use client";

import { Todo } from "@/lib/types";

export default function TodoCard({
  todo,
  onToggle,
  onDelete,
  onEdit, // 🔹 new callback
}: {
  todo: Todo;
  onToggle: (id: string, completed: boolean) => void;
  onDelete: (id: string) => void;
  onEdit?: (todo: Todo) => void; // optional
}) {
  return (
    <div
      className="glass rounded-2xl p-6 shadow-[0_14px_36px_rgba(74,111,165,0.25)] hover:scale-[1.02] transition"
    >
      <div className="flex justify-between items-start">
        <div>
          <h3
            className={`text-lg font-semibold ${todo.completed ? "line-through text-gray-400" : ""}`}
          >
            {todo.title}
          </h3>
          <p className="text-gray-500 mt-1">{todo.description}</p>
        </div>

        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => onToggle(todo.id, !todo.completed)}
          className="w-5 h-5 accent-[#4a6fa5]"
        />
      </div>

      <div className="flex justify-between mt-4">
        <button
          onClick={() => onDelete(todo.id)}
          className="text-sm text-red-500 hover:underline"
        >
          Delete
        </button>

        {onEdit && (
          <button
            onClick={() => onEdit(todo)}
            className="text-sm text-[#4a6fa5] hover:underline"
          >
            Edit
          </button>
        )}
      </div>
    </div>
  );
}