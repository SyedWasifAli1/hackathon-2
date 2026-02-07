# Accessibility and Responsive Design

## Accessibility Standards

### Color Contrast
- Text and background must meet WCAG AA standards (4.5:1 for normal text, 3:1 for large text)
- Use Tailwind's contrast utilities: `text-gray-800` on `bg-white`
- Test with tools like Chrome's accessibility inspector

### Keyboard Navigation
- All interactive elements must be focusable
- Provide visible focus states: `focus:outline-none focus:ring-2 focus:ring-blue-500`
- Ensure logical tab order

### ARIA Attributes
- Use `role` attributes when needed: `role="button"`
- Implement `aria-label` for icon-only buttons: `aria-label="Close"`
- Use `aria-describedby` for additional context

### Screen Reader Support
- Provide alternative text for images: `alt="Descriptive text"`
- Use semantic HTML elements: `<nav>`, `<main>`, `<section>`
- Hide decorative elements: `aria-hidden="true"`

## Responsive Design Patterns

### Mobile-First Approach
Start with base styles and enhance for larger screens:
```html
<div class="p-4 md:p-6 lg:p-8">
  Content with increasing padding on larger screens
</div>
```

### Breakpoint Utilities
- `sm:` - 640px and above
- `md:` - 768px and above
- `lg:` - 1024px and above
- `xl:` - 1280px and above
- `2xl:` - 1536px and above

### Responsive Typography
```html
<h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl">
  Responsive heading
</h1>
```

### Flexible Grid Systems
```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  Responsive grid
</div>
```

## Dark Mode Implementation

### Automatic Dark Mode
```html
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white">
  Automatically adjusts for dark mode
</div>
```

### Manual Dark Mode Toggle
```html
<button class="dark:hidden">Show in light mode</button>
<button class="hidden dark:block">Show in dark mode</button>
```

## Touch and Pointer Considerations

### Touch Targets
- Minimum 44px touch targets for mobile
- Use `p-4` or similar to ensure adequate size
- Consider hover states not available on touch devices

### Pointer Media Queries
```html
<button class="hover:bg-blue-500 touch-none:hover:bg-blue-400">
  Hover effect disabled on touch devices
</button>
```

## Reduced Motion Support

### Respecting User Preferences
```html
<div class="motion-safe:animate-spin motion-reduce:animate-none">
  Respects user's reduced motion preference
</div>
```

### Alternative Interactions
Provide alternatives when animations are disabled:
```html
<button class="motion-safe:transition-transform motion-safe:hover:scale-105 motion-reduce:transition-none">
  Safe hover effect
</button>
```

## Internationalization Considerations

### Right-to-Left Support
- Use `rtl:` prefix for RTL-specific styles
- Consider text direction in layouts
- Mirror icons and directional elements

### Text Expansion
- Account for text expansion in other languages
- Use flexible layouts that accommodate longer text
- Test with placeholder text in different languages

## Testing Strategies

### Automated Testing
- Use tools like axe-core for accessibility testing
- Verify contrast ratios with automated tools
- Test responsive behavior across breakpoints

### Manual Testing
- Navigate with keyboard only
- Test with screen reader
- Verify touch target sizes
- Test in high contrast mode