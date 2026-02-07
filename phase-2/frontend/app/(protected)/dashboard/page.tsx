export default function DashboardPage() {
  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <h1 className="text-4xl font-bold text-[#4a6fa5] mb-2">
        Dashboard
      </h1>
      <p className="text-gray-600 mb-10">
        Manage your tasks with clarity and precision
      </p>

      {/* Cards */}
      <div className="grid md:grid-cols-3 gap-8">
        <div className="glass rounded-2xl p-8
                        shadow-[0_16px_40px_rgba(74,111,165,0.25)]
                        hover:scale-[1.03] transition">
          <h3 className="text-lg font-semibold mb-2">
            Todos
          </h3>
          <p className="text-gray-500 mb-4">
            Create, update, and track your tasks
          </p>
          <span className="text-[#4a6fa5] font-semibold">
            Go to Todos →
          </span>
        </div>

        <div className="glass rounded-2xl p-8
                        shadow-[0_16px_40px_rgba(74,111,165,0.25)]
                        hover:scale-[1.03] transition">
          <h3 className="text-lg font-semibold mb-2">
            About
          </h3>
          <p className="text-gray-500 mb-4">
            Learn more about this application
          </p>
          <span className="text-[#4a6fa5] font-semibold">
            Learn More →
          </span>
        </div>

        <div className="glass rounded-2xl p-8
                        shadow-[0_16px_40px_rgba(74,111,165,0.25)]
                        hover:scale-[1.03] transition">
          <h3 className="text-lg font-semibold mb-2">
            Contact
          </h3>
          <p className="text-gray-500 mb-4">
            Get in touch or send feedback
          </p>
          <span className="text-[#4a6fa5] font-semibold">
            Contact Us →
          </span>
        </div>
      </div>
    </div>
  );
}