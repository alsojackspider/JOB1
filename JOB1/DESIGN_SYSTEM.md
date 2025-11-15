# Job Portal - Design System & CSS Specifications

## Color Palette

### Primary Colors
```css
--primary-color: #2563eb    /* Bright Blue - Primary CTA, Links, Icons */
--secondary-color: #1e40af  /* Dark Blue - Gradients, Hover States */
--accent-color: #f59e0b     /* Amber/Gold - Highlights, Accents */
```

### Neutral Colors
```css
--text-dark: var(--secondary-color)    /* Headings, Body Text */
--text-light: #6b7280                   /* Secondary Text, Meta Info */
--background: #f9fafb                   /* Page Background */
--border: #e5e7eb                       /* Dividers, Borders */
--white: #ffffff                        /* Cards, Containers */
```

### Status Colors
```css
--success: #d1fae5 / #065f46   /* Accepted, Positive Actions */
--warning: #fef3c7 / #92400e   /* Pending, Caution */
--error: #fee2e2 / #7f1d1d     /* Rejected, Negative Actions */
--info: #dbeafe / #1e40af      /* Information, Hints */
```

---

## Typography

### Font Stack
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
```

### Font Sizes
```css
h1: 3.5rem (56px)     /* Page Titles, Hero Headlines */
h2: 2rem (32px)       /* Section Headers */
h3: 1.3rem (20px)     /* Subsection Headers */
h4: 1.1rem (18px)     /* Form Section Headers */
h5: 1rem (16px)       /* Card Titles, Labels */
body: 1rem (16px)     /* Regular Text */
small: 0.9rem (14px)  /* Help Text, Captions */
```

### Font Weights
```css
regular: 400
medium: 500
semibold: 600
bold: 700
```

---

## Spacing System

### Padding
```css
xs: 8px
sm: 12px
md: 15px
lg: 20px
xl: 30px
2xl: 40px
```

### Margins
```css
xs: 4px
sm: 8px
md: 12px
lg: 20px
xl: 30px
2xl: 40px
```

### Line Height
```css
tight: 1.2
normal: 1.6
relaxed: 1.8
```

---

## Components

### Buttons

#### Primary Button
```css
background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%)
color: white
padding: 12px 30px
border-radius: 10px
font-weight: 600
transition: all 0.3s ease

hover:
  transform: translateY(-3px)
  box-shadow: 0 10px 25px rgba(37, 99, 235, 0.3)
```

#### Secondary Button
```css
background-color: #f3f4f6
color: #2563eb
border: 2px solid #2563eb
padding: 12px 30px
border-radius: 10px
font-weight: 600

hover:
  background-color: #2563eb
  color: white
  transform: translateY(-3px)
```

#### Icon Button
```css
display: inline-flex
align-items: center
gap: 8px
padding: 10px 20px
border-radius: 6px
```

### Cards

```css
background: white
border-radius: 12px / 15px
padding: 25px / 40px
box-shadow: 0 2px 10px rgba(0,0,0,0.08) / 0 5px 20px rgba(0,0,0,0.08)
transition: all 0.3s ease

hover:
  transform: translateY(-5px)
  box-shadow: 0 10px 30px rgba(0,0,0,0.12)
```

### Form Elements

#### Input Fields
```css
border: 2px solid #e5e7eb
border-radius: 10px
padding: 12px 15px
font-size: 1rem
transition: all 0.3s ease

focus:
  border-color: #2563eb
  box-shadow: 0 0 0 0.2rem rgba(37, 99, 235, 0.15)
  outline: none
```

#### Labels
```css
font-weight: 600
color: var(--text-dark)
margin-bottom: 8px
display: flex
align-items: center
gap: 8px

icon:
  color: var(--primary-color)
```

#### Textarea
```css
min-height: 100px
max-height: 300px
resize: vertical
border: 2px solid #e5e7eb
border-radius: 10px
padding: 12px 15px
font-family: inherit
```

### Badges & Tags

#### Status Badge
```css
display: inline-block
padding: 6px 12px
border-radius: 20px
font-weight: 600
font-size: 0.85rem
```

#### Skill Tag
```css
background-color: #e0e7ff
color: #2563eb
padding: 6px 12px / 8px 16px
border-radius: 20px
font-weight: 500
font-size: 0.9rem
```

---

## Layouts

### Grid Layout
```css
display: grid
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))
gap: 20px / 30px
```

### Flexbox Layout
```css
display: flex
align-items: center
justify-content: space-between
gap: 15px / 20px
flex-wrap: wrap
```

---

## Shadows

### Light Shadow (Subtle)
```css
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08)
```

### Medium Shadow
```css
box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08)
```

### Heavy Shadow (Hover)
```css
box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12)
```

### Button Shadow
```css
box-shadow: 0 10px 25px rgba(37, 99, 235, 0.3)
```

---

## Gradients

### Primary Gradient
```css
background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%)
```

### Accent Gradient
```css
background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%)
```

### Light Gradient (Background)
```css
background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)
```

---

## Animations

### Smooth Transitions
```css
transition: all 0.3s ease
transition: background-color 0.3s ease
transition: transform 0.3s ease
```

### Hover Effects
```css
hover:
  transform: translateY(-3px)        /* Lift effect */
  transform: translateY(-5px)        /* Larger lift */
  transform: scale(1.05)             /* Scale up */
  transform: translateX(-3px)        /* Slide left */
  box-shadow: enhanced shadow        /* Shadow enhancement */
  opacity: 0.9 / 0.95               /* Slight fade */
```

---

## Responsive Design

### Breakpoints
```css
mobile: < 576px
tablet: 576px - 992px
desktop: > 992px
```

### Media Query Examples
```css
@media (max-width: 768px) {
  grid-template-columns: 1fr
  padding: 20px
  font-size: 14px
}

@media (max-width: 576px) {
  padding: 15px
  gap: 12px
  font-size: 13px
}
```

---

## Icon Usage

### Font Awesome 6.0.0 Icons

#### Common Icons Used
```html
<!-- Navigation -->
<i class="fas fa-home"></i>
<i class="fas fa-briefcase"></i>
<i class="fas fa-file-alt"></i>
<i class="fas fa-building"></i>
<i class="fas fa-users"></i>

<!-- Actions -->
<i class="fas fa-search"></i>
<i class="fas fa-plus"></i>
<i class="fas fa-edit"></i>
<i class="fas fa-trash"></i>
<i class="fas fa-check"></i>
<i class="fas fa-times"></i>

<!-- Status -->
<i class="fas fa-check-circle"></i>
<i class="fas fa-times-circle"></i>
<i class="fas fa-hourglass-half"></i>

<!-- Info -->
<i class="fas fa-info-circle"></i>
<i class="fas fa-lightbulb"></i>
<i class="fas fa-star"></i>

<!-- Contact -->
<i class="fas fa-envelope"></i>
<i class="fas fa-phone"></i>
<i class="fas fa-map-marker-alt"></i>
```

---

## Accessibility

### Color Contrast
- Primary text on white: #1e40af (WCAG AA)
- Secondary text on white: #6b7280 (WCAG AA)
- Sufficient contrast on all status colors

### Focus States
```css
focus:
  outline: 2px solid #2563eb
  outline-offset: 2px
```

### Semantic HTML
- Use `<button>` for buttons
- Use `<a>` for links
- Use `<label>` for form labels
- Use `<h1>` to `<h6>` for headings
- Use `<section>` for sections

---

## Print Styles

For resume and document printing:
```css
@media print {
  body { background: white }
  .no-print { display: none }
  box-shadow { box-shadow: none }
  page-break-after: always
}
```

---

## File Uploads

### Upload Area
```css
border: 2px dashed #2563eb
border-radius: 10px
padding: 30px
text-align: center
background-color: #f0f9ff
transition: all 0.3s ease

hover:
  background-color: #e0e7ff
  border-color: #1e40af
```

---

## Section Spacing

### Page Sections
```css
padding: 50px 0      /* Headers */
padding: 40px        /* Cards */
padding: 35px        /* Form Sections */
margin-bottom: 30px  /* Between Sections */
margin-bottom: 40px  /* Between Major Sections */
```

---

## Utility Classes

### Text Alignment
```css
.text-center { text-align: center }
.text-left { text-align: left }
.text-right { text-align: right }
```

### Visibility
```css
.hidden { display: none }
.visible { display: block }
.invisible { visibility: hidden }
```

### Spacing
```css
.mt-3 { margin-top: 1rem }
.mb-3 { margin-bottom: 1rem }
.p-3 { padding: 1rem }
```

---

## CSS Variables

All colors and sizes should use CSS variables for consistency:

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #1e40af;
  --accent-color: #f59e0b;
  --text-dark: #1e40af;
  --text-light: #6b7280;
  --background: #f9fafb;
  --border: #e5e7eb;
  --white: #ffffff;
  
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-xl: 15px;
  
  --shadow-sm: 0 2px 10px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 5px 20px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.12);
}
```

---

## Implementation Guidelines

1. **Use CSS Variables**: Always reference --primary-color instead of hardcoding #2563eb
2. **Maintain Consistency**: Keep padding, border-radius, and shadow values consistent
3. **Responsive First**: Start with mobile layout, then enhance for larger screens
4. **Accessibility First**: Ensure all elements have proper contrast and focus states
5. **Performance**: Minimize CSS, optimize images, use efficient selectors

---

## Browser Support

✅ Chrome/Edge (v90+)
✅ Firefox (v88+)
✅ Safari (v14+)
✅ Mobile Safari (iOS 12+)
✅ Chrome Mobile (v90+)

---

**Last Updated**: November 14, 2025
**Version**: 1.0
