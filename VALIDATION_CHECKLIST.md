# Checklist de Validation Finale - DocDriven V1.0

## US8 : Optimisations Finales

Cette checklist vous permet de valider manuellement tous les aspects du site avant le déploiement en production.

---

## 📦 Build Production

### Commandes de test
```bash
# Build production
npm run build

# Preview build local
npm run preview
# Puis ouvrir http://localhost:4321
```

### Métriques attendues
- [ ] **22 pages générées** (2 homepages + 2 about + 18 docs)
- [ ] **Build time** : < 3 secondes
- [ ] **Bundle size** : ~195 KB (gzip ~61 KB)
- [ ] **Zero erreurs** de build
- [ ] **Zero warnings** critiques

---

## 🌐 Navigation & Routing

### Pages principales (FR)
- [ ] `/` - Homepage (5 sections visibles)
- [ ] `/about` - Page À Propos
- [ ] `/intro` - Introduction documentation
- [ ] `/phase1-architecture-strategique` - Phase 1
- [ ] `/licence` - Page licence

### Pages principales (EN)
- [ ] `/en/` - Homepage anglaise
- [ ] `/en/about` - About page
- [ ] `/en/intro` - Introduction
- [ ] `/en/phase1-architecture-strategique` - Phase 1
- [ ] `/en/licence` - License page

### Navbar
- [ ] Logo "DOC//DRIVEN" cliquable → homepage
- [ ] Lien "Méthodologie" → `/intro` (FR) ou `/en/intro` (EN)
- [ ] Lien "À Propos" → `/about` (FR) ou `/en/about` (EN)
- [ ] LanguageSwitcher fonctionnel (FR ↔ EN)
- [ ] Navbar sticky (reste en haut au scroll)

### Footer
- [ ] 3 colonnes visibles (About, Méthodologie, Ressources)
- [ ] Tous les liens fonctionnels
- [ ] Copyright avec lien vers About
- [ ] Lien licence fonctionnel

### Sidebar Documentation
- [ ] Visible sur pages docs uniquement (pas sur homepage/about)
- [ ] Logo DocDriven cliquable → homepage
- [ ] LanguageSwitcher présent
- [ ] 9 documents listés en ordre (sidebar_position)
- [ ] Page active surlignée en bleu
- [ ] Hover effects sur liens

---

## 📱 Responsive Design

### Mobile (< 768px)
Tester avec Chrome DevTools (F12) → Device toolbar → iPhone SE / iPhone 12

- [ ] **Homepage** : Sections stack verticalement
- [ ] **Navbar** : Stack vertical, liens centrés
- [ ] **Footer** : Stack vertical (colonnes → lignes)
- [ ] **Docs sidebar** : Height auto, pas de sticky
- [ ] **Phase cards** : 1 colonne
- [ ] **For Who cards** : 1 colonne
- [ ] **Typography** : Font-size réduit (responsive)

### Tablet (768px - 1024px)
- [ ] Grids adaptés (2 colonnes max)
- [ ] Navigation confortable
- [ ] Images/cards dimensionnées correctement

### Desktop (> 1024px)
- [ ] **Max-width 1200-1400px** : Contenu centré
- [ ] **Grids 3 colonnes** : Phase cards, For Who cards
- [ ] **Sidebar docs** : 280px largeur fixe
- [ ] **Navbar** : Horizontal, espacement généreux

---

## ♿ Accessibilité

### Navigation clavier
- [ ] **Tab** : Navigation séquentielle visible
- [ ] **Focus visible** : Outline bleu sur éléments focusés
- [ ] **Enter/Space** : Active liens et boutons
- [ ] **Escape** : (Non applicable - pas de modales)

### Sémantique HTML
- [ ] Headings hiérarchiques (H1 → H2 → H3)
- [ ] `<nav>` pour navigation
- [ ] `<main>` pour contenu principal
- [ ] `<footer>` pour footer
- [ ] `<aside>` pour sidebar docs

### ARIA & Labels
- [ ] Liens externes : `rel="noopener noreferrer"`
- [ ] LanguageSwitcher : `aria-label` présent
- [ ] Images : `alt` text descriptif (quand images ajoutées)

### Contrastes couleurs
- [ ] Texte noir sur fond blanc : ✅ WCAG AAA
- [ ] Texte blanc sur primary (#1A2332) : ✅ WCAG AA
- [ ] Liens bleu (#2E86AB) : ✅ WCAG AA

---

## 🎨 Design & Identité Visuelle

### Palette DocDriven
- [ ] **Primary** (#1A2332) : Headers, navbar, footer
- [ ] **Secondary** (#2E86AB) : Liens, accents, boutons
- [ ] **Neutral Light** (#F0F4F8) : Backgrounds cards
- [ ] **Accent Warning** (#D64933) : Challenge problem box

### Typography
- [ ] **Headings** : JetBrains Mono (Bold)
- [ ] **Body** : Inter (Regular, 16px)
- [ ] **Code** : JetBrains Mono (Regular)
- [ ] Fonts chargées depuis Google Fonts

### Composants clés
- [ ] Logo "DOC//DRIVEN" avec séparateur "//" coloré
- [ ] Buttons hover : Transform + shadow
- [ ] Cards hover : Border color + translateY
- [ ] Gradients : Hero, CTA sections

---

## 🌍 Bilingue (i18n)

### Détection langue
- [ ] Première visite : Détecte `navigator.language`
- [ ] Préférence stockée dans `localStorage`
- [ ] Pas de redirection en boucle

### LanguageSwitcher
- [ ] Affiche "EN" sur pages FR
- [ ] Affiche "FR" sur pages EN
- [ ] Redirige vers URL équivalente
- [ ] Préserve la page courante (ex: /intro → /en/intro)

### Contenu traduit
- [ ] Homepage : 5 sections FR et EN
- [ ] About : Bio complète FR et EN
- [ ] Navigation : Labels traduits
- [ ] Footer : Textes traduits
- [ ] Docs : Frontmatter `lang` correct

---

## 🔍 SEO & Meta Tags

### Meta tags de base
- [ ] `<title>` : Descriptif et unique par page
- [ ] `<meta name="description">` : 150-160 caractères
- [ ] `<meta name="viewport">` : Responsive
- [ ] `<html lang="fr">` ou `lang="en"` : Correct

### Open Graph (Facebook)
- [ ] `og:type` : website
- [ ] `og:url` : URL correcte
- [ ] `og:title` : Titre page
- [ ] `og:description` : Description page
- [ ] `og:image` : Image 1200x630px (placeholder pour l'instant)

### Twitter Card
- [ ] `twitter:card` : summary_large_image
- [ ] `twitter:title` : Titre page
- [ ] `twitter:description` : Description page
- [ ] `twitter:image` : Image partagée

---

## ⚡ Performance

### Lighthouse Audit
Tester avec Chrome DevTools → Lighthouse → Generate report (Desktop + Mobile)

#### Targets (Desktop)
- [ ] **Performance** : ≥ 98/100
- [ ] **Accessibility** : 100/100
- [ ] **Best Practices** : 100/100
- [ ] **SEO** : 100/100

#### Targets (Mobile)
- [ ] **Performance** : ≥ 95/100 (mobile plus strict)
- [ ] **Accessibility** : 100/100
- [ ] **Best Practices** : 100/100
- [ ] **SEO** : 100/100

### Core Web Vitals
- [ ] **LCP** (Largest Contentful Paint) : < 2.5s
- [ ] **FID** (First Input Delay) : < 100ms
- [ ] **CLS** (Cumulative Layout Shift) : < 0.1

### Optimisations appliquées
- [ ] Fonts preconnect (Google Fonts)
- [ ] `display=swap` sur fonts (évite FOIT)
- [ ] SSG pur (zero JavaScript côté client sauf detector)
- [ ] Bundle minimal (~195 KB total, ~61 KB gzip)

---

## 🧪 Tests Cross-Browser

### Browsers à tester
- [ ] **Chrome** (latest) : Windows + macOS
- [ ] **Firefox** (latest) : Windows + macOS
- [ ] **Safari** (latest) : macOS + iOS
- [ ] **Edge** (latest) : Windows
- [ ] **Chrome Mobile** : Android

### Vérifications par browser
- [ ] Layout identique (pas de différences majeures)
- [ ] Fonts chargées correctement
- [ ] Hover states fonctionnels (desktop)
- [ ] Touch targets ≥ 44x44px (mobile)
- [ ] Scroll smooth

---

## 🔐 Sécurité & Best Practices

### Liens externes
- [ ] Tous avec `target="_blank"`
- [ ] Tous avec `rel="noopener noreferrer"`

### Content Security
- [ ] Pas de `dangerouslySetInnerHTML` (React)
- [ ] Pas de `eval()` ou scripts inline non sécurisés

### HTTPS Ready
- [ ] Toutes les URLs relatives (pas de http:// hardcodé)
- [ ] Assets servis depuis `/public/` ou CDN

---

## ✅ Validation Finale

### Critères de succès V1.0 (DoD)
- [ ] **22 pages générées** sans erreurs
- [ ] **Homepage impeccable** : 5 sections, responsive, bilingue
- [ ] **Documentation accessible** : 9 docs FR + 9 EN avec sidebar
- [ ] **About page complète** : Bio, dissociation claire
- [ ] **Lighthouse ≥ 98/100** : Performance targets atteints
- [ ] **Bilingue fonctionnel** : FR/EN switch sans bugs
- [ ] **Mobile responsive** : Toutes pages testées
- [ ] **Zero erreurs console** : Chrome DevTools clean

### Blockers (à résoudre avant déploiement)
- [ ] Aucune erreur JavaScript console
- [ ] Aucun lien cassé (404)
- [ ] Aucune image manquante critique

### Nice-to-have (peut être reporté post-V1.0)
- ⚠️ Open Graph image 1200x630px (placeholder pour l'instant)
- ⚠️ Favicon multi-formats (ico, png 192x192, 512x512)
- ⚠️ Diagramme 6-phase interactif (US5 reporté)

---

## 🚀 Prêt pour Déploiement

Quand TOUS les critères ci-dessus sont validés :

```bash
# Build final
npm run build

# Vérifier dist/
ls -la dist/

# Déployer sur Vercel/Netlify
# (Configuration CI/CD selon hébergeur choisi)
```

---

**Date validation** : __________
**Validé par** : __________
**Statut** : ⬜ PASS / ⬜ FAIL (avec blockers listés)
