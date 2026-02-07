"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/auth/login`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password }),
        }
      );

      if (!res.ok) throw new Error("Invalid credentials");

      const data = await res.json();

      localStorage.setItem("token", data.access_token);
      document.cookie = `token=${data.access_token}; path=/`;

      router.push("/");
    } catch (err) {
      setError("Invalid email or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#d4e4f7] to-[#fafafa]">
      <div
        className="glass rounded-2xl p-10 w-full max-w-md
                   shadow-[0_20px_50px_rgba(74,111,165,0.25)]
                   transform transition hover:scale-[1.02]"
      >
        {/* Header */}
        <h1 className="text-3xl font-bold text-[#4a6fa5] text-center mb-2">
          Welcome Back
        </h1>
        <p className="text-center text-gray-500 mb-8">
          Sign in to continue
        </p>

        {/* Error */}
        {error && (
          <div className="mb-4 text-sm text-red-500 text-center">
            {error}
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleLogin} className="space-y-6">
          <div>
            <label className="block text-sm font-medium mb-1">
              Email
            </label>
            <input
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-3 rounded-xl
                         border border-[#c0c0c0]
                         focus:outline-none focus:ring-2
                         focus:ring-[#4a6fa5]
                         bg-white"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">
              Password
            </label>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-xl
                         border border-[#c0c0c0]
                         focus:outline-none focus:ring-2
                         focus:ring-[#4a6fa5]
                         bg-white"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-xl font-semibold
                       bg-[#4a6fa5] text-white
                       shadow-[0_8px_20px_rgba(74,111,165,0.4)]
                       hover:shadow-[0_12px_28px_rgba(74,111,165,0.6)]
                       transition-all"
          >
            {loading ? "Signing in..." : "Login"}
          </button>
        </form>

        {/* Footer */}
        <p className="text-sm text-center text-gray-500 mt-8">
          Don&apos;t have an account?{" "}
          <span
            className="text-[#4a6fa5] font-semibold cursor-pointer hover:underline"
            onClick={() => router.push("/register")}
          >
            Register
          </span>
        </p>
      </div>
    </div>
  );
}