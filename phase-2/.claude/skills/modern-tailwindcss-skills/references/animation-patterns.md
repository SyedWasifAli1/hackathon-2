# Animation and Transition Patterns

## Basic Transitions

### Transition Properties
- `transition` - Applies transition to all properties
- `transition-all` - Explicitly transitions all properties
- `transition-colors` - Transitions only color properties
- `transition-opacity` - Transitions only opacity
- `transition-shadow` - Transitions only shadow
- `transition-transform` - Transitions only transform

### Duration Classes
- `duration-75` - 75ms
- `duration-100` - 100ms
- `duration-150` - 150ms
- `duration-200` - 200ms
- `duration-300` - 300ms
- `duration-500` - 500ms
- `duration-700` - 700ms
- `duration-1000` - 1000ms

### Easing Functions
- `ease-linear` - Linear timing
- `ease-in` - Starts slow, ends fast
- `ease-out` - Starts fast, ends slow
- `ease-in-out` - Starts slow, speeds up, ends slow

## Transform Animations

### Scale Effects
- `scale-0` - Completely scaled down
- `scale-50` - 50% scale
- `scale-95` - 95% scale
- `scale-100` - 100% scale
- `scale-105` - 105% scale
- `scale-125` - 125% scale
- `scale-150` - 150% scale

### Rotation Effects
- `rotate-0` - No rotation
- `rotate-1` - 1 degree clockwise
- `rotate-2` - 2 degrees clockwise
- `rotate-12` - 12 degrees clockwise
- `-rotate-1` - 1 degree counter-clockwise
- `-rotate-2` - 2 degrees counter-clockwise

### Translation Effects
- `translate-x-0` - No horizontal translation
- `translate-x-1` - 0.25rem right
- `translate-x-2` - 0.5rem right
- `translate-x-4` - 1rem right
- `-translate-x-1` - 0.25rem left
- `translate-y-1` - 0.25rem down
- `-translate-y-1` - 0.25rem up

## Advanced Animation Techniques

### Keyframe Animations
Tailwind includes several built-in animations:
- `animate-spin` - Continuous rotation
- `animate-pulse` - Smooth opacity cycling
- `animate-bounce` - Bouncing effect
- `animate-ping` - Scaling pulse outward

### Custom Animation Classes
To use custom animations, define them in your CSS and use with `animate-[name]`.

## Hover State Animations

### Basic Hover Effects
```html
<button class="transition-all duration-300 ease-out hover:scale-105 hover:shadow-lg">
  Hover Effect
</button>
```

### Complex Hover Sequences
```html
<div class="group relative transition-all duration-300 ease-out">
  <div class="transform transition-transform duration-300 group-hover:-translate-y-1 group-hover:scale-105">
    Content
  </div>
  <div class="absolute inset-0 bg-blue-500 opacity-0 transition-opacity duration-300 group-hover:opacity-100"></div>
</div>
```

## Micro-Interactions

### Button Press Effects
```html
<button class="transform transition-all duration-150 active:scale-95">
  Press Effect
</button>
```

### Loading States
```html
<div class="flex items-center">
  <span class="animate-spin mr-2">Loading...</span>
</div>
```

### Progress Indicators
```html
<div class="h-2 bg-gray-200 rounded-full overflow-hidden">
  <div class="h-full bg-blue-500 animate-pulse w-1/2"></div>
</div>
```

## Performance Considerations

### Optimized Properties
- Animate only `transform` and `opacity` properties
- Use `will-change` for elements that animate frequently
- Avoid animating layout properties (width, height, margin, padding)

### Hardware Acceleration
```html
<div class="transform will-change-transform">
  Element that will be animated
</div>
```

## Responsive Animations

### Mobile Considerations
Consider reduced motion preferences:
```html
<div class="motion-safe:animate-pulse motion-reduce:animate-none">
  Animation respects user preferences
</div>
```

### Breakpoint-Specific Animations
```html
<div class="transition-transform duration-300 md:hover:scale-110 sm:hover:scale-105">
  Different hover scale on different screens
</div>
```