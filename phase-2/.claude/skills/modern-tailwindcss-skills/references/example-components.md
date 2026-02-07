# Example Components

## 3D Animated Button

```html
<button class="relative overflow-hidden px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-medium rounded-xl transform transition-all duration-300 hover:scale-105 hover:shadow-2xl active:scale-95 group">
  <span class="relative z-10">3D Hover Effect</span>
  <!-- Shimmer effect -->
  <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent -skew-x-12 -translate-x-full group-hover:translate-x-full transition-transform duration-700 ease-out"></div>
  <!-- Inner shadow for depth -->
  <div class="absolute inset-0 bg-gradient-to-b from-white/10 to-transparent rounded-xl"></div>
</button>
```

## Glass Card with Tilt Effect

```html
<div class="group perspective-1000">
  <div class="relative bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 shadow-xl p-6 transform transition-transform duration-500 hover:rotate-y-6 hover:rotate-x-6 hover:scale-105">
    <div class="bg-white/80 backdrop-blur-sm rounded-xl p-6">
      <h3 class="text-xl font-bold text-gray-800 mb-2">Glass Card</h3>
      <p class="text-gray-600">This card has a beautiful glass effect with 3D hover transformation.</p>
    </div>
  </div>
</div>
```

## Floating Stats Panel

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
  <div class="relative bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-gray-800 dark:to-gray-900 rounded-2xl p-6 shadow-lg transform transition-all duration-300 hover:-translate-y-2 hover:shadow-xl">
    <div class="text-3xl font-bold text-blue-600 dark:text-blue-400">98%</div>
    <div class="text-gray-600 dark:text-gray-300 mt-1">Success Rate</div>
  </div>
  <div class="relative bg-gradient-to-br from-green-50 to-emerald-50 dark:from-gray-800 dark:to-gray-900 rounded-2xl p-6 shadow-lg transform transition-all duration-300 hover:-translate-y-2 hover:shadow-xl">
    <div class="text-3xl font-bold text-green-600 dark:text-green-400">24/7</div>
    <div class="text-gray-600 dark:text-gray-300 mt-1">Support</div>
  </div>
  <div class="relative bg-gradient-to-br from-purple-50 to-violet-50 dark:from-gray-800 dark:to-gray-900 rounded-2xl p-6 shadow-lg transform transition-all duration-300 hover:-translate-y-2 hover:shadow-xl">
    <div class="text-3xl font-bold text-purple-600 dark:text-purple-400">10K+</div>
    <div class="text-gray-600 dark:text-gray-300 mt-1">Users</div>
  </div>
</div>
```

## Animated Hero Section

```html
<section class="relative bg-gradient-to-br from-indigo-50 via-white to-cyan-50 dark:from-gray-900 dark:via-gray-800 dark:to-indigo-900 py-20 overflow-hidden">
  <div class="absolute top-0 left-0 w-full h-full opacity-30 overflow-hidden">
    <div class="absolute -top-1/2 -left-1/2 w-[200%] h-[200%] animate-spin-slow" style="animation-duration: 60s;">
      <div class="absolute top-1/4 left-1/4 w-64 h-64 bg-blue-200 dark:bg-blue-900/30 rounded-full blur-3xl opacity-50"></div>
      <div class="absolute bottom-1/3 right-1/4 w-72 h-72 bg-purple-200 dark:bg-purple-900/30 rounded-full blur-3xl opacity-50"></div>
    </div>
  </div>
  <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <h1 class="text-4xl md:text-6xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-6">
      Modern UI Experience
    </h1>
    <p class="text-xl text-gray-600 dark:text-gray-300 max-w-2xl mx-auto mb-10">
      Beautiful, animated interfaces crafted with Tailwind CSS and modern design principles.
    </p>
    <div class="flex justify-center gap-4">
      <button class="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-medium rounded-lg transform transition-all duration-300 hover:scale-105 hover:shadow-lg active:scale-95">
        Get Started
      </button>
      <button class="px-8 py-3 bg-white dark:bg-gray-800 text-gray-900 dark:text-white font-medium rounded-lg border border-gray-200 dark:border-gray-700 transform transition-all duration-300 hover:scale-105 hover:shadow-lg active:scale-95">
        Learn More
      </button>
    </div>
  </div>
</section>
```

## Modal with Glass Background

```html
<div class="fixed inset-0 bg-black/30 backdrop-blur-sm flex items-center justify-center p-4 z-50">
  <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl max-w-md w-full transform transition-all duration-300 scale-95 animate-in fade-in-90 zoom-in-90">
    <div class="p-6">
      <div class="flex justify-between items-start mb-4">
        <h3 class="text-xl font-bold text-gray-900 dark:text-white">Modal Title</h3>
        <button class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <p class="text-gray-600 dark:text-gray-300 mb-6">
        This modal has a beautiful glass effect background with smooth entrance animation.
      </p>
      <div class="flex justify-end gap-3">
        <button class="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors">
          Cancel
        </button>
        <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
          Confirm
        </button>
      </div>
    </div>
  </div>
</div>
```