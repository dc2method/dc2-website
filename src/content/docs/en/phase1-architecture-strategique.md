---
title: "Phase 1: Strategic Architecture"
description: "Define the architectural vision and strategic decisions of the project"
sidebar_position: 2
lang: en
---

# Phase 1: Strategic Architecture

<!-- ========================================= -->
<!-- LEVEL 1: ESSENTIAL (5-10 seconds)       -->
<!-- ========================================= -->

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile: Sprint 0 / Inception
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Roles: Architect + Product Owner
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Human: 65%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM: 35%
  </span>
</div>

---

**In brief**: Creates the documented architectural vision (ADRs + diagrams) that provides the LLM with the "mental map" it naturally lacks. Strategic decisions made by humans, alternatives explored with LLM assistance.

---

<!-- ========================================= -->
<!-- LEVEL 2: IMPACT (30-60 seconds)         -->
<!-- ========================================= -->

## Why This Phase Is Critical

**The problem without Phase 1**:
LLM generates code based on generic internet patterns, without understanding the specific context. Proposes solutions disconnected from real needs (e.g., SQL database instead of vectorial). Fundamental architectural errors discovered late require complete redesign.

**The solution provided**:
Strategic Architecture Document creates explicit system representation: why each component exists, which constraints must be respected, which trade-offs are accepted. The LLM receives the business and technical context it cannot guess.

**LLM limitations addressed**:
- **No internal representation**: ADRs and diagrams create the explicit "mental map" (components, dependencies, impacts)
- **No understanding of architecture role**: Documentation explains why a component exists, what business problem it solves, which architectural trade-offs it represents

**Measured impact**:
- Architectural redesigns avoided thanks to validated decisions before coding
- Faster onboarding time for new developers
- Improved code generation quality
- Technical debt avoided: Documented decisions prevent "tribal knowledge"

---

<!-- ========================================= -->
<!-- LEVEL 3: HOW TO DO IT (2-5 minutes)     -->
<!-- ========================================= -->

## Process Flow

**Inputs**:
- Business requirements and success criteria
- Technical constraints (existing systems, standards, performance)
- Organizational constraints (team skills, timeline, budget)
- Stakeholder priorities
- Existing system documentation (if refactoring/extension)

### 1. Problem Crystallization ⏱️⏱️

**Architect 80%, LLM 20%**

- Architect articulates business problem clearly
- LLM helps identify unstated assumptions
- Separate symptoms from root causes
- Define quantitative success criteria

**Output**: Precise problem statement with success metrics

### 2. Constraint Mapping ⏱️

**Architect 60%, LLM 40%**

- Architect identifies constraints from experience
- LLM generates comprehensive constraint checklist
- Prioritize constraints (mandatory vs. nice-to-have)
- Document organizational/political constraints

**Output**: Prioritized constraint list (technical + organizational)

### 3. Solution Generation ⏱️⏱️

**Architect 50%, LLM 50%**

- Architect provides 1-2 initial solution directions
- LLM generates 2-3 alternative approaches
- Ensure at least one innovative/unconventional approach
- Document each approach with architecture diagrams

**Output**: 3-4 solution approaches with C4 diagrams

### 4. Trade-off Analysis ⏱️⏱️

**Architect 70%, LLM 30%**

- Architect evaluates approaches against business priorities
- LLM generates trade-off comparison matrix
- Identify risks and mitigation strategies per approach
- Architect makes final decision with documented justification

**Output**: Trade-off matrix + justified decision

### 5. Stakeholder Validation ⏱️⏱️

**Human 90%, LLM 10%**

- Present recommendation to Product Owner
- Discuss trade-offs, validate business alignment
- Revisions based on feedback (1-2 cycles may be needed)
- Formal final approval

**Output**: Approved Architecture Document

## Strategic Architecture Document Deliverable

**Length**: 2,000-4,000 words

**Sections**:
1. **Executive Summary** (~200 words): Problem + recommended solution
2. **Problem Definition**: Root cause analysis, success criteria
3. **Constraints**: Technical, organizational, timeline, budget
4. **Solution Approaches**: 2-4 approaches with C4 level 1-2 diagrams
5. **Trade-off Analysis**: Comparison matrix, risk evaluation
6. **Recommendation**: Chosen approach with explicit justification
7. **Success Metrics**: How to measure if solution succeeds
8. **Risk Mitigation**: Top 3-5 risks and strategies

## Definition of Done

This phase is considered complete when:

1. The business problem is clearly articulated with quantified success criteria
2. At least 3 ADRs (Architecture Decision Records) document major decisions
3. A high-level architecture diagram exists (C4 diagrams levels 1-2)
4. Critical technical constraints are identified and prioritized
5. The chosen solution includes clear justification of trade-offs vs. alternatives
6. Main architectural risks are documented with mitigation strategies
7. The Product Owner validates that the proposed solution meets business needs

---

<!-- ========================================= -->
<!-- LEVEL 4: MASTER (5-15 minutes)          -->
<!-- Detailed content hidden by default        -->
<!-- ========================================= -->

## Going Deeper

<details>
<summary><strong>See concrete examples, prompts and detailed ADRs</strong></summary>

### Complete Example: Nutritional Recommendation System

#### Business Context

A nutrition application wants to recommend foods based on user profile (allergies, preferences, health goals). Currently: static list by category. Goal: personalized real-time recommendations.

#### 1. Problem Crystallization

**Initial statement (vague)**:
"We want to improve food recommendations to make the app more useful."

**After crystallization with LLM**:

**Precise problem**:
Users abandon the app (Day-7 retention rate: 12%) because current recommendations don't account for their constraints (peanut allergies, vegetarian diet, weight loss goal). 35% of users report "irrelevant suggestions" in surveys.

**Root causes**:
- Current system: static if/then logic (120 lines of spaghetti code)
- No similarity consideration between foods
- No confidence score on recommendations
- No learning mechanism (user feedback ignored)

**Quantified success criteria**:
1. Day-7 retention rate: 12% → 25% (+108%)
2. Recommendation satisfaction: 2.1/5 → 4.0/5
3. API response time: < 200ms (95th percentile)
4. Allergy/restriction coverage: 100% (vs. 60% current)

#### 2. Constraint Mapping

**Mandatory technical constraints**:
- Backend: Python 3.11+ (existing stack)
- API latency: < 200ms p95 (UX critical)
- Database: PostgreSQL existing (migration forbidden due to cost)
- Volume: 50,000 active users, 10M foods in DB

**Organizational constraints**:
- Team: 2 backend developers, 1 frontend developer (no data scientist)
- Timeline: MVP in 6 weeks (business deadline)
- Infrastructure budget: +$500/month max
- No in-house ML/AI expertise

**Nice-to-have constraints**:
- Recommendation explainability (why this food?)
- Basic offline mode (cache recent recommendations)
- Multilingual support (FR/EN)

#### 3. Solution Generation

**Approach 1: Advanced Rules System (Architect)**

```
Architecture:
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

**Advantages**:
- Fully explicable (rules = justification)
- No ML expertise needed
- Predictable latency (< 50ms)

**Disadvantages**:
- Maintenance nightmare (500+ rules to maintain)
- No learning (user feedback lost)
- Limited scalability (rules explosion with complexity)

**Complexity**: Medium (simple implementation, high maintenance)
**Risks**: Major technical debt after 1 year

---

**Approach 2: Vector Search + Filtering (LLM - innovative)**

```
Architecture:
┌──────────────────┐
│  User Profile    │
│  embeddings      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────────┐
│  Vector Search   │      │  pgvector        │
│  (cosine sim)    │─────▶│  (PG extension)  │
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

**Advantages**:
- Semantic similarity (finds related foods)
- No rule maintenance (embeddings learned)
- Natural confidence scores (cosine distance)
- Uses existing PostgreSQL (pgvector extension)

**Disadvantages**:
- Embeddings to generate (initial cost)
- Reduced explainability (cosine distance ≠ business reason)
- Team must learn vector concepts

**Complexity**: Medium-High (technical novelty)
**Risks**: Team learning curve, embedding quality

---

**Approach 3: External ML API (LLM - alternative)**

```
Architecture:
┌──────────────────┐
│  User Profile    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────────┐
│  API Gateway     │      │  OpenAI API      │
│  (1h cache)      │─────▶│  (embeddings)    │
└────────┬─────────┘      └──────────────────┘
         │
         ▼
┌──────────────────┐
│  Post-processing │
│  (filters)       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Ranked Results  │
└──────────────────┘
```

**Advantages**:
- Zero in-house ML expertise needed
- Embedding quality guaranteed (OpenAI)
- Minimal maintenance

**Disadvantages**:
- Recurring cost (~$2000/month estimated)
- External dependency (API availability)
- Variable latency (network)
- User data sent externally (privacy concerns?)

**Complexity**: Low (simple API call)
**Risks**: Costs explode with volume, vendor lock-in

#### 4. Trade-off Analysis

**Comparison matrix**:

| Dimension | Advanced Rules | Vectors pgvector | External ML API |
|-----------|----------------|-------------------|-----------------|
| **Dev time** | 4 weeks | 5-6 weeks | 2-3 weeks |
| **Tech complexity** | 4/10 | 7/10 | 3/10 |
| **Maintainability** | 2/10 (rules explode) | 8/10 (auto-learning) | 9/10 (outsourced) |
| **Performance** | 9/10 (< 50ms) | 7/10 (< 150ms) | 5/10 (200ms+ network) |
| **Infrastructure cost** | $50/month | $200/month | $2000/month |
| **Risk** | High (tech debt) | Medium (learning curve) | Medium (dependency) |
| **Scalability** | Low | High | High |
| **Explainability** | 10/10 (clear rules) | 4/10 (cosine distance) | 3/10 (black box) |

**Recommendation: Approach 2 (pgvector Vectors)**

**Justification**:
1. **Respects budget constraints**: $200/month < $2000/month external API
2. **Long-term scalability**: Avoids technical debt from rules
3. **Uses existing stack**: pgvector = PostgreSQL extension (no migration)
4. **Acceptable timeline**: 5-6 weeks vs. 4 (manageable difference)
5. **Learning investment**: Team learns valuable skill (vectors = the future)

**Accepted trade-offs**:
- Technical complexity +30% vs. simple rules
- Reduced explainability (but confidence scores partially compensate)
- Team learning curve (mitigated by documentation + 2-day training)

**Rejected trade-offs**:
- External API: recurring costs 10x too high
- Advanced rules: unacceptable technical debt (explosive maintenance)

#### 5. Produced ADRs

**ADR-001: Use pgvector for Similarity Search**

**Status**: Accepted
**Date**: 2025-12-28
**Decision Makers**: Architect + Product Owner

**Context**:
Current recommendation system (static if/then rules) doesn't scale. Need semantic similarity between foods for relevant recommendations.

**Decision**:
Use pgvector extension in existing PostgreSQL for vector-based search with cosine similarity.

**Alternatives considered**:
1. **Advanced Rules System**: Rejected (explosive maintenance, not scalable)
2. **External ML API (OpenAI)**: Rejected (costs $2000/month too high)
3. **Dedicated vector database migration (Pinecone)**: Rejected (migration cost forbidden)

**Consequences**:
- Uses existing infrastructure (PostgreSQL)
- Acceptable infrastructure cost ($200/month)
- Semantic similarity without rule maintenance
- Team must learn embedding concepts (2-day training)
- Reduced explainability vs. rules (compensated by confidence scores)

---

**ADR-002: Generate Embeddings via Local sentence-transformers**

**Status**: Accepted
**Date**: 2025-12-28

**Context**:
Need to generate embeddings for 10M foods + user profiles. Choice: external API (OpenAI) vs. local model.

**Decision**:
Use `sentence-transformers` (model `all-MiniLM-L6-v2`) locally.

**Justification**:
- Zero cost after initial generation (vs. $2000/month API)
- Predictable latency (no network dependency)
- Privacy: data stays on-premise
- Performance sufficient (384 dimensions, quality acceptable for nutrition domain)

**Consequences**:
- Costs controlled long-term
- Stable latency (< 50ms embedding generation)
- Initial generation of 10M embeddings = 8h compute (one-time)
- Embedding quality lower than GPT-4 (acceptable for MVP)

---

**ADR-003: Hard Filtering of Allergies BEFORE Vector Search**

**Status**: Accepted
**Date**: 2025-12-28

**Context**:
Users with allergies (peanuts, gluten, lactose) MUST NEVER receive dangerous recommendations, even if vector similarity is high.

**Decision**:
Apply PostgreSQL allergy filters (WHERE clauses) BEFORE vector search. Safety > relevance.

**Justification**:
- Safety criticality: Allergen recommendation = health risk
- Performance: SQL filtering very fast (index)
- Certainty: Hard filters = 100% guarantee (vs. probabilistic ML)

**Consequences**:
- Allergy safety guaranteed
- Health regulatory compliance
- Reduced candidate pool (may impact diversity)
- Allergen list maintenance (DB table up-to-date)

### Recommended Prompts

#### Prompt 1: Problem Crystallization

```
I'm designing a solution for [business problem]. Here's the initial statement:

PROBLEM:
[paste vague/initial problem description]

CONTEXT:
- Users: [who]
- Current system: [how it works today]
- Main complaints: [user feedback]

Help me crystallize this problem by:

1. **Identify unstated assumptions**: What assumptions have I made
   that aren't explicit?

2. **Separate symptoms from root causes**:
   - Observed symptoms: [what users see]
   - Probable root causes: [why it happens]

3. **Suggest 3-5 QUANTITATIVE success criteria**:
   - Format: Current metric → Target metric (+% improvement)
   - Examples: "Day-7 retention rate: 12% → 25% (+108%)"

4. **Scope drift risks**: What aspects could dangerously expand
   the project?

Response format: Structured markdown with clear sections.
```

#### Prompt 2: Solution Generation

```
Given this problem definition and constraints:

PROBLEM:
[paste crystallized problem]

MANDATORY CONSTRAINTS:
- Technical: [ex: Python 3.11+, latency < 200ms, existing PostgreSQL]
- Organizational: [ex: team 3 devs, 6 weeks, no ML expertise]
- Budget: [ex: +$500/month infrastructure max]

BUSINESS PRIORITIES:
[ex: 1. User retention, 2. Time-to-market, 3. Operating costs]

I've identified this initial approach:

ARCHITECT APPROACH:
[paste initial solution 2-3 paragraphs]

Generate 2-3 ALTERNATIVE solution approaches that:
- Address the same problem differently
- Work within stated constraints
- **INCLUDE at least ONE innovative/unconventional approach**
- Are technically feasible for this context

For EACH solution, provide:

1. **Approach name** (short descriptive)
2. **High-level architecture**:
   - Main components (3-5 max)
   - Interactions between components (data flow)
   - Simple ASCII diagram
3. **Key advantages** (3-5 points)
4. **Key disadvantages** (3-5 points)
5. **Estimated complexity**: Low / Medium / High (justify)
6. **Main risks** (top 2-3 with impact)
7. **Dev time estimation**: X weeks (acceptable range)

Format: Markdown, one section per approach.
```

#### Prompt 3: Trade-off Analysis

```
Create a trade-off comparison matrix for these approaches:

SOLUTION APPROACHES:
[paste 3-4 previously generated approaches]

Compare along these dimensions (rate 1-10 or Low/Medium/High):

1. **Development time**: Weeks estimated
2. **Technical complexity**: 1-10 (1 = trivial, 10 = expert required)
3. **Maintainability**: Long-term maintenance cost (Low/Med/High)
4. **Performance**: Meets requirements? Estimated latency
5. **Risk level**: Low/Medium/High (technical + business)
6. **Organizational fit**: Team skills, culture
7. **Scalability**: Future growth (users, data)
8. **Infrastructure cost**: $/month estimated
9. **Explainability**: Can we explain results to users? (1-10)

For each dimension, briefly explain the rating (1-2 sentences).

Then RECOMMEND which approach best balances trade-offs
for this context:

BUSINESS PRIORITIES (in order of importance):
[paste priorities: ex: 1. Retention, 2. Time-to-market, 3. Costs]

NON-NEGOTIABLE CONSTRAINTS:
[paste hard constraints]

Recommendation format:
- **Recommended approach**: [which one]
- **Justification**: Why this approach (5-7 points)
- **Accepted trade-offs**: What we consciously sacrifice
- **Rejected trade-offs**: What we refuse to sacrifice
```

### Quality Standards

#### Good Architecture Document

**Characteristics**:
- **Quantified problem**: "Day-7 retention: 12%" not "poor retention"
- **3+ alternatives evaluated**: No single decision without comparison
- **Explicit trade-offs**: "We accept 30% complexity increase to avoid technical debt"
- **Concrete ADRs**: Documented decisions with rejected alternatives
- **Clear C4 diagrams**: Components + interactions visible
- **Formal PO validation**: Signature/explicit approval

**Example good documented decision**:
```
ADR-001: Use pgvector

Alternatives considered:
1. Advanced rules (rejected: technical debt)
2. OpenAI API (rejected: $2000/month)
3. Pinecone migration (rejected: migration cost)

Decision: pgvector
Justification: Balances cost/performance/maintenance
Accepted trade-off: 30% complexity increase, learning curve
Consequences: 2-day team training, embedding documentation
```

#### Bad Architecture Document

**Problems**:
- **Vague problem**: "Improve the app" without metrics
- **Single solution**: No evaluated alternatives
- **Technology bias**: "Let's use GraphQL" without justifying why
- **Hidden trade-offs**: Only benefits, no downsides
- **Ignored constraints**: Theoretically perfect solution, team can't execute it
- **No PO validation**: Architect decides alone

**Example bad decision**:
```
We'll use GraphQL.

[End. No alternatives, no why, no trade-offs]
```
→ Impossible to understand context or challenge the decision

### Common Pitfalls

#### 1. Single-Approach Analysis

**Problem**:
Architect evaluates only their preferred solution. No true alternatives. False impression of objective choice.

**Solution**:
- **Minimum 3 approaches**: Architect + 2 LLM alternatives
- **One "crazy" approach**: Forced innovative/unconventional
- **Honest evaluation**: Each approach has advantages AND disadvantages
- **Comparison matrix**: Impossible to bias if all dimensions listed

**DoD Check #5**: "Chosen solution includes justification vs. alternatives"

---

#### 2. Technology-First Thinking

**Problem**:
"Let's use Kubernetes!" before understanding the problem. Choosing tech stack before needs = guaranteed failure.

**Example**:
```
Architect: "We'll do microservices with Kubernetes"
Reality: 3 users/day, 1 team developer
→ Massive over-engineering
```

**Solution**:
- **Strict order**: Problem → Constraints → Solutions → Technologies
- **Tech justification**: Every technology choice must address a specific constraint
- **YAGNI**: "You Aren't Gonna Need It" - default to simplicity

**Good process**:
```
1. Problem: API latency > 500ms (frustrated users)
2. Constraint: Must pass < 200ms
3. Solution: In-memory cache
4. Technology: Redis (justified for speed)
```

---

#### 3. Ignoring Organizational Constraints

**Problem**:
Technically perfect solution design, but team can't execute it. Architecture requires ML expertise, team has zero experience.

**Real example**:
```
Architecture: Custom deep learning recommendation system
Actual team: 2 Python backend devs, zero ML
Timeline: 6 weeks
→ Impossible. Project fails.
```

**Solution**:
- **Skills mapping**: Who can actually do what
- **Learning budgeted**: If new technology, add training time
- **Realistic alternatives**: "Perfect solution impossible" → "Feasible good solution"

**DoD Check #4**: "Technical AND organizational constraints identified"

---

#### 4. Analysis Paralysis

**Problem**:
LLM generates 15 approaches. Architect spends 2 weeks analyzing all. Deadline explodes. Never decides.

**Solution**:
- **Strict limit: 3-4 approaches max**
- **Timeboxing**: Phase 1 = 1-2 days, not 2 weeks
- **"Good enough" > "Perfect"**: Aim for 80% certainty, not 100%
- **Decidable decision**: Better to decide fast and adjust than analyze forever

**Problem signal**: Phase 1 lasts > 3 days = analysis paralysis

---

#### 5. Vague Success Criteria

**Problem**:
"Improve performance", "increase user satisfaction". Impossible to measure success or failure.

**Vague examples**:
```
"Make the app faster"
"Increase quality"
"Improve user experience"
```

**Solution**:
- **Quantified metrics**: Precise numbers
- **Current baseline**: Where we start
- **Specific target**: Where we want to go
- **% improvement**: Magnitude of change

**Good examples**:
```
"Reduce p95 latency: 500ms → < 200ms (-60%)"
"Day-7 retention rate: 12% → 25% (+108%)"
"Satisfaction score: 2.1/5 → 4.0/5 (+90%)"
```

**DoD Check #1**: "Business problem with quantified success criteria"

---

#### 6. Missing Stakeholder Buy-in

**Problem**:
Architect decides architecture alone. Presents "fait accompli" to Product Owner. PO discovers solution misaligned with business priorities. Redoes Phase 1.

**Solution**:
- **PO involved from problem crystallization**: Validates success criteria
- **Collaborative trade-off review**: PO arbitrates conflicting priorities
- **Formal approval**: PO signs document before Phase 2
- **Feedback loops**: 1-2 revision cycles are normal

**DoD Check #7**: "Product Owner validates solution meets business needs"

### Standard ADR Format

**Reusable template**:

```markdown
# ADR-XXX: [Decision Title]

**Status**: [Proposed / Accepted / Rejected / Deprecated / Superseded]
**Date**: YYYY-MM-DD
**Decision Makers**: [Who decided]

## Context

[Why is this decision necessary? What problem does it solve?
2-4 paragraphs of business and technical context.]

## Decision

[What decision was made? Clear and concise statement. 1-2 paragraphs.]

## Alternatives Considered

### Alternative 1: [Name]
**Advantages**: [2-3 points]
**Disadvantages**: [2-3 points]
**Reason for rejection**: [Why not chosen]

### Alternative 2: [Name]
[Same structure]

## Justification

[Why this decision versus alternatives? Reference business priorities.
3-5 justified paragraphs.]

## Consequences

**Positive**:
- [Positive consequence 1]
- [Positive consequence 2]

**Negative / Accepted Trade-offs**:
- [Trade-off 1]
- [Trade-off 2]

**Required Actions**:
- [ ] [Action 1 to implement decision]
- [ ] [Action 2]

## References

- [Link to architecture document]
- [Link to Slack/email discussion]
- [Performance benchmark]
```

</details>

---

**Next step**: [Phase 2: Tactical Planning + Critical Handoff →](./phase2-planification-tactique)

**Need help?** See the [Roles and Responsibilities](./roles-et-responsabilites) document to clarify who does what in this phase.
