---
title: "Theoretical Foundations of Development by Convergent Constraints"
description: "Understanding the scientific principles that explain why DC² works"
sidebar_position: 9
lang: en
---

# Theoretical Foundations of Development by Convergent Constraints

Development by Convergent Constraints (DC²) is not a collection of "tips and tricks"—it is a structured engineering methodology grounded in an understanding of the capabilities and limitations of large language models. This document explores the theoretical foundations that explain why this approach works.

---

## Built on Proven Engineering Principles

DC² builds on engineering practices whose effectiveness has been demonstrated for decades. Some of these practices, previously deemed too expensive to apply systematically, have now become feasible through the automation enabled by LLMs.

### Fundamental Practices Reintegrated

**Architectural Documentation (ADR)**
Explicitly documenting major decisions and their justifications creates a durable knowledge base that survives team turnover.

**Test-Driven Development (TDD)**
Writing tests before code guarantees that every line has a reason for existing and verified behavior.

**Systematic Code Inspection**
Fagan inspection detected 60-90% of defects before production, but required 30 hours per component. LLMs reduce this time to 40 minutes (97% reduction), finally making the practice economically viable.

**Disciplined Refactoring**
Continuous improvement of code structure without changing its behavior, under expert guidance to maximize team learning.

### Automation Changes the Economic Equation

LLMs do not replace human expertise; they **accelerate tactical activities** that previously took too much time to be systematic:

- Exhaustive test generation: ⏱️⏱️⏱️ → ⏱️
- Complete Fagan inspection: ⏱️⏱️⏱️ → ⏱️
- Technical documentation: ⏱️⏱️⏱️ → ⏱️

**The result**: Practices once reserved for critical projects become applicable to all projects without compromising velocity.

---

### Principles in Detail

**Human Strategic Leadership**
Strategic phases (1-2) are directed by the architect and development team, clearly defining the problem, architecture, constraints, and design choices. The architect can be a solutions architect, technical analyst, tech lead, or senior developer with design talent.

**Documentation as Single Source of Truth**
Every tactical and strategic decision is recorded. The method produces an up-to-date documentation base that reduces dependence on tribal knowledge.

**TDD as Quality Foundation**
Tests are generated and verified before code is written, imposing clear and measurable expected behavior. These tests become the guidance system that orients the LLM and prevents drift.

**Collaborative Refactoring Under Expert Guidance**
The LLM proposes an initial functional implementation, then the development team, guided by a senior, transforms it into production-quality code: structured, clean, and conforming to engineering principles. It is not the senior doing all the work—it is the team improving itself through practice.

**Explicit Handoff Points**
The Critical Transfer between design and development is a formal review meeting, ensuring team alignment before the first line of code is written. This is the decisive moment where the architect's vision meets the team's reality.

**Systematic Triple Inspection (Optional)**
For critical or long-lived systems, each delivery can be audited for:

1. **Code (Fagan)**: Quality, maintainability, technical debt
2. **Tests**: Real semantic coverage versus empty metrics
3. **Security**: Multi-vector vulnerabilities, compliance

This optional phase enables a higher level of excellence. An investment that prevents hours of rework down the line. LLMs now make feasible inspection techniques that were previously too expensive.

**Explicit and Controlled Feedback Loop**
Tests, documentation, and inspections replace the LLM's "pseudo-intelligence" with a realistic and verifiable validation loop.

**Skill Building Rather Than Substitution**
The method places the development team, guided by senior expertise, at the center of critical phases. The team improves through practice, develops code ownership, and advances in competencies. The senior becomes a force multiplier rather than a bottleneck.

---

## AI as an Architectural Component, Not a Tool {#ia-comme-composant}

In DC², **the LLM is not considered a simple productivity tool**, but rather a **complete software component**, with properties fundamentally different from traditional deterministic systems.

### Properties of an LLM

An LLM is:
- **Probabilistic** — identical input ≠ identical output guaranteed
- **Non-deterministic** — variable behavior depending on context
- **Non-verifiable from within** — no introspection into its reasoning
- **Opaque by construction** — impossible to trace why a decision is made
- **Context-sensitive** — phrasing and information order drastically influence results
- **Evolving without direct control** — model change, version, or provider modification alters behavior

These characteristics make it a **risky architectural component** if naively integrated into a system.

### The Common Integration Mistake

The most common error is treating an LLM like a traditional library or deterministic microservice: direct invocation, implicit business logic, absence of formal contracts.

**The system works as long as everything is fine**, then becomes impossible to:
- Understand its behavior
- Audit its decisions
- Evolve without regression
- Debug when it fails

### Central Principle: Externalize Intelligence, Internalize Control

DC² is built on a simple but fundamental architectural principle:

> **Intelligence can be probabilistic. Control must never be.**

Concretely, this means:
- The LLM **does not decide** system invariants
- It **does not impose** implicit structure
- It **is never** a source of truth
- It **never validates** its own result

**Every interaction with an LLM is encapsulated by**:
- **Explicit contracts** (documentation, interfaces, types)
- **Verifiable constraints** (tests, business rules)
- **Validation points** human or automated

The LLM is treated as an **unreliable generative subsystem**, comparable to an external data source that contains noise. Useful, powerful, but structurally incapable of guaranteeing global system coherence.

### Beyond Development: A Generalizable AI Integration Pattern

DC² methodology is not limited to LLM-assisted development. **The same principles apply to integrating AI components in production**:

- **Documentation** plays the role of external memory, contract, and audit mechanism
- **Tests** define acceptable system behavior when facing AI
- **Inspections** replace implicit trust with systematic verification
- **Explicit handoff points** prevent AI from becoming an invisible dependency

**Whether it is**:
- A conversational agent
- An assisted decision engine
- A semantic enrichment pipeline
- An automated analysis component

**The same rules apply**: AI is integrated, bounded, and verified, never allowed to drift freely.

---

## 7 Structural Limitations of LLMs

### 1. No Internal Program Representation

The LLM does not build a logical tree, does not track internal system state, does not simulate execution, and does not analyze the consequences of its choices. Two generated functions can contradict each other without it "seeing" it.

**Concrete example**:
```python
# Function 1 generated
def calculate_total(items):
    return sum(item.price for item in items)

# Function 2 generated elsewhere
def calculate_total(items):
    total = 0
    for item in items:
        total += item.cost  # Uses 'cost' instead of 'price'
    return total
```

The LLM can generate these two functions in different files without "seeing" that they access different attributes (`price` vs `cost`), creating an invisible inconsistency that will explode in production.

**How DC² compensates**:
→ **Phase 1: Strategic Architecture** creates ADRs (Architecture Decision Records) and explicit schemas that document data structures, interfaces, and contracts. The LLM receives this explicit "mental map" instead of guessing.

### 2. No Understanding of Architectural Role

The model does not understand why an interface exists, why a layer must be isolated, or why a design pattern is used. It only reproduces frequent patterns, including bad ones.

**Concrete example**:
You ask the LLM to create an authentication module. It generates a working module, but mixes business logic, database access, and validation in a single monolithic 500-line class, simply because it is a statistically frequent pattern on the internet.

**How DC² compensates**:
→ **Phase 1** documents the **why**, not just the **what**. "We isolate authentication in a separate layer to enable future OAuth replacement without touching business code" becomes an explicit constraint the LLM must respect.

### 3. Difficulty with Complex Semantic Dependencies

When multiple modules interact, subtle relationships between invariants, contracts, and responsibilities are not captured. The LLM therefore easily generates locally plausible but globally incoherent code.

**Concrete example**:
Module A assumes user IDs are always > 0. Module B generates negative IDs for test users. The LLM generates both modules separately without seeing the invariant contradiction.

**How DC² compensates**:
→ **Phase 2: Tactical Plan** forces complete explicitation of interfaces, implementation sequences, and relationships between components. Semantic dependencies become documented constraints.

### 4. Weak Reliability on Edge Cases

Edge cases are not a strong statistical model: they appear rarely in training data. The LLM therefore tends to forget or superficially treat them.

**Concrete example**:
Division function generated by LLM:
```python
def divide(a, b):
    return a / b
```

The LLM systematically forgets: `b == 0`, `a` and `b` are `None`, `a` and `b` are strings, overflow if numbers are huge. These cases appear rarely in training code.

**How DC² compensates**:
→ **Phase 3: TDD RED** generates an exhaustive test suite BEFORE any implementation, systematically including all edge cases (null, empty, zero, negative, overflow). The LLM can no longer forget them; tests fail if absent.

### 5. No Operational Memory

The context window is not a reasoning space; it is only a range of visible text. The model maintains no stable trace between steps and can rewrite, undo, or contradict its own decisions.

**Concrete example**:
You ask the LLM to generate 5 consecutive modules. Between module 3 and module 4, it "forgets" that it had decided to use string IDs instead of int, and generates module 4 with int IDs. Invisible inconsistency.

**How DC² compensates**:
→ **Documentation = persistent external memory**. Every decision (Phase 1 ADR, Phase 2 Tactical Plan) is written and re-injected into each following prompt. The LLM does not need to "remember"; documentation remembers for it.

### 6. No Internal Verification

The LLM does not test its code, does not execute it, does not detect logical errors, and never validates whether a solution respects constraints defined elsewhere. All validation must come from the external methodological framework.

**Concrete example**:
LLM generates a function that should return a score between 0 and 1, but can return 1.5 if data is unexpected. The LLM does not "see" the error because it has no internal verification.

**How DC² compensates**:
→ **Phases 3-4: Tests validate everything**. Tests specify `assert 0.0 <= result <= 1.0`. If code violates this constraint, the test fails immediately. Validation is external and automatic.

### 7. Production of "Average Internet Code"

The model was trained on good and bad code. Without guardrails, it replicates questionable practices too: duplication, approximative error handling, unnecessary dependencies, SOLID violations, etc.

**Concrete example**:
LLM generates:
```python
try:
    result = risky_operation()
except:
    pass  # Error silently swallowed
```

Statistically frequent pattern on the internet (unfortunately), so reproduced.

**How DC² compensates**:
→ **Phase 5: Collaborative Refactoring**. The development team, guided by a senior, transforms functional code into production-quality code. Bad patterns are systematically identified and corrected.

---

## Result: A Method That Systematically Compensates

**DC² does not fight LLM limitations; it systematically compensates for them**:

| LLM Limitation | DC² Compensation |
|-----------|-------------------------|
| No internal representation | Phase 1: ADR + explicit schemas |
| No architectural understanding | Phase 1: Document the why, not just the what |
| Difficulty with complex dependencies | Phase 2: Force complete explicitation |
| No operational memory | Documentation = persistent external memory |
| Forgets edge cases | Phase 3: Exhaustive tests including edge cases |
| No internal verification | Phases 3-4: Tests validate everything |
| "Average internet code" | Phase 5: Team transforms to production quality |

LLMs excel at generating fast tactical fragments, but possess neither global understanding nor systemic reasoning. They imitate solutions that "look like good code," but have no way to guarantee that the code is coherent, robust, secure, or aligned with a given architecture.

**Hence the importance of a framework that centers humans in structural decisions and uses the LLM as an accelerator, not as a designer.**

---

## Converging Constraints: The Heart of DC²

**Converging Constraints** are the central mechanism that explains why DC² produces correct code on the first attempt in the majority of cases.

### The Concept

The combination (tactical specifications + exhaustive tests + type hints) guides the LLM toward a restricted solution space where only correct implementations remain. The LLM then converges to the most natural solution for the language used.

### Why It Works: Mathematical Reduction of Solution Space

**Without constraints**: Multitude of possible implementations
**+ Specifications (Phase 2)**: Reduction of plausible implementation space
**+ Tests (Phase 3)**: Only a few implementations pass
**+ Type hints**: 3-5 correct implementations

The LLM finds the solution among these remaining 3-5 options.

### Concrete Example: calculate_sum()

**Specification**: "Function that calculates the sum of a list of numbers"

**Tests**:
```python
assert calculate_sum([1, 2, 3]) == 6
assert calculate_sum([]) == 0
assert calculate_sum([-1, 1]) == 0
assert calculate_sum([1.5, 2.5]) == 4.0
```

**Type hints**:
```python
def calculate_sum(numbers: List[float]) -> float:
    ...
```

**Solution space reduced to 3 correct implementations**:
1. Loop: `for n in numbers: total += n`
2. Recursive: `numbers[0] + calculate_sum(numbers[1:])`
3. Built-in: `return sum(numbers)`

The LLM naturally chooses #3 (the most standard in Python).

### GPS Analogy

Converging Constraints work like GPS: they do not guide to ONE precise point, but to a zone of 3-5 meters around the address. **Sufficient to "find the door."**

---

## The Critical Transfer: The Most Important Meeting

The **Critical Transfer** (Phase 2B) is the decisive moment when the architect's vision meets the team's reality. It is a formal review meeting that detects and resolves misunderstandings BEFORE the first line of code is written.

### Why It's Critical

**Without Critical Transfer**:
The team begins coding with fragmented understanding of the architectural vision. Misunderstandings reveal themselves late (Phase 4-5), requiring costly and unexpected rework.

**With Critical Transfer**:
Shared and team-validated architectural vision. Architect-team alignment verified. Misunderstandings are detected and resolved in 90 minutes instead of 40 hours of rework.

### Typical Structure (90-120 minutes)

1. **Presentation (20 min)** - Architect presents vision
2. **Active Challenge (40-60 min)** - Team asks questions, identifies risks
3. **Collaborative Revision (20 min)** - LLM incorporates feedback
4. **Final Validation (10 min)** - Formal approval

### Red Flags of a Failed Transfer

- ❌ Silent team (no questions/concerns)
- ❌ Rubber-stamp approval without discussion
- ❌ Estimates diverging >50% between architect and team

**A passive team = major problem.** Silence is not approval; it is often unexpressed discomfort.

---

## Phase 5: Force Multiplier vs Bottleneck

### The Classic Anti-pattern (Solo Senior)

```
Senior does all refactoring alone
├─ Refactor component 1 (6h)
├─ Refactor component 2 (6h)
├─ Refactor component 3 (6h)
└─ Refactor component 4 (6h)
Total: 24h

Team waits, blocked
No learning
Senior exhausted
```

**Problem**: Senior = bottleneck. Not scalable. Team stagnates.

### The Pattern Suggested by DC² (Guided Team)

```
Senior identifies opportunities (2h)
├─ Dev 1: Refactor component 1 (6h parallel)
├─ Dev 2: Refactor component 2 (6h parallel)
└─ Dev 3: Refactor component 3 (6h parallel)
Senior continuously reviews (4h)
Total elapsed time: 12h

Team active, learning
Senior force multiplier
Scalable
```

**Transformation**: Senior does NOT do the work; he **guides the team executing it**. Learning through practice. Collective ownership.

---

## The Resurrection of Fagan: 1976 → 2026

Michael Fagan (IBM, 1976) developed revolutionary code inspection that detected 60-90% of defects before production with an ROI of 10-100x.
**Problem**: 30 hours per component, 2-4 hour meetings with 6-8 people. The method was abandoned in the 1990s as too expensive.

### Economic Transformation 2026

**Fagan 1976 (Human Alone)**:
30h inspection × $100/h = $3,000
Detects 10 defects × ROI 10x = $30,000 value
→ Positive ROI BUT impractical cost

**DC² Phase 6 2026 (LLM + Human)**:
40min inspection × $100/h = $67
Detects 10 defects × ROI 10x = $30,000 value
→ **450x ROI!** Finally practical!

### Why Now?

LLMs can exhaustively execute a Fagan inspection checklist without fatigue, cognitive bias, or memory lapses. What took 30h in 1976 takes 40 minutes in 2026.

**The best practices of the 1970s were CORRECT; they were simply impossible to apply without AI.**

### Phase 6: Triple Inspection (Optional)

For critical systems, Phase 6 offers three automated inspections:

1. **Fagan**: Code quality, maintainability, technical debt
2. **Tests**: Real semantic coverage (not empty metrics)
3. **Security**: 6 OWASP attack vectors

**4-6h investment prevents 40-80h rework + costly incidents.**

**When to do Phase 6**:
- Critical code (finance, health, infrastructure)
- Long lifespan (>2 years evolution)
- High cost of production bugs
- Strict regulatory compliance

---

## The Result: A Method That Produces Superior Code Quality

DC² does not promise "faster now"; it promises **"structured investment now, stable velocity forever"**.

**What you gain**:
- Production-quality code by Phase 5
- Team that improves in competencies (not regresses)
- Documentation automatically up-to-date
- Technical debt systematically avoided
- Stable long-term velocity (no -20%/year degradation)

**What you invest**:
- An initial learning curve (first feature)
- A steady pace thereafter (method once established)
- Methodological rigor (process discipline)

**The trade-off is clear**: Short-term investment for massive long-term benefits.

---

## Next Steps

**You now understand the theoretical foundations of DC².**

### You want to implement now
→ [**Start with Phase 1: Strategic Architecture**](./phase1-architecture-strategique)

### Back to introduction
→ [**Back to introduction**](./intro)

---

**The method works with or without LLMs.** LLMs simply accelerate it 3 to 5 times.
