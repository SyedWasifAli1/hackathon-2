export default function AboutPage() {
  return (
    <div className="max-w-5xl mx-auto">
      {/* Header */}
      <h1 className="text-4xl font-bold text-[#4a6fa5] mb-3">
        About This App
      </h1>
      <p className="text-gray-600 mb-10">
        Built with clarity, precision, and performance in mind
      </p>

      {/* Content Cards */}
      <div className="grid md:grid-cols-2 gap-8">
        <div
          className="glass rounded-2xl p-8
                     shadow-[0_16px_40px_rgba(74,111,165,0.25)]
                     hover:scale-[1.02] transition"
        >
          <h2 className="text-xl font-semibold mb-3">
            ❄ Arctic Frost Design
          </h2>
          <p className="text-gray-600 leading-relaxed">
            This application uses the Arctic Frost design system —
            a clean, winter-inspired UI that focuses on clarity,
            minimalism, and professional aesthetics.
          </p>
        </div>

        <div
          className="glass rounded-2xl p-8
                     shadow-[0_16px_40px_rgba(74,111,165,0.25)]
                     hover:scale-[1.02] transition"
        >
          <h2 className="text-xl font-semibold mb-3">
            ⚙️ Technology Stack
          </h2>
          <ul className="text-gray-600 space-y-2">
            <li>• Next.js 16+ (App Router)</li>
            <li>• TypeScript</li>
            <li>• Tailwind CSS</li>
            <li>• FastAPI + JWT Authentication</li>
          </ul>
        </div>

        <div
          className="glass rounded-2xl p-8 md:col-span-2
                     shadow-[0_16px_40px_rgba(74,111,165,0.25)]
                     hover:scale-[1.02] transition"
        >
          <h2 className="text-xl font-semibold mb-3">
            🎯 Purpose
          </h2>
          <p className="text-gray-600 leading-relaxed">
            The goal of this app is to demonstrate a real-world,
            production-grade Todo system with secure authentication,
            clean UI, and scalable frontend architecture.
          </p>
        </div>
      </div>
    </div>
  );
}