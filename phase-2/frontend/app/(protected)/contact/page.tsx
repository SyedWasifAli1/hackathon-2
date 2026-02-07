"use client";

import { useState } from "react";

export default function ContactPage() {
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");

  const submitForm = (e: React.FormEvent) => {
    e.preventDefault();
    alert("Message sent ❄️ (demo only)");
    setName("");
    setMessage("");
  };

  return (
    <div className="max-w-4xl mx-auto">
      {/* Header */}
      <h1 className="text-4xl font-bold text-[#4a6fa5] mb-3">
        Contact Us
      </h1>
      <p className="text-gray-600 mb-10">
        We’d love to hear from you
      </p>

      <div
        className="glass rounded-2xl p-8
                   shadow-[0_16px_40px_rgba(74,111,165,0.25)]"
      >
        <form onSubmit={submitForm} className="space-y-6">
          <div>
            <label className="block text-sm font-medium mb-1">
              Your Name
            </label>
            <input
              required
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full px-4 py-3 rounded-xl
                         border border-[#c0c0c0]
                         focus:ring-2 focus:ring-[#4a6fa5]
                         outline-none"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">
              Message
            </label>
            <textarea
              required
              rows={5}
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              className="w-full px-4 py-3 rounded-xl
                         border border-[#c0c0c0]
                         focus:ring-2 focus:ring-[#4a6fa5]
                         outline-none resize-none"
            />
          </div>

          <button
            type="submit"
            className="px-6 py-3 rounded-xl
                       bg-[#4a6fa5] text-white font-semibold
                       shadow-[0_8px_20px_rgba(74,111,165,0.4)]
                       hover:shadow-[0_12px_28px_rgba(74,111,165,0.6)]
                       transition-all"
          >
            Send Message
          </button>
        </form>
      </div>
    </div>
  );
}