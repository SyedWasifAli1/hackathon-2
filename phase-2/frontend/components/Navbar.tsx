"use client";

import { useRouter } from "next/navigation";

export default function Navbar() {
  const router = useRouter();

  const logout = () => {
    localStorage.removeItem("token");
    document.cookie = "token=; path=/; max-age=0";
    router.push("/login");
  };

  return (
    <nav
      className="glass mx-6  rounded-2xl px-8 py-4
                 flex items-center justify-between
                 shadow-[0_12px_30px_rgba(74,111,165,0.25)]
                 backdrop-blur-lg"
    >
      {/* Logo */}
      <div
        className="text-xl font-bold text-[#4a6fa5] cursor-pointer"
        onClick={() => router.push("/")}
      >
        ❄ TodoApp
      </div>

      {/* Links */}
      <div className="flex items-center gap-8 text-sm font-medium">
        <button
          onClick={() => router.push("/")}
          className="hover:text-[#4a6fa5] transition"
        >
          Dashboard
        </button>
        <button
          onClick={() => router.push("/todos")}
          className="hover:text-[#4a6fa5] transition"
        >
          Todos
        </button>
        <button
          onClick={() => router.push("/about")}
          className="hover:text-[#4a6fa5] transition"
        >
          About
        </button>
        <button
          onClick={() => router.push("/contact")}
          className="hover:text-[#4a6fa5] transition"
        >
          Contact
        </button>

        <button
          onClick={logout}
          className="ml-6 px-4 py-2 rounded-xl
                     bg-[#4a6fa5] text-white
                     shadow-[0_6px_18px_rgba(74,111,165,0.4)]
                     hover:shadow-[0_10px_24px_rgba(74,111,165,0.6)]
                     transition-all"
        >
          Logout
        </button>
      </div>
    </nav>
  );
}