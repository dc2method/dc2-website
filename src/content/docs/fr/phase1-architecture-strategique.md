---
title: "Phase 1 : Architecture Stratégique"
description: "Définir la vision architecturale et les décisions stratégiques du projet"
sidebar_position: 2
lang: fr
---

# Phase 1 : Architecture Stratégique

<!-- ========================================= -->
<!-- NIVEAU 1 : ESSENTIEL (5-10 secondes)     -->
<!-- ========================================= -->

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile : Sprint 0 / Inception
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Rôles : Concepteur + Product Owner
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Humain : 65%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM : 35%
  </span>
</div>

---

**En bref** : Crée la vision architecturale documentée (ADR + schémas) qui donne au LLM la "carte mentale" qu'il n'a pas naturellement. Décisions stratégiques prises par humains, alternatives explorées avec aide LLM.

---

<!-- ========================================= -->
<!-- NIVEAU 2 : IMPACT (30-60 secondes)       -->
<!-- ========================================= -->

## Pourquoi Cette Phase Est Critique

**Le problème sans Phase 1** :  
LLM génère du code basé sur patterns génériques internet, sans compréhension du contexte spécifique. Propose solutions déconnectées des besoins réels (ex: base SQL au lieu de vectorielle). Erreurs architecturales fondamentales découvertes tardivement nécessitent refonte complète.

**La solution apportée** :  
Document d'Architecture Stratégique crée représentation explicite du système : pourquoi chaque composant existe, quelles contraintes respecter, quels compromis acceptés. Le LLM reçoit le contexte business et technique qu'il ne peut deviner.

**Limites LLM adressées** :
- **Pas de représentation interne** : ADR et schémas créent la "carte mentale" explicite (composants, dépendances, impacts)
- **Pas de compréhension rôle architecture** : Documentation explique pourquoi composant existe, quel problème business résout, quels compromis architecturaux

**Impact mesuré** :
- Refontes architecturales évitées grace aux décisions validées avant codage
- Temps onboarding nouveaux devs plus rapide
- Qualité de la génération de code
- Dette technique évitée : Les décisions documentées évitent la "connaissance tribale"

---

<!-- ========================================= -->
<!-- NIVEAU 3 : COMMENT FAIRE (2-5 minutes)   -->
<!-- ========================================= -->

## Déroulement

**Entrées** :
- Exigences business et critères de succès
- Contraintes techniques (systèmes existants, standards, performance)
- Contraintes organisationnelles (compétences équipe, chronologie, budget)
- Priorités parties prenantes
- Documentation système existant (si refactoring/extension)

### 1. Cristallisation du Problème ⏱️⏱️

**Concepteur 80%, LLM 20%**

- Concepteur articule problème business clairement
- LLM aide identifier hypothèses non formulées
- Séparer symptômes vs causes racines
- Définir critères de succès quantitatifs

**Sortie** : Énoncé problème précis avec métriques succès

### 2. Cartographie des Contraintes ⏱️

**Concepteur 60%, LLM 40%**

- Concepteur identifie contraintes depuis expérience
- LLM génère checklist contraintes complète
- Prioriser contraintes (indispensables vs souhaitables)
- Documenter contraintes organisationnelles/politiques

**Sortie** : Liste contraintes priorisées (techniques + orga)

### 3. Génération de Solutions ⏱️⏱️

**Concepteur 50%, LLM 50%**

- Concepteur fournit 1-2 directions solution initiales
- LLM génère 2-3 approches alternatives
- Assurer au moins une approche innovante/non conventionnelle
- Documenter chaque approche avec diagrammes architecture

**Sortie** : 3-4 approches solution avec diagrammes C4

### 4. Analyse des Compromis ⏱️⏱️

**Concepteur 70%, LLM 30%**

- Concepteur évalue approches contre priorités business
- LLM génère matrice comparaison compromis
- Identifier risques et stratégies atténuation par approche
- Concepteur décision finale avec justification documentée

**Sortie** : Matrice compromis + décision justifiée

### 5. Validation Parties Prenantes ⏱️⏱️

**Humain 90%, LLM 10%**

- Présentation recommandation à Product Owner
- Discussion compromis, validation alignement business
- Révisions selon feedback (peut nécessiter 1-2 cycles)
- Approbation finale formelle

**Sortie** : Document Architecture approuvé

## Document d'Architecture Stratégique Produit

**Taille** : 2,000-4,000 mots

**Sections** :
1. **Résumé Exécutif** (~200 mots) : Problème + solution recommandée
2. **Définition du Problème** : Analyse cause racine, critères de succès
3. **Contraintes** : Techniques, organisationnelles, chronologie, budget
4. **Approches de Solution** : 2-4 approches avec diagrammes C4 niveaux 1-2
5. **Analyse des Compromis** : Matrice comparaison, évaluation risques
6. **Recommandation** : Approche choisie avec justification explicite
7. **Métriques de Succès** : Comment mesurer si solution réussit
8. **Atténuation des Risques** : Top 3-5 risques et stratégies

## Definition of Done

Cette phase est considérée terminée quand :

1. Le problème business est clairement articulé avec critères de succès quantifiés
2. Au moins 3 ADR (Architecture Decision Records) documentent les décisions majeures
3. Un schéma d'architecture de haut niveau existe (diagrammes C4 niveaux 1-2)
4. Les contraintes techniques critiques sont identifiées et priorisées
5. La solution choisie inclut une justification claire des compromis vs alternatives
6. Les risques architecturaux principaux sont documentés avec stratégies d'atténuation
7. Le Product Owner valide que la solution proposée répond aux besoins business

---

<!-- ========================================= -->
<!-- NIVEAU 4 : MAÎTRISER (5-15 minutes)      -->
<!-- Contenu détaillé caché par défaut        -->
<!-- ========================================= -->

## Pour Aller Plus Loin

<details>
<summary><strong>Voir exemples concrets, prompts et ADR détaillés</strong></summary>

### Exemple Complet : Système de Recommandation Nutritionnelle

#### Contexte Business

Une application nutrition veut recommander des aliments basé sur profile utilisateur (allergies, préférences, objectifs santé). Actuellement : liste statique par catégorie. Objectif : recommandations personnalisées temps réel.

#### 1. Cristallisation du Problème

**Énoncé initial (vague)** :  
"Nous voulons améliorer les recommandations d'aliments pour rendre l'app plus utile."

**Après cristallisation avec LLM** :

**Problème précis** :  
Les utilisateurs abandonnent l'app (taux rétention J7 : 12%) car recommandations actuelles ne tiennent pas compte de leurs contraintes (allergies arachides, régime végétarien, objectif perte poids). 35% utilisateurs rapportent "suggestions non pertinentes" dans surveys.

**Causes racines** :
- Système actuel : logique if/then statique (120 lignes code spaghetti)
- Pas de prise en compte similarité entre aliments
- Pas de score confiance sur recommandations
- Pas de mécanisme apprentissage (feedback utilisateur ignoré)

**Critères de succès quantifiés** :
1. Taux rétention J7 : 12% → 25% (+108%)
2. Satisfaction recommandations : 2.1/5 → 4.0/5
3. Temps réponse API : < 200ms (95e percentile)
4. Couverture allergies/restrictions : 100% (vs 60% actuel)

#### 2. Cartographie des Contraintes

**Contraintes techniques indispensables** :
- Backend : Python 3.11+ (stack existant)
- Latence API : < 200ms p95 (UX critique)
- Base données : PostgreSQL existant (migration coûteuse interdite)
- Volume : 50,000 utilisateurs actifs, 10M aliments DB

**Contraintes organisationnelles** :
- Équipe : 2 devs backend, 1 dev frontend (pas data scientist)
- Timeline : MVP en 6 semaines (deadline business)
- Budget infrastructure : +$500/mois max
- Pas expertise ML/AI in-house

**Contraintes souhaitables (nice-to-have)** :
- Explicabilité recommandations (pourquoi cet aliment ?)
- Mode offline basique (cache dernières reco)
- Support multilingue (FR/EN)

#### 3. Génération de Solutions

**Approche 1 : Système Règles Avancé (Concepteur)**

```
Architecture :
┌──────────────────┐
│  User Profile    │
│  (allergies,     │
│   restrictions)  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────────┐
│  Rules Engine    │─────▶│  Food Database   │
│  (500+ rules)    │      │  (PostgreSQL)    │
└────────┬─────────┘      └──────────────────┘
         │
         ▼
┌──────────────────┐
│  Ranked Results  │
└──────────────────┘
```

**Avantages** :
- Totalement explicable (règles = justification)
- Pas besoin expertise ML
- Latence prévisible (< 50ms)

**Inconvénients** :
- Maintenance cauchemar (500+ règles à jour)
- Pas d'apprentissage (feedback utilisateur perdu)
- Scalabilité limitée (règles explosent avec complexité)

**Complexité** : Moyenne (implémentation simple, maintenance élevée)  
**Risques** : Dette technique majeure après 1 an

---

**Approche 2 : Recherche Vectorielle + Filtrage (LLM - innovante)**

```
Architecture :
┌──────────────────┐
│  User Profile    │
│  embeddings      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────────┐
│  Vector Search   │      │  pgvector        │
│  (cosine sim)    │─────▶│  (extension PG)  │
└────────┬─────────┘      └──────────────────┘
         │
         ▼
┌──────────────────┐
│  Hard Filters    │
│  (allergies)     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Ranked Results  │
│  + confidence    │
└──────────────────┘
```

**Avantages** :
- Similarité sémantique (trouve aliments proches)
- Pas maintenance règles (embeddings appris)
- Confidence scores naturels (distance cosine)
- Utilise PostgreSQL existant (pgvector extension)

**Inconvénients** :
- Embeddings à générer (coût initial)
- Explicabilité réduite (distance cosine ≠ raison business)
- Équipe doit apprendre concepts vecteurs

**Complexité** : Moyenne-Élevée (nouveauté technique)  
**Risques** : Courbe apprentissage équipe, qualité embeddings

---

**Approche 3 : API ML Externe (LLM - alternative)**

```
Architecture :
┌──────────────────┐
│  User Profile    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────────┐
│  API Gateway     │      │  OpenAI API      │
│  (cache 1h)      │─────▶│  (embeddings)    │
└────────┬─────────┘      └──────────────────┘
         │
         ▼
┌──────────────────┐
│  Post-processing │
│  (filtres)       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Ranked Results  │
└──────────────────┘
```

**Avantages** :
- Zéro expertise ML in-house nécessaire
- Qualité embeddings garantie (OpenAI)
- Maintenance minimale

**Inconvénients** :
- Coût récurrent (~$2000/mois estimé)
- Dépendance externe (disponibilité API)
- Latence variable (réseau)
- Données utilisateur envoyées externe (privacy ?)

**Complexité** : Faible (API call simple)  
**Risques** : Coûts explosent avec volume, vendor lock-in

#### 4. Analyse des Compromis

**Matrice comparaison** :

| Dimension | Règles Avancé | Vecteurs pgvector | API ML Externe |
|-----------|---------------|-------------------|----------------|
| **Temps dev** | 4 semaines | 5-6 semaines | 2-3 semaines |
| **Complexité tech** | 4/10 | 7/10 | 3/10 |
| **Maintenabilité** | 2/10 (règles explosent) | 8/10 (auto-learning) | 9/10 (externalisé) |
| **Performance** | 9/10 (< 50ms) | 7/10 (< 150ms) | 5/10 (200ms+ réseau) |
| **Coût infra** | $50/mois | $200/mois | $2000/mois |
| **Risque** | Élevé (dette tech) | Moyen (courbe apprentissage) | Moyen (dépendance) |
| **Scalabilité** | Faible | Élevée | Élevée |
| **Explicabilité** | 10/10 (règles claires) | 4/10 (distance cosine) | 3/10 (black box) |

**Recommandation : Approche 2 (Vecteurs pgvector)**

**Justification** :
1. **Respecte contraintes budget** : $200/mois < $2000/mois API externe
2. **Scalabilité long terme** : Évite dette technique règles
3. **Utilise stack existant** : pgvector = extension PostgreSQL (pas migration)
4. **Timeline acceptable** : 5-6 semaines vs 4 (différence gérable)
5. **Investissement apprentissage** : Équipe apprend compétence valuable (vecteurs = futur)

**Compromis acceptés** :
- Complexité technique +30% vs règles simples
- Explicabilité réduite (mais confidence scores compensent partiellement)
- Courbe apprentissage équipe (mitigé par doc + formation 2 jours)

**Compromis rejetés** :
- API externe : coûts récurrents 10x trop élevés
- Règles avancé : dette technique inacceptable (maintenance explosive)

#### 5. ADR Produits

**ADR-001 : Utiliser pgvector pour recherche similarité**

**Statut** : Accepté  
**Date** : 2025-12-28  
**Décideurs** : Concepteur + Product Owner

**Contexte** :  
Système recommandation actuel (règles if/then statiques) ne scale pas. Besoin similarité sémantique entre aliments pour recommandations pertinentes.

**Décision** :  
Utiliser extension pgvector dans PostgreSQL existant pour recherche vectorielle basée cosine similarity.

**Alternatives considérées** :
1. **Système règles avancé** : Rejeté (maintenance explosive, pas scalable)
2. **API ML externe (OpenAI)** : Rejeté (coûts $2000/mois trop élevés)
3. **Migration base vectorielle dédiée (Pinecone)** : Rejeté (migration coûteuse interdite)

**Conséquences** :
- Utilise infrastructure existante (PostgreSQL)
- Coût infrastructure acceptable ($200/mois)
- Similarité sémantique sans maintenance règles
- Équipe doit apprendre concepts embeddings (formation 2 jours)
- Explicabilité réduite vs règles (compensé par confidence scores)

---

**ADR-002 : Générer embeddings via sentence-transformers local**

**Statut** : Accepté  
**Date** : 2025-12-28

**Contexte** :  
Besoin générer embeddings pour 10M aliments + profiles utilisateurs. Choix : API externe (OpenAI) vs modèle local.

**Décision** :  
Utiliser `sentence-transformers` (modèle `all-MiniLM-L6-v2`) localement.

**Justification** :
- Coût zéro après génération initiale (vs $2000/mois API)
- Latence prévisible (pas dépendance réseau)
- Privacy : données restent on-premise
- Performance suffisante (384 dimensions, qualité acceptable nutrition domain)

**Conséquences** :
- Coûts contrôlés long terme
- Latence stable (< 50ms génération embedding)
- Génération initiale 10M embeddings = 8h compute (one-time)
- Qualité embeddings inférieure à GPT-4 (acceptable pour MVP)

---

**ADR-003 : Filtrage dur allergies AVANT recherche vectorielle**

**Statut** : Accepté  
**Date** : 2025-12-28

**Contexte** :  
Utilisateurs avec allergies (arachides, gluten, lactose) NE DOIVENT JAMAIS recevoir recommandations dangereuses, même si similarité vectorielle élevée.

**Décision** :  
Appliquer filtres allergies PostgreSQL (WHERE clauses) AVANT recherche vectorielle. Sécurité > pertinence.

**Justification** :
- Criticité sécurité : Recommandation allergène = risque santé
- Performance : Filtrage SQL très rapide (index)
- Certitude : Filtres durs = garantie 100% (vs ML probabiliste)

**Conséquences** :
- Sécurité allergies garantie
- Conformité réglementaire santé
- Pool candidats réduit (peut impacter diversité)
- Maintenance liste allergènes (DB table à jour)

### Prompts Recommandés

#### Prompt 1 : Cristallisation du Problème

```
Je conçois une solution pour [problème business]. Voici l'énoncé initial :

PROBLÈME :
[coller description problème vague/initiale]

CONTEXTE :
- Utilisateurs : [qui]
- Système actuel : [comment ça marche aujourd'hui]
- Plaintes principales : [feedback users]

Aide-moi à cristalliser ce problème en :

1. **Identifier hypothèses non formulées** : Quelles suppositions ai-je faites 
   qui ne sont pas explicites ?

2. **Séparer symptômes vs causes racines** : 
   - Symptômes observés : [ce que les users voient]
   - Causes racines probables : [pourquoi ça arrive]

3. **Suggérer 3-5 critères de succès QUANTITATIFS** :
   - Format : Métrique actuelle → Métrique cible (+% amélioration)
   - Exemples : "Taux rétention J7 : 12% → 25% (+108%)"

4. **Risques de dérive de périmètre** : Quels aspects pourraient élargir 
   le projet de façon dangereuse ?

Format réponse : Markdown structuré avec sections claires.
```

#### Prompt 2 : Génération de Solutions

```
Étant donné cette définition de problème et contraintes :

PROBLÈME :
[coller problème cristallisé]

CONTRAINTES INDISPENSABLES :
- Techniques : [ex: Python 3.11+, latence < 200ms, PostgreSQL existant]
- Organisationnelles : [ex: équipe 3 devs, 6 semaines, pas expertise ML]
- Budget : [ex: +$500/mois infra max]

PRIORITÉS BUSINESS :
[ex: 1. Rétention utilisateurs, 2. Time-to-market, 3. Coûts opérationnels]

J'ai identifié cette approche initiale :

APPROCHE CONCEPTEUR :
[coller solution initiale 2-3 paragraphes]

Génère 2-3 approches de solution ALTERNATIVES qui :
- Abordent le même problème différemment
- Fonctionnent dans contraintes énoncées
- **Incluent au moins UNE approche innovante/non conventionnelle**
- Sont techniquement faisables pour ce contexte

Pour CHAQUE solution, fournis :

1. **Nom approche** (descriptif court)
2. **Architecture haut niveau** :
   - Composants principaux (3-5 max)
   - Interactions entre composants (flux données)
   - Diagramme ASCII simple
3. **Avantages clés** (3-5 points)
4. **Inconvénients clés** (3-5 points)
5. **Complexité estimée** : Faible / Moyenne / Élevée (justifier)
6. **Risques principaux** (top 2-3 avec impact)
7. **Estimation temps dev** : X semaines (range acceptable)

Format : Markdown, une section par approche.
```

#### Prompt 3 : Analyse des Compromis

```
Crée une matrice de comparaison des compromis pour ces approches :

APPROCHES DE SOLUTION :
[coller 3-4 approches générées précédemment]

Compare selon ces dimensions (note 1-10 ou Low/Medium/High) :

1. **Temps de développement** : Semaines estimées
2. **Complexité technique** : 1-10 (1 = trivial, 10 = expert requis)
3. **Maintenabilité** : Coût maintenance long terme (Low/Med/High)
4. **Performance** : Répond exigences ? Latence estimée
5. **Niveau de risque** : Low/Medium/High (technique + business)
6. **Adéquation organisationnelle** : Compétences équipe, culture
7. **Scalabilité** : Croissance future (utilisateurs, données)
8. **Coût infrastructure** : $/mois estimé
9. **Explicabilité** : Peut-on expliquer résultats users ? (1-10)

Pour chaque dimension, explique brièvement la notation (1-2 phrases).

Puis RECOMMANDE quelle approche équilibre le mieux les compromis 
pour ce contexte :

PRIORITÉS BUSINESS (ordre importance) :
[coller priorités : ex: 1. Rétention, 2. Time-to-market, 3. Coûts]

CONTRAINTES NON NÉGOCIABLES :
[coller contraintes dures]

Format recommandation :
- **Approche recommandée** : [laquelle]
- **Justification** : Pourquoi cette approche (5-7 points)
- **Compromis acceptés** : Ce qu'on sacrifie consciemment
- **Compromis rejetés** : Ce qu'on refuse de sacrifier
```

### Standards de Qualité

#### Bon Document d'Architecture

**Caractéristiques** :
- **Problème quantifié** : "Rétention J7 : 12%" pas "mauvaise rétention"
- **3+ alternatives évaluées** : Pas décision unique sans comparaison
- **Compromis explicites** : "On accepte complexité +30% pour éviter dette technique"
- **ADR concrets** : Décisions documentées avec alternatives rejetées
- **Schémas C4 clairs** : Composants + interactions visibles
- **Validation PO formelle** : Signature/approbation explicite

**Exemple bonne décision documentée** :
```
ADR-001 : Utiliser pgvector

Alternatives considérées :
1. Règles avancé (rejeté : dette tech)
2. API OpenAI (rejeté : $2000/mois)
3. Migration Pinecone (rejeté : coût migration)

Décision : pgvector
Justification : Équilibre coût/performance/maintenance
Compromis accepté : Complexité +30%, courbe apprentissage
Conséquences : Formation équipe 2 jours, doc embeddings
```

#### Mauvais Document d'Architecture

**Problèmes** :
- **Problème vague** : "Améliorer l'app" sans métriques
- **Solution unique** : Pas d'alternatives évaluées
- **Biais technologie** : "Utilisons GraphQL" sans justifier pourquoi
- **Compromis cachés** : Seulement bénéfices, pas inconvénients
- **Contraintes ignorées** : Solution parfaite théorique, équipe incapable exécuter
- **Pas validation PO** : Architecte décide seul

**Exemple mauvaise décision** :
```
On va utiliser GraphQL.

[Fin. Pas d'alternatives, pas de pourquoi, pas de compromis]
```
→ Impossible de comprendre contexte ou challengerla décision

### Pièges Courants

#### 1. Analyse à Approche Unique

**Problème** :  
Concepteur évalue seulement SA solution préférée. Pas de vraies alternatives. Fausse impression choix objectif.

**Solution** :
- **Minimum 3 approches** : Concepteur + 2 alternatives LLM
- **Une approche "folle"** : Innovante/non conventionnelle forcée
- **Évaluation honnête** : Chaque approche a avantages ET inconvénients
- **Matrice comparative** : Impossible de biaiser si toutes dimensions listées

**Check DoD #5** : "Solution choisie inclut justification vs alternatives"

---

#### 2. Pensée Technologie-D'abord

**Problème** :  
"Utilisons Kubernetes !" avant de comprendre problème. Choisir pile techno avant besoins = échec garanti.

**Exemple** :
```
Concepteur : "On va faire microservices avec Kubernetes"
Réalité : 3 utilisateurs/jour, 1 dev équipe
→ Over-engineering massif
```

**Solution** :
- **Ordre strict** : Problème → Contraintes → Solutions → Technologies
- **Justification tech** : Chaque choix techno doit répondre à contrainte spécifique
- **YAGNI** : "You Aren't Gonna Need It" - simplicité par défaut

**Bon processus** :
```
1. Problème : Latence API > 500ms (users frustrés)
2. Contrainte : Doit passer < 200ms
3. Solution : Cache en mémoire
4. Technologie : Redis (justifié pour vitesse)
```

---

#### 3. Ignorer Contraintes Organisationnelles

**Problème** :  
Conception solution parfaite techniquement, mais équipe incapable exécuter. Architecture nécessite expertise ML, équipe a zéro expérience.

**Exemple réel** :
```
Architecture : Système recommandation deep learning custom
Équipe réelle : 2 devs backend Python, zéro ML
Timeline : 6 semaines
→ Impossible. Projet échoue.
```

**Solution** :
- **Cartographie compétences** : Qui sait faire quoi réellement
- **Apprentissage budgété** : Si nouvelle techno, ajouter temps formation
- **Alternatives réalistes** : "Solution parfaite impossible" → "Solution faisable bonne"

**Check DoD #4** : "Contraintes techniques ET organisationnelles identifiées"

---

#### 4. Paralysie de l'Analyse

**Problème** :  
LLM génère 15 approches. Concepteur passe 2 semaines analyser toutes. Deadline explose. Jamais de décision.

**Solution** :
- **Limite stricte : 3-4 approches max**
- **Timeboxing** : Phase 1 = 1-2 jours, pas 2 semaines
- **"Good enough" > "Perfect"** : Viser 80% certitude, pas 100%
- **Décision validable** : Mieux décider vite et ajuster que analyser à l'infini

**Signal problème** : Phase 1 dure > 3 jours = paralysie analysis

---

#### 5. Critères de Succès Vagues

**Problème** :  
"Améliorer la performance", "Augmenter satisfaction users". Impossible mesurer si succès ou échec.

**Exemples vagues** :
```
 "Rendre l'app plus rapide"
 "Augmenter la qualité"
 "Améliorer l'expérience utilisateur"
```

**Solution** :
- **Métriques quantifiées** : Nombre précis
- **Baseline actuelle** : D'où on part
- **Cible spécifique** : Où on veut aller
- **% amélioration** : Ampleur changement

**Exemples bons** :
```
"Réduire latence p95 : 500ms → < 200ms (-60%)"
"Taux rétention J7 : 12% → 25% (+108%)"
"Score satisfaction : 2.1/5 → 4.0/5 (+90%)"
```

**Check DoD #1** : "Problème business avec critères succès quantifiés"

---

#### 6. Adhésion Manquante des Parties Prenantes

**Problème** :  
Concepteur décide seul architecture. Présente "fait accompli" à Product Owner. PO découvre solution pas alignée priorités business. Refait Phase 1.

**Solution** :
- **PO impliqué dès cristallisation problème** : Valide critères succès
- **Révision collaborative compromis** : PO arbitre priorités conflictuelles
- **Approbation formelle** : PO signe document avant Phase 2
- **Feedback loops** : 1-2 cycles révision normaux

**Check DoD #7** : "Product Owner valide solution répond besoins business"

### Format ADR Standard

**Template réutilisable** :

```markdown
# ADR-XXX : [Titre Décision]

**Statut** : [Proposé / Accepté / Rejeté / Déprécié / Supersédé]
**Date** : YYYY-MM-DD
**Décideurs** : [Qui a décidé]

## Contexte

[Pourquoi cette décision est nécessaire. Quel problème résout-elle ?
2-4 paragraphes contexte business et technique.]

## Décision

[Quelle décision a été prise. Énoncé clair et concis. 1-2 paragraphes.]

## Alternatives Considérées

### Alternative 1 : [Nom]
**Avantages** : [2-3 points]
**Inconvénients** : [2-3 points]
**Raison rejet** : [Pourquoi pas choisie]

### Alternative 2 : [Nom]
[Idem]

## Justification

[Pourquoi cette décision vs alternatives. Référence priorités business.
3-5 paragraphes argumentés.]

## Conséquences

**Positives** :
- [Conséquence positive 1]
- [Conséquence positive 2]

**Négatives / Compromis Acceptés** :
- [Compromis 1]
- [Compromis 2]

**Actions Requises** :
- [ ] [Action 1 pour implémenter décision]
- [ ] [Action 2]

## Références

- [Lien document architecture]
- [Lien discussion Slack/email]
- [Benchmark performance]
```

</details>

---

**Prochaine étape** : [Phase 2 : Plan Tactique + Transfert Critique →](/fr/phase2-planification-tactique)

**Besoin d'aide ?** Consultez le [document Rôles et Responsabilités](/fr/roles-et-responsabilites) pour clarifier qui fait quoi dans cette phase.
