# Modern UI Design Patterns with Tailwind CSS

## Glassmorphism

Glassmorphism is a popular design trend that creates frosted glass-like elements with transparency and blur effects.

### Implementation
```html
<div class="relative bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 shadow-xl p-6">
  <!-- Content -->
</div>
```

### Key Properties
- `bg-white/10` - White background with 10% opacity
- `backdrop-blur-lg` - Large backdrop blur effect
- `border border-white/20` - Subtle white border with 20% opacity
- `rounded-2xl` - Rounded corners
- `shadow-xl` - Extra large shadow for depth

### Variations
- Light glass: `bg-white/20` with `backdrop-blur-md`
- Dark glass: `bg-black/20` with `backdrop-blur-lg`
- Colored glass: Use gradient backgrounds with opacity

## Neumorphism

Neumorphism creates soft, extruded plastic-like effects using subtle shadows and highlights.

### Implementation
```html
<div class="bg-gray-100 rounded-2xl shadow-[8px_8px_16px_#d1d1d1,-8px_-8px_16px_#ffffff] p-6">
  <!-- Content -->
</div>
```

## 3D Transform Effects

### Perspective Containers
```html
<div class="perspective-1000 transform-style-3d">
  <!-- Elements that will be transformed in 3D space -->
</div>
```

### 3D Rotations
- `rotate-x-12` - Rotate 12 degrees around X-axis
- `rotate-y-12` - Rotate 12 degrees around Y-axis
- `rotate-z-12` - Rotate 12 degrees around Z-axis (same as regular rotate)

### 3D Translations
- `translate-3d-x-10` - Translate in 3D space along X-axis
- `translate-3d-y-10` - Translate in 3D space along Y-axis
- `translate-3d-z-10` - Translate in 3D space along Z-axis

## Depth and Layering

### Shadow Layers
- `shadow-sm` - Subtle shadow
- `shadow-md` - Medium shadow
- `shadow-lg` - Large shadow
- `shadow-xl` - Extra large shadow
- `shadow-2xl` - Double extra large shadow
- `shadow-inner` - Inner shadow

### Gradient Depths
```html
<div class="bg-gradient-to-br from-gray-50 to-gray-100">
  <!-- Content with subtle depth -->
</div>
```

## Hover and Interaction Effects

### Smooth Transitions
```html
<div class="transition-all duration-300 ease-out hover:scale-105 hover:rotate-2">
  <!-- Element that scales and rotates on hover -->
</div>
```

### Magnetic Buttons
Buttons that follow cursor movement slightly:
```html>
<button class="magnetic-trigger">
  <span class="magnetic-element transition-transform duration-300">Button</span>
</button>
```