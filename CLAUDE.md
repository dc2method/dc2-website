# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**DocDriven Website V1.0** is a professional documentation website for the "Structured LLM Development" methodology. The site demonstrates enterprise-grade web development practices while documenting a 6-phase methodology for structured AI-assisted software development.

**Tech Stack**: Astro 4.x (Islands Architecture), React 18+ (interactive components only), TypeScript, Content Collections

**Performance Targets**:
- Lighthouse Score: 98-100/100 (all categories)
- Bundle Size: ~50KB initial load
- First Contentful Paint: <1s
- Time to Interactive: <2s

## Build & Development Commands

### Essential Commands

```bash
# Install dependencies
npm install

# Start development server (http://localhost:4321)
npm run dev

# Production build (outputs to dist/)
npm run build

# Preview production build locally
npm run preview

# Type checking
npx astro check
```

### Common Development Tasks

```bash
# Add new Astro integration
npx astro add <integration-name>

# Build and analyze bundle size
npm run build && npx astro build --analyze

# Run with verbose logging for debugging
npm run dev -- --verbose
```

## Architecture & Code Structure

### Astro Islands Architecture

This project uses **Islands Architecture** - the core principle that distinguishes this from traditional React/SPA frameworks:

- **Static by default**: All components render to HTML at build time (SSG)
- **Selective hydration**: JavaScript loads ONLY for interactive components
- **Component directives**: Use `client:*` directives to control when/how components hydrate

**Key directive used**: `client:visible` - Hydrates component only when it becomes visible in viewport (used for 6-phase diagram)

### Project Structure

```
src/
├── pages/              # File-based routing (/ = index.astro)
│   ├── index.astro     # Homepage (French default)
│   ├── about.astro     # About page
│   ├── [...slug].astro # Dynamic docs routes (French)
│   └── en/             # English versions
│       ├── index.astro
│       ├── about.astro
│       └── [...slug].astro
├── content/            # Content Collections (type-safe Markdown)
│   ├── config.ts       # Zod schema definitions
│   └── docs/
│       ├── fr/         # French documentation
│       └── en/         # English documentation
├── components/
│   ├── Homepage/       # Homepage-specific Astro components
│   ├── LanguageSwitcher.astro
│   ├── LanguageDetector.astro
│   ├── Navbar.astro
│   └── Footer.astro
├── layouts/
│   ├── BaseLayout.astro    # Root HTML wrapper
│   ├── DocsLayout.astro    # Documentation pages with sidebar
│   └── HomeLayout.astro    # Homepage-specific layout
├── styles/
│   └── global.css          # DocDriven design system (palette, typography)
└── utils/
    └── i18n.ts             # Bilingual support helpers

public/                 # Static assets (served as-is)
└── img/                # Images, logos, diagrams
```

### Content Collections System

**Critical concept**: Content Collections provide type-safe Markdown with frontmatter validation.

**Schema** (`src/content/config.ts`):
```typescript
const docsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    sidebar_position: z.number().optional(),
    lang: z.enum(['fr', 'en']),
  }),
});
```

**Accessing content**:
```typescript
import { getCollection } from 'astro:content';

// Get all French docs
const frDocs = await getCollection('docs', ({ data }) => data.lang === 'fr');

// Render a specific doc
const { Content } = await entry.render();
```

**Adding new documentation**:
1. Create `.md` file in `src/content/docs/fr/` or `/en/`
2. Add required frontmatter (title, lang, sidebar_position)
3. Content automatically validated against Zod schema at build time
4. Accessible via `[...slug].astro` dynamic route

### Bilingual (i18n) Implementation

**Routing strategy**:
- French (default): `/`, `/intro`, `/about`
- English: `/en/`, `/en/intro`, `/en/about`
- Configured in `astro.config.mjs` with `prefixDefaultLocale: false`

**Translation system** (`src/utils/i18n.ts`):
- `getLocale(url)`: Extracts current language from URL
- `t(key, locale)`: Retrieves translated string
- `translations` object: Contains all UI strings

**Language detection**:
- `LanguageDetector.astro`: Client-side script (runs once on first visit)
- Detects `navigator.language`, stores preference in `localStorage`
- Redirects to appropriate locale if needed

### React Islands Integration

**When to use React vs Astro components**:
- **Astro**: Static content, server-rendered UI (Navbar, Footer, Hero sections)
- **React**: Interactive components requiring state (6-phase diagram with hover states)

**Example** (`DiagramSixPhase.tsx`):
```tsx
// src/components/DiagramSixPhase.tsx
export default function DiagramSixPhase() {
  const [activePhase, setActivePhase] = useState<number | null>(null);
  // ... React component logic
}
```

**Integration in Astro page**:
```astro
---
import DiagramSixPhase from '../components/DiagramSixPhase';
---

<section class="diagram-section">
  <!-- Only hydrates when visible in viewport -->
  <DiagramSixPhase client:visible />
</section>
```

**Performance consideration**: Each React island adds ~30-50KB to bundle. Use sparingly.

### Design System (DocDriven Identity)

**Palette** (defined in `src/styles/global.css`):
```css
--dd-primary: #1A2332;        /* Dark blue-grey - Authority */
--dd-secondary: #2E86AB;      /* Industrial blue - Trust */
--dd-accent-positive: #06A77D; /* Technical green - Validation */
--dd-accent-warning: #D64933;  /* Technical red - Guards */
--dd-neutral-light: #F0F4F8;   /* Bluish grey - Backgrounds */
--dd-neutral-dark: #2C3E50;    /* Slate grey - Text */
--dd-code-bg: #282C34;         /* Code block background */
```

**Typography**:
- Headings: JetBrains Mono Bold (16-48px) - Technical aesthetic
- Body: Inter Regular (16px / 1.6 line-height) - Readability
- Code: JetBrains Mono Regular (14px)

**Visual principle**: "Industrial Documentation" - Sober, professional, technical (not flashy startup aesthetic)

## Critical Constraints

### Business Context

This website serves dual purposes:
1. **Professional portfolio asset**: Demonstrates Eric Gauthier's senior-level expertise in architecture and AI methodology
2. **Open-source methodology documentation**: DocDriven as a framework bigger than its creator

**Key positioning requirement**: Clear separation between methodology (primary) and author (secondary):
- Homepage focuses 100% on methodology (zero author mention)
- About page contains author bio (linked from footer/nav)
- License: Creative Commons CC BY-SA 4.0

### Performance Requirements (Non-Negotiable)

**Why this matters**: Lighthouse 98-100 score serves as proof of professional competency during job interviews.

**Lighthouse targets**:
- Performance: 98-100/100
- Accessibility: 100/100
- Best Practices: 100/100
- SEO: 100/100

**Optimization strategies**:
- Minimize JavaScript (Astro Islands = only load what's interactive)
- WebP images with lazy loading
- Inline critical CSS
- Preload fonts
- No render-blocking resources

**Testing**:
```bash
# Build and run Lighthouse
npm run build
npx serve dist/
# Then run Lighthouse in Chrome DevTools
```

### Content Quality Standards

**Tone of voice** (from strategic architecture doc):
- **Sober**: No hype words ("revolutionary", "disruptive")
- **Confident**: Direct assertions, not hesitant
- **Educational**: Explains concepts, doesn't just sell benefits
- **Authentic**: Acknowledges limitations (V1.0, no case studies yet)

**Translation requirement**: All content must exist in both French and English with identical structure.

## Development Workflow

### Adding New Documentation Pages

1. Create Markdown file in appropriate language directory:
   ```bash
   # French
   src/content/docs/fr/new-page.md

   # English
   src/content/docs/en/new-page.md
   ```

2. Add required frontmatter:
   ```yaml
   ---
   title: "Page Title"
   description: "Short description for SEO"
   sidebar_position: 10  # Order in sidebar
   lang: fr  # or 'en'
   ---
   ```

3. Build to validate schema:
   ```bash
   npm run build
   ```
   Zod will error if frontmatter is invalid.

4. Page automatically available at `/new-page` (French) or `/en/new-page` (English)

### Modifying Homepage

Homepage consists of 5 main sections (see `src/pages/index.astro`):
1. Hero Section
2. Challenge Section (Why structured methodology?)
3. Architecture Section (6-phase diagram)
4. For Who Section (Self-qualification)
5. CTA Section (Next steps)

Each section should be a separate Astro component in `src/components/Homepage/`.

### Adding Static Assets

```bash
# Images, logos, diagrams
public/img/filename.png

# Reference in Markdown
![Alt text](/img/filename.png)

# Reference in Astro component
<img src="/img/filename.png" alt="..." />
```

### Styling Guidelines

**Prefer scoped styles** in Astro components:
```astro
<style>
  .component-class {
    /* Styles scoped to this component only */
  }
</style>
```

**Global styles** only for design system (colors, typography, resets).

**Responsive breakpoints**:
```css
@media (max-width: 768px) { /* Mobile */ }
@media (min-width: 769px) and (max-width: 1024px) { /* Tablet */ }
@media (min-width: 1025px) { /* Desktop */ }
```

## Common Pitfalls to Avoid

### Astro-Specific Issues

1. **Dynamic imports in frontmatter fail**: Astro components must use static imports in frontmatter
   ```astro
   ---
   // ❌ Won't work
   const Component = await import('./Component.astro');

   // ✅ Correct
   import Component from './Component.astro';
   ---
   ```

2. **Client directives on Astro components**: `client:*` only works with framework components (React, Vue, etc.)
   ```astro
   ❌ <AstroComponent client:visible />  # Error
   ✅ <ReactComponent client:visible />  # Works
   ```

3. **Props passing to islands**: Must be JSON-serializable
   ```astro
   ❌ <ReactIsland data={new Date()} />  # Fails
   ✅ <ReactIsland data={dateString} />  # Works
   ```

### Content Collections Issues

1. **Invalid frontmatter silently breaks build**: Always validate schema early
2. **File naming**: Hyphens in filenames (`my-page.md`), not underscores
3. **Slug generation**: Filename becomes URL slug (intro.md → /intro)

### Performance Pitfalls

1. **Over-using React**: Each island adds bundle size. Default to Astro components.
2. **Large images**: Compress and convert to WebP before adding to `public/img/`
3. **Third-party scripts**: Each external script impacts Lighthouse. Minimize.

## Project-Specific Conventions

### Commit Messages

Follow semantic commit format:
```
US[X]-T[Y.Z]: Short description

Example:
US1-T1.2: Configure astro.config.mjs for DocDriven
US6-T6.3: Create HeroSection component with bilingual support
```

### File Naming

- Components: PascalCase (`HeroSection.astro`, `DiagramSixPhase.tsx`)
- Layouts: PascalCase (`BaseLayout.astro`, `DocsLayout.astro`)
- Pages: kebab-case or lowercase (`index.astro`, `about.astro`)
- Content: kebab-case (`intro.md`, `phase1-architecture-strategique.md`)
- Utilities: camelCase (`i18n.ts`)

### TypeScript Strict Mode

Project uses TypeScript strict mode. All `.ts` and `.tsx` files must:
- Explicitly type function parameters
- Avoid `any` types
- Handle nullable values properly

```typescript
// ✅ Good
function getLocale(url: URL): 'fr' | 'en' {
  // ...
}

// ❌ Avoid
function getLocale(url) {
  // ...
}
```

## Testing & Validation

### Pre-Deployment Checklist

- [ ] Build succeeds: `npm run build`
- [ ] Type check passes: `npx astro check`
- [ ] All pages accessible in both languages
- [ ] Images load correctly
- [ ] Sidebar navigation works
- [ ] Language switcher functional
- [ ] Mobile responsive (test viewport 375px, 768px, 1920px)
- [ ] Lighthouse audit: 98-100/100 all categories
- [ ] Bundle size <50KB: Check `dist/_astro/` folder

### Browser Testing Matrix

Minimum browser support:
- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile Safari iOS (latest)
- Chrome Android (latest)

## Implementation Status

**Current Phase**: Project planning completed (Phase 1 Strategic Architecture + Phase 2 Tactical Plan)

**Next Steps** (from Implementation Checklist):
1. Setup Astro project (US1)
2. Configure bilingual support (US2)
3. Migrate content to Content Collections (US3)
4. Implement design system (US4)
5. Build 6-phase diagram React Island (US5)
6. Create homepage (US6)
7. Create About page (US7)
8. Final optimizations and Lighthouse audit (US8)

**Estimated Timeline**: 16-20 days (3.5 weeks with buffer)

## Key Resources

**Documentation**:
- Astro Docs: https://docs.astro.build
- Content Collections: https://docs.astro.build/en/guides/content-collections/
- Islands Architecture: https://docs.astro.build/en/concepts/islands/

**Project Specs** (in `specs/` directory):
- Phase 1 Strategic Architecture: Complete architectural vision
- Phase 2 Tactical Plan: Detailed implementation breakdown
- Implementation Checklist (Astro): Step-by-step development guide

**Source Content**:
- French: `documents-sources/francais/`
- English: `documents-sources/english/`
