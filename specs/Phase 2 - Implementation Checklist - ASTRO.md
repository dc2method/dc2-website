# Checklist d'Implémentation DocDriven V1.0 - Astro 4.x
## Guide Opérationnel Développeur

**Version** : 2.0 - ASTRO
**Date** : 2026-01-07
**Statut** : READY FOR EXECUTION

---

## Instructions d'Utilisation

Cette checklist est conçue pour être suivie **séquentiellement** avec Astro 4.x. Chaque tâche inclut :
- **Checkbox** : Pour marquer la progression
- **Commandes Astro précises** : À exécuter dans terminal
- **Fichiers à modifier** : Chemins absolus exacts (structure Astro)
- **Points de validation** : Tests à effectuer après chaque groupe

**Convention** :
- 🔴 CRITIQUE : Doit absolument fonctionner avant de continuer
- 🟡 IMPORTANT : Valider avant de passer à la US suivante
- 🟢 VALIDATION : Point de contrôle qualité

**Structure Projet Astro** :
```
/home/eric/Projects/DocDriven/doc-driven_v1/
├── src/
│   ├── pages/              # Routes (index.astro, about.astro, [...slug].astro)
│   ├── content/            # Content Collections
│   │   ├── config.ts
│   │   └── docs/
│   │       ├── fr/         # Documents français
│   │       └── en/         # Documents anglais
│   ├── components/         # Astro + React components
│   ├── layouts/            # BaseLayout, DocsLayout, HomeLayout
│   ├── styles/             # CSS global
│   └── utils/              # Helper functions (i18n.ts)
├── public/                 # Assets statiques (images, fonts)
├── astro.config.mjs        # Configuration Astro
└── package.json
```

---

## Setup Initial

### Prérequis Environnement

- [ ] Node.js 20+ installé : `node --version` (doit afficher v20.x.x ou supérieur)
- [ ] npm à jour : `npm --version` (v10.x.x minimum)
- [ ] Git configuré : `git --version`
- [ ] Éditeur code prêt (VSCode recommandé avec extensions : Astro, ESLint, Prettier)

### Setup Projet Astro

- [ ] Naviguer vers dossier parent : `cd /home/eric/Projects/DocDriven`
- [ ] Sauvegarder ancien projet (si existant) : `mv doc-driven_v1 doc-driven_v1_backup_docusaurus`
- [ ] Initialiser nouveau projet Astro :
  ```bash
  npm create astro@latest doc-driven_v1 -- --template empty --typescript strict
  ```
- [ ] Naviguer vers projet : `cd doc-driven_v1`
- [ ] Créer branche implémentation : `git init && git checkout -b feature/v1.0-astro-implementation`
- [ ] 🔴 **VALIDATION** : Lancer dev server : `npm run dev` (doit ouvrir http://localhost:4321 sans erreurs)
- [ ] Vérifier build fonctionne : `npm run build` (doit réussir sans erreurs)

---

## US1 : Setup Astro + Configuration Socle

### T1.1 - Installer intégrations Astro nécessaires

- [ ] Installer intégration MDX :
  ```bash
  npx astro add mdx
  ```
- [ ] Installer intégration React :
  ```bash
  npx astro add react
  ```
- [ ] Installer Zod pour Content Collections (si pas installé) :
  ```bash
  npm install zod
  ```
- [ ] Sauvegarder : `git add . && git commit -m "US1-T1.1: Install Astro integrations (MDX, React, Zod)"`

### T1.2 - Configurer astro.config.mjs

- [ ] Ouvrir `/home/eric/Projects/DocDriven/doc-driven_v1/astro.config.mjs`
- [ ] Remplacer contenu par :
  ```javascript
  import { defineConfig } from 'astro/config';
  import mdx from '@astrojs/mdx';
  import react from '@astrojs/react';

  export default defineConfig({
    site: 'https://docdriven.dev',
    integrations: [
      mdx(),
      react(),
    ],
    build: {
      format: 'directory', // URLs propres sans .html
    },
    markdown: {
      shikiConfig: {
        theme: 'github-dark',
        wrap: true,
      },
    },
  });
  ```
- [ ] Sauvegarder : `git add astro.config.mjs && git commit -m "US1-T1.2: Configure astro.config.mjs for DocDriven"`

### T1.3 - Créer structure répertoires

- [ ] Créer structure :
  ```bash
  mkdir -p src/content/docs/fr src/content/docs/en
  mkdir -p src/layouts
  mkdir -p src/components/Homepage
  mkdir -p src/styles
  mkdir -p src/utils
  mkdir -p public/img
  ```
- [ ] Vérifier structure :
  ```bash
  ls -R src/
  ```
- [ ] Sauvegarder : `git add src/ public/ && git commit -m "US1-T1.3: Create DocDriven directory structure"`

### T1.4 - Configurer Content Collections

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/content/config.ts`
- [ ] Ajouter code :
  ```typescript
  import { defineCollection, z } from 'astro:content';

  const docsCollection = defineCollection({
    type: 'content',
    schema: z.object({
      title: z.string(),
      description: z.string().optional(),
      sidebar_position: z.number().optional(),
      lang: z.enum(['fr', 'en']),
    }),
  });

  export const collections = {
    'docs': docsCollection,
  };
  ```
- [ ] Sauvegarder : `git add src/content/config.ts && git commit -m "US1-T1.4: Configure Content Collections with Zod schema"`

### T1.5 - Créer BaseLayout

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/layouts/BaseLayout.astro`
- [ ] Ajouter code :
  ```astro
  ---
  interface Props {
    title: string;
    description?: string;
    lang?: 'fr' | 'en';
  }

  const {
    title,
    description = 'Structured LLM Development',
    lang = 'fr'
  } = Astro.props;
  ---

  <!DOCTYPE html>
  <html lang={lang}>
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width" />
      <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
      <meta name="generator" content={Astro.generator} />
      <meta name="description" content={description} />
      <title>{title}</title>
    </head>
    <body>
      <slot />
    </body>
  </html>
  ```
- [ ] Sauvegarder : `git add src/layouts/BaseLayout.astro && git commit -m "US1-T1.5: Create BaseLayout foundation"`

### T1.6 - Créer page index.astro temporaire

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/pages/index.astro`
- [ ] Ajouter code :
  ```astro
  ---
  import BaseLayout from '../layouts/BaseLayout.astro';
  ---

  <BaseLayout title="DocDriven - Structured LLM Development">
    <main style="padding: 2rem; max-width: 800px; margin: 0 auto;">
      <h1>DocDriven Website V1.0</h1>
      <p>Site en construction avec Astro 4.x</p>
      <p>Framework : Astro | Performance Target : 98-100 Lighthouse</p>
    </main>
  </BaseLayout>
  ```
- [ ] Sauvegarder : `git add src/pages/index.astro && git commit -m "US1-T1.6: Create temporary homepage"`

### 🟢 VALIDATION US1

- [ ] Lancer dev server : `npm run dev`
- [ ] Vérifier http://localhost:4321 affiche homepage temporaire
- [ ] Build production : `npm run build`
- [ ] Preview build : `npm run preview`
- [ ] Vérifier zéro erreurs console dans les deux modes
- [ ] **STOP si erreurs** : Debugger avant de continuer

---

## US2 : Support Bilingue i18n Astro

### T2.1 - Configurer routing i18n

- [ ] Ouvrir `/home/eric/Projects/DocDriven/doc-driven_v1/astro.config.mjs`
- [ ] Ajouter configuration i18n :
  ```javascript
  export default defineConfig({
    site: 'https://docdriven.dev',
    i18n: {
      defaultLocale: 'fr',
      locales: ['fr', 'en'],
      routing: {
        prefixDefaultLocale: false, // /fr/page devient /page
      },
    },
    integrations: [mdx(), react()],
    // ... reste config
  });
  ```
- [ ] Sauvegarder : `git add astro.config.mjs && git commit -m "US2-T2.1: Configure i18n routing"`

### T2.2 - Créer helper fonctions i18n

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/utils/i18n.ts`
- [ ] Ajouter code complet :
  ```typescript
  export function getLocale(url: URL): 'fr' | 'en' {
    const pathname = url.pathname;
    if (pathname.startsWith('/en/') || pathname === '/en') return 'en';
    return 'fr'; // default
  }

  export function getLocalizedPath(path: string, locale: 'fr' | 'en'): string {
    if (locale === 'fr') return path;
    return `/en${path}`;
  }

  export const translations = {
    fr: {
      'nav.methodology': 'Méthodologie',
      'nav.about': 'À Propos',
      'hero.tagline': 'Structured LLM Development',
      'hero.message': 'La méthodologie qui transforme les LLM de générateurs statistiques en outils de développement structurés, testés et maintenables.',
      'hero.cta.primary': 'Découvrir la Méthodologie →',
      'hero.cta.secondary': 'Voir les 6 Phases',
      'footer.methodology': 'Méthodologie',
      'footer.resources': 'Ressources',
    },
    en: {
      'nav.methodology': 'Methodology',
      'nav.about': 'About',
      'hero.tagline': 'Structured LLM Development',
      'hero.message': 'The methodology that transforms LLMs from statistical generators into structured, tested, and maintainable development tools.',
      'hero.cta.primary': 'Discover the Methodology →',
      'hero.cta.secondary': 'See the 6 Phases',
      'footer.methodology': 'Methodology',
      'footer.resources': 'Resources',
    },
  };

  export function t(key: string, locale: 'fr' | 'en'): string {
    return translations[locale][key] || key;
  }
  ```
- [ ] Sauvegarder : `git add src/utils/i18n.ts && git commit -m "US2-T2.2: Create i18n helper functions"`

### T2.3 - Créer composant LanguageSwitcher

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/components/LanguageSwitcher.astro`
- [ ] Ajouter code :
  ```astro
  ---
  import { getLocale, getLocalizedPath } from '../utils/i18n';

  const currentLocale = getLocale(Astro.url);
  const currentPath = Astro.url.pathname.replace(/^\/(en|fr)/, '') || '/';
  const otherLocale = currentLocale === 'fr' ? 'en' : 'fr';
  const otherPath = getLocalizedPath(currentPath, otherLocale);
  ---

  <div class="language-switcher">
    <a href={otherPath} aria-label={`Switch to ${otherLocale.toUpperCase()}`}>
      {otherLocale.toUpperCase()}
    </a>
  </div>

  <style>
    .language-switcher {
      display: inline-block;
    }

    .language-switcher a {
      padding: 0.5rem 1rem;
      text-decoration: none;
      font-weight: 600;
      color: white;
      background: var(--dd-secondary);
      border-radius: 4px;
      transition: background 0.2s;
    }

    .language-switcher a:hover {
      background: var(--dd-primary);
    }
  </style>
  ```
- [ ] Sauvegarder : `git add src/components/LanguageSwitcher.astro && git commit -m "US2-T2.3: Create LanguageSwitcher component"`

### T2.4 - Créer détecteur langue navigateur

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/components/LanguageDetector.astro`
- [ ] Ajouter code :
  ```astro
  ---
  // Composant vide côté serveur, script inline client
  ---

  <script is:inline>
    (function() {
      // Exécuter seulement sur page racine
      if (window.location.pathname !== '/' && !window.location.pathname.startsWith('/en')) return;

      const storedLang = localStorage.getItem('preferred-lang');
      if (storedLang) return; // Préférence déjà définie

      const browserLang = navigator.language.split('-')[0]; // 'fr-CA' -> 'fr'
      const currentPath = window.location.pathname;

      if (browserLang === 'en' && !currentPath.startsWith('/en')) {
        localStorage.setItem('preferred-lang', 'en');
        window.location.href = '/en' + currentPath;
      } else if (browserLang !== 'en' && currentPath.startsWith('/en')) {
        localStorage.setItem('preferred-lang', 'fr');
        window.location.href = currentPath.replace(/^\/en/, '');
      }
    })();
  </script>
  ```
- [ ] Intégrer dans BaseLayout :
  ```astro
  <head>
    <!-- ... autres meta tags ... -->
    <LanguageDetector />
  </head>
  ```
- [ ] Sauvegarder : `git add src/components/LanguageDetector.astro src/layouts/BaseLayout.astro && git commit -m "US2-T2.4: Add browser language detection"`

### 🟡 VALIDATION US2

- [ ] Lancer dev server : `npm run dev`
- [ ] Vérifier LanguageSwitcher visible (à intégrer dans navbar plus tard)
- [ ] Tester détection langue navigateur (changer langue Chrome Settings > Languages)
- [ ] Vérifier localStorage stocke préférence
- [ ] Zéro erreurs console
- [ ] **STOP si switch langue ne fonctionne pas**

---

## US3 : Content Collections + Migration Contenu

### T3.1 - Copier documents sources français

- [ ] Copier fichiers :
  ```bash
  cp /home/eric/Projects/DocDriven/doc-driven_v1_backup_docusaurus/documents-sources/francais/*.md \
     /home/eric/Projects/DocDriven/doc-driven_v1/src/content/docs/fr/
  ```
- [ ] Vérifier fichiers copiés :
  ```bash
  ls src/content/docs/fr/
  ```
- [ ] Devrait afficher : intro.md, phase1-architecture-strategique.md, etc.

### T3.2 - Ajouter frontmatter Astro aux documents français

- [ ] Pour CHAQUE fichier dans `src/content/docs/fr/`, ajouter frontmatter en haut :
  ```yaml
  ---
  title: "Introduction"  # Titre du document
  description: "Description courte"
  sidebar_position: 1  # Position dans sidebar (1, 2, 3, etc.)
  lang: fr
  ---
  ```
- [ ] Exemple `intro.md` :
  ```yaml
  ---
  title: "Introduction à DocDriven"
  description: "Maîtrisez le développement logiciel avec l'IA"
  sidebar_position: 1
  lang: fr
  ---
  ```
- [ ] Numéros sidebar_position :
  - intro.md : 1
  - phase1-architecture-strategique.md : 2
  - phase2-planification-tactique.md : 3
  - ... (continuer pour phases 3-6)
  - roles-et-responsabilites.md : 8

### T3.3 - Copier documents sources anglais

- [ ] Copier fichiers :
  ```bash
  cp /home/eric/Projects/DocDriven/doc-driven_v1_backup_docusaurus/documents-sources/english/*.md \
     /home/eric/Projects/DocDriven/doc-driven_v1/src/content/docs/en/
  ```
- [ ] Ajouter frontmatter avec `lang: en` à TOUS les fichiers anglais

### T3.4 - Créer page Licence

- [ ] Créer `/home/eric/Projects/DocDriven/doc-driven_v1/src/content/docs/fr/licence.md`
- [ ] Ajouter contenu complet avec frontmatter :
  ```markdown
  ---
  title: "Licence et Utilisation"
  description: "Licence Creative Commons CC BY-SA 4.0"
  sidebar_position: 9
  lang: fr
  ---

  # Licence et Utilisation

  ## Licence du Contenu

  Le contenu de la méthodologie DocDriven est publié sous licence
  **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

  ### Cela signifie que vous êtes libre de :

  - **Partager** : Copier et redistribuer le matériel
  - **Adapter** : Remixer, transformer et créer à partir du matériel
  - Pour toute utilisation, y compris commerciale

  ### Selon les conditions suivantes :

  - **Attribution** : Vous devez créditer Éric Gauthier comme auteur original
  - **Partage dans les mêmes conditions** : Les œuvres dérivées doivent
    utiliser la même licence CC BY-SA 4.0

  [Lire le texte complet de la licence](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)

  ## Questions

  Pour toute question, contactez Éric Gauthier via la [page À Propos](/about).
  ```
- [ ] Créer version anglaise : `src/content/docs/en/licence.md` (traduire)

### T3.5 - Créer DocsLayout avec sidebar

- [ ] Créer fichier `/home/eric/Projects/DocDriven/doc-driven_v1/src/layouts/DocsLayout.astro`
- [ ] Ajouter code complet (voir document Tactical Plan pour code détaillé)
- [ ] Inclut : Sidebar avec navigation, layout grid responsive

### T3.6 - Créer pages dynamiques [...slug].astro

- [ ] Créer `/home/eric/Projects/DocDriven/doc-driven_v1/src/pages/[...slug].astro` (français)
- [ ] Créer `/home/eric/Projects/DocDriven/doc-driven_v1/src/pages/en/[...slug].astro` (anglais)
- [ ] Code utilise `getCollection()` pour fetcher contenu et `DocsLayout`

### T3.7 - Ajuster chemins images

- [ ] Copier images vers `/home/eric/Projects/DocDriven/doc-driven_v1/public/img/`
- [ ] Vérifier syntaxe dans Markdown : `![Alt](/img/image.png)`
- [ ] Optimiser images >200KB : Compression, WebP

### 🟢 VALIDATION US3

- [ ] Build : `npm run build` (zéro erreurs schema Zod)
- [ ] Dev server : `npm run dev`
- [ ] Naviguer vers http://localhost:4321/intro
- [ ] Sidebar affiche tous documents
- [ ] Images chargent correctement
- [ ] Navigation entre pages fonctionne
- [ ] Version EN : http://localhost:4321/en/intro
- [ ] **STOP si erreurs Content Collections**

---

## US4 : Identité Visuelle DocDriven

### T4.1 - Créer global.css avec palette

- [ ] Créer `/home/eric/Projects/DocDriven/doc-driven_v1/src/styles/global.css`
- [ ] Ajouter code complet (voir Tactical Plan)
- [ ] Palette DocDriven, typography, reset CSS

### T4.2 - Importer global.css dans BaseLayout

- [ ] Modifier BaseLayout :
  ```astro
  <head>
    <!-- ... autres meta tags ... -->
    <link rel="stylesheet" href="/src/styles/global.css" />
  </head>
  ```

### T4.3 - Configurer Google Fonts

- [ ] Ajouter dans BaseLayout `<head>` :
  ```astro
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet" />
  ```

### T4.4 - Créer wordmark, logo, favicons

- [ ] Créer wordmark SVG : `public/img/docdriven-wordmark.svg`
- [ ] Créer logo navbar : `public/img/logo.svg`
- [ ] Générer favicons (realfavicongenerator.net) → `public/`

### T4.5 - Créer composants Navbar et Footer

- [ ] Créer `src/components/Navbar.astro` (voir Tactical Plan code complet)
- [ ] Créer `src/components/Footer.astro`
- [ ] Intégrer dans BaseLayout avant/après `<slot />`

### T4.6 - Créer Open Graph image

- [ ] Créer `public/img/docdriven-og.png` (1200x630px)
- [ ] Ajouter meta tags dans BaseLayout

### 🟡 VALIDATION US4

- [ ] Navbar et Footer visibles
- [ ] Palette DocDriven appliquée
- [ ] Fonts Google chargées (inspecter DevTools)
- [ ] Logo et favicons affichés

---

## US5, US6, US7, US8 : [Continuer selon même structure]

**Note** : La suite de la checklist suit le même pattern détaillé pour :
- US5 : Diagramme 6-Phase React Island (composant .tsx + client:visible)
- US6 : Homepage Astro (5 sections components)
- US7 : Page About
- US8 : Optimisations finales (Lighthouse 98-100)

---

## Suivi Progression

- [ ] US1 complétée (Setup Astro)
- [ ] US2 complétée (i18n)
- [ ] US3 complétée (Content Collections)
- [ ] US4 complétée (Identité visuelle)
- [ ] US5 complétée (Diagramme)
- [ ] US6 complétée (Homepage)
- [ ] US7 complétée (About)
- [ ] US8 complétée (Optimisations)

**VALIDATION FINALE** : Lighthouse audit 98-100/100, bundle <50KB, site bilingue fonctionnel.

---

**Fin de la Checklist d'Implémentation Astro**

**Prochaine Action** : Commencer par **Setup Initial** puis **US1 : Setup Astro + Configuration Socle**
