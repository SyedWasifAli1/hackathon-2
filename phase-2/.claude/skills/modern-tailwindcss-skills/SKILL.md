---
name: modern-tailwindcss-skills
description: |
  This skill should be used when creating modern, eye-catching, animated, and 3D-inspired UI components using Tailwind CSS.
  Generates clean, premium UI with strong visual hierarchy, balanced spacing, and modern aesthetics such as glassmorphism,
  soft shadows, subtle gradients, blur effects, and depth. 3D-like visuals are achieved using CSS transforms including
  perspective, rotate, translate, scale, and smooth hover interactions that feel natural and polished.
allowed-tools: Read, Grep, Glob
---

# Modern Tailwind CSS UI Components Skill

Builds modern, eye-catching, animated, and 3D-inspired UI components using Tailwind CSS with production-grade quality.

## Core Capabilities

### Visual Effects
- **Glassmorphism**: Achieved with `backdrop-blur-*`, semi-transparent backgrounds, and subtle borders
- **3D Transforms**: Using `transform`, `perspective-*`, `rotate-*`, `translate-*`, `scale-*` classes
- **Animations**: Smooth transitions with `transition-*`, `duration-*`, `ease-*`, and `animate-*`
- **Depth Effects**: Shadows (`shadow-*`), gradients (`bg-gradient-*`), and layered positioning

### Component Types
- 3D and animated buttons (hover lift, glow, magnetic effects)
- Modern cards (glass, neon, floating, tilt-on-hover)
- Sticky and blurred navbars
- Hero sections with animated text and gradient backgrounds
- Modals, badges, stats panels, and UI sections

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Existing Tailwind configuration, design system patterns, component structure |
| **Conversation** | User's specific requirements, design preferences, accessibility needs |
| **Skill References** | Modern UI patterns, Tailwind best practices, accessibility guidelines |
| **User Guidelines** | Project-specific conventions, brand guidelines, responsive requirements |

Ensure all required context is gathered before implementing.

## Implementation Guidelines

### 1. Utility-First Approach
- Use Tailwind's utility classes exclusively
- Avoid inline styles and custom CSS unless unavoidable
- Combine utilities to achieve complex effects

### 2. Responsive Design
- Apply mobile-first responsive design with Tailwind breakpoints
- Use `sm:`, `md:`, `lg:`, `xl:`, `2xl:` prefixes appropriately
- Consider touch targets and mobile UX

### 3. Accessibility Standards
- Include proper ARIA attributes
- Ensure adequate color contrast ratios
- Maintain keyboard navigability
- Use semantic HTML elements

### 4. Performance Optimization
- Leverage Tailwind's JIT compiler for smaller CSS bundles
- Remove unused classes in production builds
- Optimize animations to prevent layout thrashing

## Component Implementation Patterns

### Glassmorphism Effect
```html
<div class="relative bg-white/10 backdrop-blur-lg rounded-xl border border-white/20 shadow-lg p-6">
  <!-- Content -->
</div>
```

### 3D Card with Hover Effect
```html
<div class="group relative transform transition-transform duration-300 hover:rotate-y-6 hover:rotate-x-6 hover:scale-105">
  <div class="bg-white/80 backdrop-blur-sm rounded-xl p-6 shadow-xl">
    <!-- Card content -->
  </div>
</div>
```

### Animated Button with Magnetic Effect
```html
<button class="relative overflow-hidden px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg transform transition-all duration-300 hover:scale-105 hover:shadow-lg active:scale-95">
  <span class="relative z-10">Button Text</span>
  <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
</button>
```

### Perspective Container
```html
<div class="perspective-1000 transform-style-3d">
  <!-- Elements with 3D transforms -->
</div>
```

## Modern UI Aesthetics

### Color Palettes
- Use Tailwind's extended color palette with opacity modifiers
- Apply subtle gradients for depth: `bg-gradient-to-br from-indigo-50 to-purple-50`
- Implement dark mode support with `dark:` variants

### Spacing and Layout
- Follow Tailwind's spacing scale consistently
- Use flexbox and grid for complex layouts
- Maintain visual rhythm with consistent padding/margin

### Typography
- Apply responsive typography with `text-*` classes
- Use font weights strategically for hierarchy
- Maintain readability with proper line-height

## Animation Principles

### Smooth Transitions
- Use `transition-all` or specific property transitions
- Apply appropriate durations (150ms-300ms for micro-interactions)
- Choose proper easing functions (`ease-in-out`, `ease-out`)

### Interactive States
- Define clear hover, focus, and active states
- Use `group` classes to coordinate parent-child animations
- Ensure states are predictable and accessible

### Performance Considerations
- Animate only `transform` and `opacity` properties when possible
- Use `will-change` for elements that animate frequently
- Test animations on lower-powered devices

## Quality Standards

### Code Quality
- Clean, readable HTML structure
- Proper class organization and grouping
- Semantic markup for accessibility

### Visual Consistency
- Consistent spacing, colors, and typography
- Unified animation patterns across components
- Adherence to design system principles

### Cross-Browser Compatibility
- Test with modern browsers supporting CSS transforms
- Provide graceful degradation where needed
- Validate accessibility features

## Validation Checklist

Before delivering components, verify:

- [ ] All interactive elements have proper focus states
- [ ] Color contrast meets WCAG AA standards
- [ ] Components are responsive across all breakpoints
- [ ] Animations perform well on mobile devices
- [ ] Semantic HTML is maintained
- [ ] No custom CSS is required (only Tailwind utilities)
- [ ] Components work in both light and dark modes
- [ ] Hover and focus states are consistent
- [ ] Accessibility attributes are properly applied
- [ ] Performance is optimized for production