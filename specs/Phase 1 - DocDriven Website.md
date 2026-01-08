# Document d'Architecture Stratégique
## Projet : DocDriven Website V1.0
**Date** : 2026-01-07  
**Version** : 1.0 - DRAFT  
**Architecte** : Éric Gauthier  
**Contributeurs** : Équipe consultation (Claude, Sophie, Claire, Julien, Élodie, Sarah, Mathieu)  
**Statut** : EN RÉVISION - Prêt pour Phase 2

---

## Résumé Exécutif

### Contexte Stratégique

Éric Gauthier, architecte TI senior avec 30+ ans d'expérience, est en recherche d'emploi à 60 ans dans un marché âgiste. Il a développé **DocDriven**, une méthodologie structurée pour développement logiciel assisté par LLM, et souhaite publier un site web professionnel documentant cette méthodologie.

**Objectif Principal** : Créer un asset professionnel démontrant expertise différenciante en architecture et méthodologies IA, utilisable en entrevue et pitch de vente.

**Contrainte Critique** : Le site doit établir crédibilité professionnelle immédiate (≤30 secondes) auprès de CTOs/VPs Engineering évaluant le profil d'Éric, tout en positionnant DocDriven comme méthodologie plus grande que son créateur.

### Décision d'Architecture Recommandée

**Architecture Sélectionnée** : **"MVP de Qualité Professionnelle"**

- **Périmètre V1.0** : Homepage + Méthodologie Core + Identité Visuelle impeccable
- **Framework** : **Astro 4.x** (Islands Architecture, performance maximale)
- **Standard** : Excellence sur ce qui est présent, extensibilité pour V1.1+
- **Timeline** : **3.5 semaines** (réduit de 4 grâce à simplicité Astro)
- **Positionnement** : DocDriven = méthodologie open source, Éric = contributeur principal (pas gourou)

**Justification** : Cette architecture équilibre les trois contraintes simultanées (crédibilité professionnelle, dissociation auteur/méthode, timeline raisonnable) tout en permettant itération future sans refonte. **Astro choisi vs Docusaurus** pour homepage first-class, performance supérieure (Lighthouse 98-100), et maintenance solo simplifiée.

---

## 1. Définition du Problème

### 1.1 Problème Business

**Énoncé Principal** :  
Éric Gauthier doit se différencier sur un marché de l'emploi âgiste (60 ans) en démontrant une expertise unique et contemporaine en architecture de solutions et intelligence artificielle, que les développeurs plus jeunes ne possèdent pas.

**Symptômes** :
- Marché IT post-COVID favorise jeunes développeurs (coût moindre, perception "plus à jour")
- Compétences traditionnelles (30 ans d'expérience) insuffisantes sans preuve maîtrise IA
- CV/LinkedIn standards ne communiquent pas profondeur d'analyse architecturale
- Besoin d'un "proof point" tangible utilisable en entrevue/pitch

**Impact si Non-Résolu** :
- Éric perçu comme "expérimenté mais dépassé technologiquement"
- Allongement recherche emploi (6-12 mois au lieu de 3-6 mois)
- Acceptation d'opportunités sous-qualifiées (perte salaire/satisfaction)
- Impossibilité de valoriser pleinement 30 ans d'expertise

### 1.2 Problème Technique

**Énoncé** :  
Créer un site web professionnel qui :
1. Documente une méthodologie complexe (15K+ mots, 6 phases) de manière accessible
2. Établit crédibilité technique **sans case study client** disponible
3. Positionne méthode comme "plus grande que créateur" (éviter narcissisme)
4. Fonctionne comme vitrine professionnelle pour recherche emploi
5. Reste maintenable et extensible pour ajouts futurs (V1.1+)

**Contraintes Techniques** :
- Docusaurus comme plateforme (décision préalable)
- Hébergement statique (simplicité, coût)
- Performance web (temps chargement <2s)
- Responsive design (mobile/tablet/desktop)
- SEO optimisé ("structured LLM development", "AI methodology")

### 1.3 Contraintes & Limitations

**Contraintes Business** :
- ❌ Budget marketing : $0 (pas de pub payante)
- ❌ Case study client : Aucun disponible publiquement
- ❌ Communauté existante : Aucune (V1.0 = lancement)
- ✅ Preuve conceptuelle : Chef Jules (projet solo utilisable comme exemple)
- ✅ Documentation extensive : 15K+ mots, 26 ADRs

**Contraintes Temporelles** :
- Timeline souhaitée : 3-4 semaines maximum
- Pression emploi : Asset nécessaire MAINTENANT pour recherche active
- Qualité non-négociable : "Suffisamment bon" pour crédibilité pro = ~80% perfection

**Contraintes Organisationnelles** :
- Équipe : Solo (Éric + consultation Claude)
- Compétences design : Limitées (besoin de simplicité vs. sophistication)
- Maintenance future : Doit être gérable par Éric seul

**Contraintes Psychologiques** :
- Dissociation auteur/méthode obligatoire (intégrité intellectuelle d'Éric)
- Ton sobre requis (pas de hype marketing, authentique)
- Positionnement "contributeur" pas "gourou"

---

## 2. Options d'Architecture Évaluées

### Option A : "Site Produit Commercial"

**Description** :  
Site type SaaS startup avec landing page optimisée conversion, CTAs agressifs, pricing page, testimonials, démo vidéo.

**Approche Technique** :
- Framework marketing (Webflow, Framer)
- Design moderne/flashy (gradients, animations)
- Copy orienté conversion ("Transformez votre dev en 10x!")
- Funnel : Homepage → Signup → Onboarding

**Avantages** :
- ✅ Maximum d'impact visuel immédiat
- ✅ Templates existants (déploiement rapide)
- ✅ Optimisé pour acquisition utilisateurs

**Inconvénients** :
- ❌ Inauthentique (DocDriven ≠ produit commercial)
- ❌ Incompatible avec positionnement "open source communautaire"
- ❌ Crédibilité professionnelle compromise (semble amateur ou vendeur)
- ❌ Maintenance complexe (updates fréquentes nécessaires)

**Verdict** : ❌ **REJETÉ** - Misalignment complet avec contraintes business et valeurs d'Éric

---

### Option B : "Documentation Technique Pure"

**Description** :  
Site type documentation officielle (Read the Docs, GitBook style) sans homepage marketing, direct vers documentation méthodologique.

**Approche Technique** :
- Docusaurus configuration minimale
- Navigation sidebar gauche
- Contenu = documentation 6 phases
- Zéro design custom (thème default)

**Avantages** :
- ✅ Rapide à déployer (3-5 jours)
- ✅ Cohérent avec nature "méthodologie"
- ✅ Maintenabilité maximale
- ✅ Authentique (pas de faux-semblants)

**Inconvénients** :
- ❌ Zéro impact visuel pour recruteur arrivant homepage
- ❌ Ne communique pas sophistication/séniorité d'Éric
- ❌ Manque différenciation (ressemble à tout projet open source)
- ❌ Pas de "vitrine professionnelle" utilisable en portfolio

**Verdict** : ❌ **REJETÉ** - Insuffisant pour objectif crédibilité professionnelle

---

### Option C : "MVP de Qualité Professionnelle" ⭐

**Description** :  
Hybride entre vitrine professionnelle et documentation technique. Homepage soignée établissant crédibilité (30s), puis documentation extensive. Identité visuelle sobre mais distinctive. Architecture extensible pour V1.1+.

**Approche Technique** :
- Docusaurus avec homepage custom React
- Design sobre, codes visuels "documentation industrielle" (ISO/IEEE)
- 3 sections principales :
  1. Homepage (vitrine pro)
  2. Méthodologie (documentation 6 phases)
  3. À Propos (profil Éric séparé)
- Identité visuelle : Wordmark professionnel, diagramme 6-phase signature, palette technique

**Périmètre V1.0** :
- ✅ Homepage impeccable (5 sections)
- ✅ Méthodologie documentée (6 phases + exemples)
- ✅ Identité visuelle cohérente
- ✅ Page "À Propos de l'Auteur"
- ❌ ArchRAG template (V1.1)
- ❌ Case studies multiples (V1.1+)
- ❌ Communauté/Forum (V1.2+)
- ❌ Vidéos explicatives (V1.2+)

**Avantages** :
- ✅ Établit crédibilité en ≤30 secondes (recruteur)
- ✅ Démontre sophistication architecturale (diagramme 6-phase)
- ✅ Extensible sans refonte (architecture modulaire)
- ✅ Maintenable par Éric seul (Docusaurus standard)
- ✅ Authentique (tone sobre, pas marketing)
- ✅ Timeline réaliste (3-4 semaines qualité pro)

**Inconvénients** :
- ⚠️ Effort design initial significatif (wordmark, diagrammes)
- ⚠️ Nécessite validation itérative (3-4 rounds probable)
- ⚠️ Crédibilité sans case study = challenge communication

**Verdict** : ✅ **SÉLECTIONNÉ** - Meilleur équilibre contraintes/objectifs

---

### Option D : "Lancement Minimal + Itération Rapide"

**Description** :  
Lancer en 72h avec homepage ultra-minimaliste + lien doc, puis itérer publiquement selon feedback.

**Approche Technique** :
- Homepage 3 paragraphes + CTA doc
- Docusaurus thème default
- Itérations hebdomadaires basées usage

**Avantages** :
- ✅ Publication immédiate (72h)
- ✅ Feedback réel utilisateurs
- ✅ Apprentissage itératif

**Inconvénients** :
- ❌ Première impression médiocre non-récupérable
- ❌ Crédibilité professionnelle compromise (semble bâclé)
- ❌ Effort total supérieur (refonte après feedback)
- ❌ Incompatible avec usage portfolio emploi

**Verdict** : ❌ **REJETÉ** - Risque réputationnel trop élevé pour contexte recherche emploi

---

## 3. Analyse Comparative des Options

### Tableau de Décision

| Critère | Poids | Option A (Produit) | Option B (Doc Pure) | Option C (MVP Qualité) ⭐ | Option D (Minimal) |
|---------|-------|-------------------|-------------------|------------------------|-------------------|
| **Crédibilité Pro Immédiate** | 10 | 3/10 (commercial) | 5/10 (neutre) | **9/10** (sophistiqué) | 4/10 (amateur) |
| **Alignement Valeurs Éric** | 9 | 2/10 (vente) | 9/10 (authentique) | **9/10** (équilibré) | 8/10 (honnête) |
| **Timeline Réaliste** | 8 | 7/10 (templates) | 10/10 (rapide) | **7/10** (3-4 sem) | 10/10 (72h) |
| **Maintenabilité Long-Terme** | 7 | 4/10 (complexe) | 10/10 (simple) | **8/10** (Docusaurus) | 6/10 (refonte) |
| **Extensibilité V1.1+** | 8 | 5/10 (locked) | 9/10 (flexible) | **10/10** (modulaire) | 7/10 (rebuild) |
| **Impact Visuel Recruteur** | 9 | 8/10 (flashy) | 3/10 (neutre) | **9/10** (sobre élégant) | 2/10 (basique) |
| **Coût Total Possession** | 6 | 6/10 (hosting) | 10/10 (statique) | **9/10** (statique) | 9/10 (statique) |
| **Risque Réputationnel** | 10 | 8/10 (hype) | 3/10 (oubliable) | **2/10** (professionnel) | 7/10 (bâclé) |
| **TOTAL PONDÉRÉ** | - | **314/670** | **505/670** | **🏆 598/670** | **461/670** |

### Justification Décision Finale

**Option C (MVP de Qualité Professionnelle)** obtient le score le plus élevé (598/670) car elle :

1. **Maximise Crédibilité** : Homepage soignée + diagramme sophistiqué = perception "senior expert" en 30s
2. **Respecte Valeurs** : Authentique, pas commercial, dissociation auteur/méthode
3. **Timeline Acceptable** : 3-4 semaines = pression raisonnable, qualité garantie
4. **Extensible** : Architecture permet V1.1 (ArchRAG), V1.2 (communauté) sans refonte
5. **Risque Minimal** : Professionnalisme = pas de damage réputationnel si non-adopté massivement

**Trade-offs Acceptés** :
- ✅ Effort design initial supérieur (mais ROI = crédibilité durable)
- ✅ Timeline 3-4 semaines vs 72h (mais "première impression" non-récupérable)
- ✅ Pas de case study client (mais crédibilité via documentation + exemple Chef Jules)

---

## 4. Architecture de Solution Recommandée

### 4.1 Vision d'Ensemble

**DocDriven Website = Carte de Visite Professionnelle Interactive**

**Métaphore Directrice** : "Documentation Industrielle Vivante"  
Pas un produit SaaS. Pas un blog personnel. Une **spécification technique publiée** comme IEEE ou ISO publierait un standard, mais interactive et accessible.

**Principes Architecturaux** :

1. **Clarté Immédiate** : Recruteur comprend valeur en ≤30 secondes
2. **Profondeur Progressive** : Homepage → Méthodologie → ADRs (du général au détail)
3. **Sobriété Visuelle** : Design industriel sobre, pas startup flashy
4. **Modularité** : Chaque section = module indépendant, extensible
5. **Maintenabilité Solo** : Éric peut maintenir sans équipe technique

### 4.2 Structure du Site (Information Architecture)

```
docdriven.dev/
│
├─ 📄 Homepage (/)                          [ASTRO CUSTOM]
│   ├─ Hero Section
│   ├─ Le Défi (Pourquoi Structure?)
│   ├─ Architecture DocDriven (Diagramme 6-Phase React)
│   ├─ Crédibilité (Sans Case Study)
│   ├─ Pour Qui? (Auto-qualification)
│   └─ Next Steps (CTAs)
│
├─ 📚 Méthodologie (/docs/)                 [ASTRO CONTENT COLLECTIONS]
│   ├─ Introduction
│   ├─ Phase 1: Strategic Architecture
│   ├─ Phase 2: Tactical Planning
│   ├─ Phase 3: TDD RED
│   ├─ Phase 4: TDD GREEN
│   ├─ Phase 5: TDD REFACTOR
│   ├─ Phase 6: Triple Inspection
│   ├─ Adoption Roadmap
│   ├─ Scaling Guidelines
│   └─ Comparaison Méthodologies
│
├─ 🏗️ Architecture (/architecture/)        [ASTRO CONTENT COLLECTIONS]
│   ├─ ADRs (26 décisions documentées)
│   ├─ Frameworks d'Évaluation (PSC, Fagan)
│   ├─ Indirect Benefits Analysis
│   └─ Enterprise Concerns
│
├─ 👤 À Propos (/about/)                    [ASTRO PAGE]
│   ├─ Éric Gauthier (Bio)
│   ├─ Contexte Création DocDriven
│   ├─ CV + LinkedIn
│   └─ Contact
│
└─ 🔮 Roadmap (V1.1+)                       [FUTURE]
    ├─ ArchRAG Template
    ├─ Case Studies
    ├─ Communauté
    └─ Contributions
```

**Avantages Architecture Astro** :
- ✅ **Homepage** : Page Astro full custom, design freedom totale
- ✅ **Docs** : Content Collections = Markdown simple, type-safe
- ✅ **Performance** : Static HTML partout sauf diagramme interactif
- ✅ **Maintenance** : Structure fichiers intuitive, pas de config complexe
- ✅ **SEO** : Chaque page = route, sitemap auto-généré

### 4.3 Architecture Technique (Stack)

**Framework Core** :
- **Astro 4.x** : Framework principal, Islands Architecture
- **React 18+** : Composants interactifs uniquement (diagramme 6-phase)
- **TypeScript** : Type safety, meilleure DX
- **Tailwind CSS** : Utility-first styling (optionnel, alternatives : vanilla CSS modules)

**Structure Projet Astro** :
```
docdriven-website/
├── src/
│   ├── pages/
│   │   ├── index.astro                    # Homepage (custom layout)
│   │   ├── about.astro                    # À Propos Éric
│   │   └── docs/
│   │       ├── [...slug].astro            # Route dynamique docs
│   │       └── index.astro                # Docs homepage
│   ├── content/
│   │   ├── config.ts                      # Content collections schema
│   │   └── docs/                          # Markdown files
│   │       ├── methodology/
│   │       │   ├── phase-1.md
│   │       │   ├── phase-2.md
│   │       │   └── ...
│   │       └── architecture/
│   │           ├── adr-001.md
│   │           └── ...
│   ├── components/
│   │   ├── DiagramSixPhase.tsx           # React (interactif)
│   │   ├── Hero.astro
│   │   ├── Navigation.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   ├── BaseLayout.astro              # Layout de base
│   │   ├── HomeLayout.astro              # Layout homepage
│   │   └── DocsLayout.astro              # Layout docs
│   └── styles/
│       ├── global.css
│       └── variables.css
├── public/
│   ├── fonts/
│   ├── images/
│   └── favicon.svg
└── astro.config.mjs                       # Config Astro
```

**Content Collections (Astro Native)** :
```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const docsCollection = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    phase: z.number().optional(),
    order: z.number(),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'docs': docsCollection,
};
```

**Composant Interactif Exemple** :
```tsx
// src/components/DiagramSixPhase.tsx
import { useState } from 'react';

interface Phase {
  id: number;
  name: string;
  humanPercent: number;
  llmPercent: number;
  color: string;
}

export default function DiagramSixPhase() {
  const [activePhase, setActivePhase] = useState<number | null>(null);
  
  const phases: Phase[] = [
    { id: 1, name: "Strategic Architecture", humanPercent: 60, llmPercent: 40, color: "#2E86AB" },
    // ... autres phases
  ];
  
  return (
    <div className="diagram-container">
      {phases.map(phase => (
        <PhaseBlock 
          key={phase.id}
          phase={phase}
          isActive={activePhase === phase.id}
          onHover={() => setActivePhase(phase.id)}
        />
      ))}
    </div>
  );
}
```

**Page Homepage Exemple** :
```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import Hero from '../components/Hero.astro';
import DiagramSixPhase from '../components/DiagramSixPhase';
---

<BaseLayout title="DocDriven - Structured LLM Development">
  <Hero />
  
  <section class="challenge">
    <h2>Pourquoi une Méthodologie Structurée?</h2>
    <p>Les Large Language Models ont démontré...</p>
  </section>
  
  <section class="architecture">
    <h2>Une Méthodologie en 6 Phases</h2>
    <DiagramSixPhase client:visible />
    <!-- client:visible = hydrate seulement quand visible viewport -->
  </section>
  
  <!-- Autres sections... -->
</BaseLayout>
```

**Hébergement & Déploiement** :
- **Hosting** : Vercel (gratuit, optimisé Astro) ou Netlify
- **CI/CD** : GitHub Actions auto-détecte Astro
- **Build Command** : `npm run build` (génère `/dist` statique)
- **Domaine** : docdriven.dev
- **SSL** : Let's Encrypt automatique

**Performance Targets (Astro Optimisé)** :
- Lighthouse Score : **98-100/100** (Performance, Accessibility, SEO, Best Practices)
- First Contentful Paint : **<1s** (vs <1.5s Docusaurus)
- Time to Interactive : **<2s** (vs <3s Docusaurus)
- Bundle size : **~50kb initial** (vs ~300kb Docusaurus)
- Core Web Vitals : Tous VERTS (LCP <2.5s, FID <100ms, CLS <0.1)

**SEO & Discoverability** :
```typescript
// astro.config.mjs
export default defineConfig({
  site: 'https://docdriven.dev',
  integrations: [
    sitemap(),           // Génère sitemap.xml automatique
    react(),             // Support React components
  ],
  markdown: {
    shikiConfig: {
      theme: 'dracula',  // Syntax highlighting code blocks
    },
  },
});
```

**Meta Tags (Layout Base)** :
```astro
---
// src/layouts/BaseLayout.astro
const { title, description } = Astro.props;
---
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>{title}</title>
    <meta name="description" content={description} />
    
    <!-- Open Graph -->
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://docdriven.dev" />
    
    <!-- Schema.org -->
    <script type="application/ld+json">
      {JSON.stringify({
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": title,
        "description": description,
        // ...
      })}
    </script>
  </head>
  <body>
    <slot />
  </body>
</html>
```

**Avantages Astro pour Votre Cas** :
1. **Islands Architecture** : JavaScript charge seulement pour diagramme interactif, reste static HTML
2. **Content Collections** : Type-safe Markdown, validation schema, excellent DX
3. **Zero-Config** : Fonctionne out-of-the-box, pas configuration complexe
4. **Multi-Framework** : React pour interactivité, Astro pur pour reste (optimal)
5. **Performance Native** : Optimisations automatiques (image optimization, code splitting, etc.)

### 4.4 Identité Visuelle (Design System)

**Palette Couleurs** :
```css
--primary: #1A2332;        /* Bleu-gris foncé - Autorité */
--secondary: #2E86AB;      /* Bleu industriel - Confiance */
--accent-positive: #06A77D; /* Vert technique - Validation */
--accent-warning: #D64933;  /* Rouge technique - Garde-fous */
--neutral-light: #F0F4F8;   /* Gris bleuté - Backgrounds */
--neutral-dark: #2C3E50;    /* Gris ardoise - Texte */
--code-bg: #282C34;         /* Background code blocks */
```

**Typographie** :
- **Headings** : JetBrains Mono Bold (16-48px)
- **Body** : Inter Regular (16px / 1.6 line-height)
- **Code** : JetBrains Mono Regular (14px)
- **Emphasis** : Inter SemiBold (pas italic, trop élégant)

**Wordmark** :
```
╔════════════════════════════════╗
║  DOC//DRIVEN                   ║
║  STRUCTURED LLM DEVELOPMENT    ║
╚════════════════════════════════╝
```
- Séparateur `//` (référence code comment)
- All-caps pour wordmark
- Small-caps pour tagline

**Composants Signature** :

1. **Diagramme 6-Phase** (élément visuel central)
   - Format : Pipeline horizontal, 6 blocs colorés
   - Annotations : % humain/LLM par phase
   - Interactions : Hover révèle détails (tooltips)
   - Versions : Full (homepage), Simplified (favicon)

2. **Cards "Pour Qui"** (auto-qualification)
   - 3 profils : Organisations / Architectes / R&D
   - Iconographie technique (pas illustrations fantaisistes)
   - Bordure accent selon profil

3. **Badges Crédibilité** (métriques sans case study)
   - "15K+ mots documentés"
   - "26 ADRs architecturaux"
   - "Fagan 85/100"
   - "0 régression sur 840 tests"

### 4.5 Contenu Clé (Copy Strategy)

**Ton de Voix** :
- **Sobre** : Pas de hype ("révolutionnaire", "disruptif"), vocabulaire technique précis
- **Confiant** : Affirmations directes ("DocDriven résout ce problème"), pas hésitant
- **Éducatif** : Explique concepts, pas seulement vend bénéfices
- **Authentique** : Reconnaît limites (V1.0 sans case study), honnête sur périmètre

**Messages Clés (Homepage)** :

**Hero** :
*"La méthodologie qui transforme les LLM de générateurs statistiques en outils de développement structurés, testés et maintenables."*

**Section Défi** :
*"Les Large Language Models ont démontré des capacités remarquables en génération de code. Cependant, leur adoption en environnement professionnel révèle une limite critique : sans cadre méthodologique rigoureux, ils génèrent du code syntaxiquement correct mais architecturalement fragile, créant une dette technique invisible qui ne se manifeste que des mois plus tard."*

**Section Architecture** :
*"DocDriven structure l'adoption des LLM à travers 6 phases où les humains contrôlent les décisions stratégiques et architecturales, tandis que l'IA accélère l'exécution tactique sous supervision continue."*

**Section Crédibilité** :
*"DocDriven n'est pas une théorie – c'est une méthodologie opérationnelle développée et testée sur un projet de traitement de données complexe, avec génération automatique de tests, refactoring guidé et inspection systématique."*

---

## 5. Stratégie d'Implémentation

### 5.1 Roadmap de Livraison

**Phase 1 : Fondations (Semaine 1)** - 4 jours (réduit de 5)
- [x] Architecture stratégique documentée (ce document)
- [ ] Validation structure avec Éric
- [ ] Wireframes homepage (basse-fidélité)
- [ ] **Setup projet Astro** (1-2h vs 1j Docusaurus)
- [ ] Configuration domaine docdriven.dev
- [ ] Content Collections schema défini

**Phase 2 : Contenu (Semaine 2)** - 7 jours
- [ ] Rédaction finale homepage (5 sections)
- [ ] Migration documentation méthodologie (Markdown pur)
- [ ] Rédaction page "À Propos"
- [ ] Révision ton de voix (Julien)
- [ ] Validation ensemble contenu
- [ ] Organisation fichiers content/docs/

**Phase 3 : Design (Semaine 3)** - 7 jours
- [ ] Création wordmark DOC//DRIVEN
- [ ] Design diagramme 6-phase (SVG + React)
- [ ] **Layouts Astro** (BaseLayout, HomeLayout, DocsLayout)
- [ ] Styles CSS (variables, typography)
- [ ] Components Astro (Hero, Navigation, Footer)
- [ ] Composant React DiagramSixPhase

**Phase 4 : Intégration (Semaine 4)** - 5 jours
- [ ] Homepage complète (Astro + React islands)
- [ ] Pages docs dynamiques ([...slug].astro)
- [ ] Navigation optimisée
- [ ] Responsive design (mobile/tablet)
- [ ] **Performance optimization** (image optimization, lazy loading)
- [ ] SEO meta tags

**Phase 5 : QA & Publication** - 3 jours
- [ ] Testing cross-browser
- [ ] **Lighthouse audit (target: 98-100)**
- [ ] Validation finale Éric
- [ ] Déploiement Vercel production
- [ ] **🚀 LIVE**

**Timeline Totale** : 26 jours (~3.5 semaines, réduit de 4 semaines grâce à Astro)

### 5.2 Critères de Succès V1.0

**Critères Techniques** :
- ✅ Lighthouse Performance Score >90
- ✅ Time to Interactive <3s
- ✅ Mobile-responsive (test iPhone, Android, iPad)
- ✅ Cross-browser (Chrome, Firefox, Safari, Edge)
- ✅ SEO meta tags complets

**Critères Business** :
- ✅ Recruteur comprend valeur en ≤30s (test utilisateur)
- ✅ Crédibilité professionnelle établie (feedback 3 personnes externes)
- ✅ Dissociation auteur/méthode claire (section séparée)
- ✅ Utilisable en pitch emploi (Éric valide)

**Critères Qualité** :
- ✅ Zéro typo dans homepage/méthodologie core
- ✅ Identité visuelle cohérente (palette appliquée partout)
- ✅ Diagramme 6-phase qualité publication
- ✅ Documentation structurée (navigation claire)

### 5.3 Plan de Migration V1.0 → V1.1+

**V1.1 (3-4 semaines post-launch)** :
- [ ] ArchRAG template téléchargeable
- [ ] Section "Exemples Concrets" (Chef Jules détaillé)
- [ ] Page "Comparaison Méthodologies" (vs Agile, TDD-only, etc.)

**V1.2 (2-3 mois post-launch)** :
- [ ] GitHub Discussions activé (communauté)
- [ ] Contribution guidelines
- [ ] Premier case study externe (si adoption)

**V1.3+ (6+ mois)** :
- [ ] Vidéos explicatives (YouTube)
- [ ] Templates additionnels (ADR, tactical plans)
- [ ] Plugin VS Code (si demande communauté)

---

## 6. Analyse de Risques

### 6.1 Risques Techniques

**Risque T1 : Diagramme 6-Phase Trop Complexe Visuellement**
- **Probabilité** : Moyenne (40%)
- **Impact** : Élevé (confusion recruteur = perte crédibilité)
- **Mitigation** : Créer 2 versions (Simplified + Detailed), tester avec 3 personnes externes
- **Plan B** : Version statique PNG haute-résolution si interactivité complexe

**Risque T2 : Performance Homepage (Bundle Size)**
- **Probabilité** : Moyenne (30%)
- **Impact** : Moyen (temps chargement >3s = frustration)
- **Mitigation** : Code splitting React, lazy loading images, CDN fonts
- **Plan B** : Version statique HTML si React trop lourd

**Risque T3 : Docusaurus Version Breaking Changes**
- **Probabilité** : Faible (10%)
- **Impact** : Élevé (rebuild complet)
- **Mitigation** : Pin version Docusaurus, changelog monitoring
- **Plan B** : Fork Docusaurus version stable

### 6.2 Risques Business

**Risque B1 : Crédibilité Sans Case Study Insuffisante**
- **Probabilité** : Moyenne (35%)
- **Impact** : Élevé (échec objectif principal)
- **Mitigation** : 
  - Détailler exemple Chef Jules (840 tests, 0 régression, Fagan 85)
  - Emphase documentation extensive (15K mots, 26 ADRs)
  - Badges métriques visibles homepage
- **Plan B** : V1.1 ajouter case study anonymisé ou persona fictif réaliste

**Risque B2 : Perception "Trop Théorique" (Pas Assez Pratique)**
- **Probabilité** : Moyenne (40%)
- **Impact** : Moyen (adoption lente, peu de viralité)
- **Mitigation** :
  - Section "Pour Qui" avec situations concrètes
  - Exemples code dans chaque phase méthodologie
  - ArchRAG template V1.1 (proof pratique)
- **Plan B** : Créer série blog posts "DocDriven Applied" (cas pratiques)

**Risque B3 : Marché en Phase Désillusion IA (Timing Mauvais)**
- **Probabilité** : Moyenne (30%)
- **Impact** : Moyen (peu d'intérêt immédiat)
- **Mitigation** :
  - Messaging empathique "vous avez raison d'être déçus"
  - Adresse directement échecs LLM ad-hoc
  - Positionnement "solution aux problèmes connus"
- **Plan B** : Pivot messaging vers "best practices futures" (pour quand marché remonte)

### 6.3 Risques Organisationnels

**Risque O1 : Éric Trouve Emploi Avant Fin V1.0**
- **Probabilité** : Faible (20%)
- **Impact** : Faible (pause projet, reprise ultérieure)
- **Mitigation** : Architecture modulaire permet pause/reprise sans perte
- **Plan B** : Publier V0.9 "beta" rapidement si emploi imminent

**Risque O2 : Sur-Engineering (Perfectionnisme Bloquant)**
- **Probabilité** : Moyenne (35%)
- **Impact** : Moyen (timeline dépassée, énergie gaspillée)
- **Mitigation** :
  - Critères succès ÉCRITS (↑ Section 5.2)
  - Review gates chaque semaine (GO/STOP décision)
  - Mantra "80% excellent > 100% parfait jamais publié"
- **Plan B** : Timebox strict 4 semaines, publier état actuel si dépassement

**Risque O3 : Feedback Négatif Post-Launch (Ego Bruised)**
- **Probabilité** : Moyenne (30%)
- **Impact** : Faible (psychologique seulement)
- **Mitigation** :
  - Positionnement "V1.0 - Work in Progress"
  - GitHub Discussions pour canaliser critiques constructives
  - Rappel : Feedback = données pour V1.1
- **Plan B** : Pause communications 48h si critique dure, puis répondre factuellement

---

## 7. Considérations Stratégiques Long-Terme

### 7.1 Utilisation en Recherche d'Emploi

**Scénario A : En Entrevue Technique**

**Recruteur** : "Parlez-moi d'un projet récent démontrant votre expertise en architecture..."

**Éric** (pitch 60 secondes) :
*"J'ai développé DocDriven, une méthodologie structurée pour développement logiciel assisté par LLM. Le constat : l'adoption ad-hoc des LLM génère dette technique invisible. J'ai structuré une approche 6-phase où humains contrôlent stratégie/architecture, IA accélère tactique sous supervision. Documenté 15,000+ mots, 26 ADRs, testé sur projet complexe atteignant Fagan 85/100 avec zéro régression. **La méthodologie complète est sur docdriven.dev** si vous voulez voir mon approche architecturale en profondeur."*

**Impact Souhaité** :
- ✅ Démontre capacité identifier problème industriel réel
- ✅ Montre structuration méthodologique (rare chez dev)
- ✅ Preuve maîtrise IA avancée (différenciateur vs jeunes)
- ✅ Expertise consultable = crédibilité vérifiable

**Scénario B : Sur CV/LinkedIn**

**Section Projets** :
```
DocDriven - Structured LLM Development Methodology
Créateur & Architecte Principal | 2024-2025

Méthodologie open source structurant l'adoption des LLM 
en développement logiciel professionnel. Architecture 
6-phase équilibrant décisions humaines et accélération 
IA, avec mécanismes validation continue (TDD, Triple 
Inspection).

• Documentation : 15K+ mots, 26 ADRs
• Validation : Projet complexe, Fagan 85/100, 0 régression
• Impact : Framework opérationnel organisations

🔗 docdriven.dev
```

**Scénario C : En Négociation Salaire**

**Argument de Valeur** :
*"Au-delà de mon expertise technique traditionnelle, j'apporte une compréhension structurée de l'intégration IA en environnement professionnel – un asset stratégique pour toute organisation adoptant ou planifiant adopter les LLM. DocDriven documente cette expertise de manière transférable à vos équipes."*

### 7.2 Évolution Marché IA (2025-2027)

**Hypothèse Optimiste : Marché Remonte**
- LLM tools (Copilot, Cursor, etc.) deviennent standards
- Organisations cherchent méthodologies éprouvées
- DocDriven positionnée comme "early mover" crédible
- **Action V1.2** : Capitaliser momentum, case studies, communauté

**Hypothèse Pessimiste : Désillusion Prolongée**
- Adoption LLM ralentit, retour méthodes traditionnelles
- DocDriven perçue "solution à problème inexistant"
- **Action** : Pivot messaging "best practices futures", garder doc vivante

**Hypothèse Neutre : Segmentation Marché**
- Adoption LLM mature chez early adopters seulement
- Majorité sceptique attend preuves
- **Action V1.1** : Focus case studies crédibles, ROI documenté

**Position Éric** : Indépendant de l'adoption marché.
DocDriven = démonstration expertise personnelle (objectif atteint dès V1.0 live). Adoption large = bonus, pas requis pour succès personnel.

### 7.3 Propriété Intellectuelle & Licensing

**Décision Licensing** : Creative Commons BY-SA 4.0

**Justification** :
- ✅ Open source = aligné valeurs Éric
- ✅ BY (Attribution) = crédibilité préservée
- ✅ SA (Share-Alike) = empêche commercialisation fermée
- ❌ Pas GPL (trop restrictif pour méthodologie)
- ❌ Pas MIT/Apache (trop permissif, perd attribution)

**Implications** :
- Tout le monde peut utiliser/modifier DocDriven
- MAIS doit créditer Éric Gauthier comme auteur original
- MAIS dérivés doivent rester CC BY-SA 4.0
- Commercialisation possible SI attribution maintenue

**Protection Réputation** :
- Trademark "DocDriven" (optionnel, coût ~$300 CAD)
- GitHub comme preuve antériorité (timestamp)
- Copyright notice footer site web

---

## 8. Métriques de Succès & KPIs

### 8.1 Métriques Immédiates (Post-Launch J+30)

**Performance Technique** (Astro Optimisé) :
- **Lighthouse Performance** : **98-100/100** (vs 90+ Docusaurus)
- **Lighthouse Accessibility** : 100/100
- **Lighthouse SEO** : 100/100
- **Lighthouse Best Practices** : 100/100
- **First Contentful Paint** : <1s (vs <1.5s Docusaurus)
- **Time to Interactive** : <2s (vs <3s Docusaurus)
- **Largest Contentful Paint** : <2.5s (Core Web Vitals)
- **Cumulative Layout Shift** : <0.1 (Core Web Vitals)
- **Bundle Size Initial** : ~50kb (vs ~300kb Docusaurus)

**Trafic & Engagement** :
- Visites uniques : >100 (objectif modeste, pas viralité)
- Temps moyen session : >3 minutes (engagement profondeur)
- Bounce rate : <60% (homepage retient attention)
- Pages/session : >2.5 (navigation vers méthodologie)

**Conversion Objectif Personnel** :
- ✅ Éric mentionne DocDriven en 3+ entrevues
- ✅ 2+ recruteurs visitent site après mention CV
- ✅ 1+ feedback positif spontané (LinkedIn, email)
- ✅ "Lighthouse 100" mentionné en entrevue technique (signal compétence)

**Uptime & Reliability** :
- Uptime : >99.9% (Vercel SLA)
- Global CDN : <100ms TTFB toutes régions

### 8.2 Métriques Moyen-Terme (3-6 Mois)

**Adoption Organique** :
- Backlinks : >5 (articles/blogs mentionnant DocDriven)
- GitHub stars : >20 (si repo public)
- LinkedIn mentions : >10 (partages/discussions)

**Impact Professionnel Éric** :
- ✅ Emploi trouvé (objectif primaire)
- ✅ Rôle incorpore expertise IA (validation positioning)
- ✅ Salaire reflète séniorité (DocDriven comme proof point)

**Validation Méthodologie** :
- 1+ organisation teste DocDriven (même informellement)
- 3+ développeurs donnent feedback constructif
- 1+ contribution externe (GitHub issue/PR/discussion)

### 8.3 Métriques Long-Terme (6-12 Mois)

**Établissement Standard** (aspirationnel) :
- Citée dans articles/conférences IA dev
- Comparée autres méthodologies (TDD, Agile+AI)
- Incluse dans curriculum formation IA

**Communauté** (si marché réceptif) :
- GitHub Discussions actives (>20 threads)
- Contributors externes (>3 personnes)
- Forks/adaptations documentées (>5)

---

## 9. Décisions Architecturales (ADRs Clés)

### ADR-001 : Choix de Astro vs. Alternatives

**Contexte** : Besoin plateforme optimale pour site hybride (homepage marketing professionnelle + documentation technique) avec performance maximale et maintenance solo.

**Options Évaluées** :
- **Astro 4.x** (Islands architecture, content-focused, multi-framework)
- Docusaurus 3.x (React, SSG docs-first, Meta-backed)
- Next.js 14+ (React full-stack, très flexible)
- VitePress (Vue.js, Vite-powered, lightweight)
- Custom solution (flexibilité totale, effort maximum)

**Décision** : **Astro 4.x**

**Justification Technique** :
- ✅ **Homepage = First-Class** : Pas un hack dans architecture docs, design freedom totale
- ✅ **Performance exceptionnelle** : ~50kb bundle vs ~300kb Docusaurus (6x plus léger)
- ✅ **Islands Architecture** : JavaScript seulement où nécessaire (diagramme interactif)
- ✅ **Markdown natif** : Content collections simple, pas MDX complexe obligatoire
- ✅ **Multi-framework** : React pour diagramme 6-phase, reste en Astro pur
- ✅ **SEO optimal** : SSG + meta tags automatiques + sitemap
- ✅ **DX excellent** : Hot reload rapide, TypeScript native, courbe apprentissage douce
- ✅ **Moderne (2026)** : Tendance actuelle, signal "à jour technologiquement"

**Justification Business** :
- ✅ **Lighthouse 100 facile** : Performance = signal professionnalisme pour recruteurs
- ✅ **Maintenance solo simple** : Architecture claire, Éric peut gérer seul
- ✅ **Timeline optimisée** : Setup from scratch 1-2j vs 2-3j frameworks alternatifs
- ✅ **Crédibilité tech 2026** : "Built with Astro" = compétence frameworks modernes
- ✅ **Différenciation** : Rares sites DocDriven-quality avec Astro = signal innovation

**Comparaison Docusaurus** :
| Critère | Docusaurus | Astro ✅ |
|---------|------------|----------|
| Homepage Custom | Possible mais friction | First-class citizen |
| Bundle Size | ~300kb | ~50kb (6x léger) |
| Docs Simples | Excellent | Excellent |
| Performance | Bon (90-95) | Exceptionnel (98-100) |
| Maintenance Solo | Faisable | Facile |
| Modernité 2026 | Standard | Cutting-edge |

**Conséquences** :
- ✅ Performance web maximale (Lighthouse 100 = argument crédibilité)
- ✅ Flexibilité design totale (homepage pro sans compromis)
- ✅ Maintenance simplifiée (architecture claire, pas de plugins complexes)
- ✅ Modernité démontrée (Astro = tendance 2025-2026)
- ⚠️ Écosystème plus petit que Docusaurus (mais suffisant pour nos besoins)
- ⚠️ Courbe apprentissage Astro (mais plus simple que Docusaurus + React custom)

---

### ADR-002 : Hébergement GitHub Pages vs. Vercel vs. Netlify

**Contexte** : Besoin hébergement gratuit, fiable, simple déploiement.

**Options Évaluées** :
- GitHub Pages (gratuit, intégré repo)
- Vercel (gratuit tier, excellent DX)
- Netlify (gratuit tier, features riches)
- AWS S3 + CloudFront (complexité, coût)

**Décision** : Vercel (avec GitHub Pages comme fallback)

**Justification** :
- ✅ Déploiement automatique push main
- ✅ Preview deployments PR (validation avant merge)
- ✅ Analytics basiques inclus
- ✅ Domaine custom gratuit (docdriven.dev)
- ✅ Edge network global (latence minimale)
- ✅ Zéro config Docusaurus (détection automatique)

**Conséquences** :
- ✅ Workflow dev optimisé
- ✅ Performance maximale (edge caching)
- ⚠️ Dépendance plateforme (mitigation : export static possible)

---

### ADR-003 : Diagramme 6-Phase Interactif vs. Statique

**Contexte** : Élément visuel central homepage, doit impressionner sans compliquer. Astro permet Islands Architecture (JavaScript sélectif).

**Options Évaluées** :
- SVG statique (simple, léger)
- **React component interactif avec Astro Islands** (tooltips, hover states)
- Canvas animation (complexe, lourd)
- Image PNG haute-res (fallback)

**Décision** : **React Component + Astro Islands Architecture**

**Justification** :
- ✅ **Islands = Optimal** : JavaScript charge SEULEMENT pour diagramme, reste page static
- ✅ SVG = scalable, léger (<50kb)
- ✅ Tooltips hover = révèle détails sans surcharge
- ✅ Accessibilité (ARIA labels, keyboard navigation)
- ✅ Dégradation gracieuse (fallback statique mobile)
- ✅ **Performance maintenue** : Astro hydrate seulement quand visible (`client:visible`)
- ❌ Pas d'animations complexes (alourdirait inutilement)

**Implémentation Astro** :
```astro
---
// src/pages/index.astro
import DiagramSixPhase from '../components/DiagramSixPhase';
---

<section class="architecture">
  <h2>Une Méthodologie en 6 Phases</h2>
  
  <!-- client:visible = hydrate React seulement quand visible viewport -->
  <!-- Zéro JavaScript chargé si utilisateur ne scroll pas -->
  <DiagramSixPhase client:visible />
</section>
```

```tsx
// src/components/DiagramSixPhase.tsx (React)
import { useState } from 'react';

export default function DiagramSixPhase() {
  const [activePhase, setActivePhase] = useState<number | null>(null);
  
  return (
    <svg viewBox="0 0 1200 400" className="diagram">
      {phases.map(phase => (
        <PhaseBlock 
          key={phase.id}
          phase={phase}
          isActive={activePhase === phase.id}
          onMouseEnter={() => setActivePhase(phase.id)}
          onMouseLeave={() => setActivePhase(null)}
        />
      ))}
    </svg>
  );
}
```

**Conséquences** :
- ✅ Impact visuel immédiat (interactivité professionnelle)
- ✅ Performance préservée (Islands = JavaScript minimal)
- ✅ Accessibilité native (React + ARIA)
- ✅ Bundle optimal (~30kb React + 20kb component = 50kb total pour interactivité)
- ⚠️ Développement custom nécessaire (3-4 jours effort)

**Avantage Astro vs Docusaurus** :
- Astro : `client:visible` = hydratation lazy automatique
- Docusaurus : Tout React bundle charge immédiatement (pas d'Islands)

---

### ADR-004 : Dissociation Auteur/Méthode (Architecture de l'Information)

**Contexte** : Éric refuse positionnement "gourou", veut DocDriven > lui.

**Options Évaluées** :
- Homepage mentionne auteur (hero section)
- Section "À Propos" en sidebar
- Page séparée "À Propos de l'Auteur"
- Footer mention discrète seulement

**Décision** : Page séparée "À Propos de l'Auteur" + footer mention

**Justification** :
- ✅ Homepage focus 100% méthodologie (pas personne)
- ✅ Recruteur cherchant info Éric = 1 clic évident
- ✅ Respecte intégrité intellectuelle Éric
- ✅ Évite narcissisme perçu
- ✅ Permet utilisation portfolio emploi (lien direct page About)

**Implémentation** :
- Homepage hero : "DOC//DRIVEN" (zéro mention auteur)
- Footer : "Created by Éric Gauthier | About →"
- Nav menu : "About" (top-right, discret)
- Page /about : Bio complète, CV, contact

**Conséquences** :
- ✅ Cohérence positionnement "méthodologie open source"
- ✅ Utilisable en portfolio sans paraître auto-promo
- ⚠️ Risque attribution floue (mitigation : footer + license mention)

---

## 10. Plan de Validation & Approbations

### 10.1 Points de Validation Requis

**Validation 1 : Architecture Stratégique (Ce Document)**
- **Reviewer** : Éric Gauthier
- **Critères** : Alignement contraintes, décisions claires, faisabilité
- **Action** : GO/NO-GO Phase 2
- **Deadline** : J+2 (2 jours révision)

**Validation 2 : Wireframes Homepage**
- **Reviewer** : Éric + Équipe consultation
- **Critères** : Flow information, hiérarchie visuelle, messaging clair
- **Action** : Itération design ou GO Phase 3
- **Deadline** : Fin Semaine 1

**Validation 3 : Contenu Final (Copy)**
- **Reviewer** : Éric (ton de voix) + Julien (polish)
- **Critères** : Authenticité, clarté, zéro typo
- **Action** : Approbation ou révision mineure
- **Deadline** : Fin Semaine 2

**Validation 4 : Design Visuel (Mockups)**
- **Reviewer** : Éric + Élodie
- **Critères** : Sobriété, professionnalisme, cohérence
- **Action** : Approbation ou ajustements
- **Deadline** : Fin Semaine 3

**Validation 5 : QA Pré-Lancement**
- **Reviewers** : Éric (validation finale) + 2 externes (feedback)
- **Critères** : Critères succès V1.0 (Section 5.2) tous validés
- **Action** : LAUNCH ou blockers identifiés
- **Deadline** : Fin Semaine 4

### 10.2 Processus Décisionnel

**Décisions Architecture** : Éric (final) + Sophie (recommandations)
**Décisions Design** : Éric (final) + Élodie (recommandations)
**Décisions Copy** : Éric (final) + Julien (recommendations)
**Décisions Techniques** : Éric (si compétences) sinon Sophie lead

**Règle d'Or** : En cas de désaccord, **contrainte "Crédibilité Professionnelle" prime** (objectif #1).

---

## 11. Annexes

### Annexe A : Références de Design (Inspiration)

**Sites "Documentation Industrielle"** :
- Stripe Docs (https://stripe.com/docs) - Clarté, navigation
- Tailwind CSS (https://tailwindcss.com) - Sobriété, code-centric
- Rust Book (https://doc.rust-lang.org/book/) - Structure progressive
- AWS Well-Architected (https://aws.amazon.com/architecture/well-architected/) - Frameworks

**Éléments à Imiter** :
- Navigation sidebar claire (Stripe)
- Hero minimaliste, message direct (Tailwind)
- Progression pédagogique (Rust Book)
- Diagrammes d'architecture sobres (AWS)

**Éléments à ÉVITER** :
- Illustrations fantaisistes (Mailchimp, Dropbox)
- Animations complexes (Apple)
- Gradients colorés (startups SaaS)
- Hero videos (marketing lourd)

### Annexe B : Glossaire Technique

- **ADR** : Architecture Decision Record (documentation décision architecturale)
- **LLM** : Large Language Model (modèle de langage IA)
- **MVP** : Minimum Viable Product (produit minimal fonctionnel)
- **PSC** : Propensity Smelly Score (métrique qualité code)
- **SSG** : Static Site Generator (générateur site statique)
- **TDD** : Test-Driven Development (développement piloté par tests)

### Annexe C : Ressources & Contacts

**Domaines** :
- docdriven.dev (à enregistrer, ~$15/an)
- Alternative : docdriven.org (si .dev indisponible)

**Hébergement** :
- **Vercel** (gratuit, optimisé Astro) : https://vercel.com
- Alternative Netlify : https://netlify.com
- GitHub Pages (fallback) : https://pages.github.com

**Framework & Documentation** :
- **Astro Docs** : https://docs.astro.build
- Astro Themes : https://astro.build/themes
- Astro Discord : https://astro.build/chat (communauté support)

**Design Tools** :
- Figma (wireframes/mockups) : https://figma.com
- Excalidraw (diagrammes rapides) : https://excalidraw.com
- Coolors (palette) : https://coolors.co

**Fonts** :
- JetBrains Mono : https://www.jetbrains.com/lp/mono/
- Inter : https://rsms.me/inter/

**Astro Integrations Utiles** :
- @astrojs/react : Support React components
- @astrojs/sitemap : Génération sitemap.xml
- @astrojs/tailwind : Tailwind CSS (optionnel)
- astro-seo : SEO meta tags helpers

**Performance Monitoring** :
- Lighthouse CI : https://github.com/GoogleChrome/lighthouse-ci
- WebPageTest : https://www.webpagetest.org
- Vercel Analytics (built-in) : Dashboard performance temps réel

---

## 12. Signatures & Approbations

**Architecte Principal** : Éric Gauthier  
**Date Création** : 2026-01-07  
**Version** : 1.0 - DRAFT

**Approbation Requise** :
- [ ] Éric Gauthier (Décision GO/NO-GO Phase 2)
- [ ] Sophie Delarive (Validation architecture technique)

**Prochaine Action** : Éric révise ce document, fournit feedback/approbation, déclenche Phase 2 (Tactical Planning).

---

*Fin du Document d'Architecture Stratégique*

**Prochaine Étape DocDriven** : Phase 2 - Tactical Planning (Plan d'Implémentation Détaillé)
