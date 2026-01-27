---
title: "Introduction to Development by Convergent Constraints"
description: "Master software development with AI through a structured methodology"
sidebar_position: 1
lang: en
---

# Master Software Development with AI

You've installed GitHub Copilot or Claude Code. The first few hours were magical: code wrote itself almost effortlessly. Three weeks later, you find yourself with duplicated functions, subtle bugs that pass tests but fail in production, and an architecture that looks like spaghetti code.

Even worse: during a code review, your team can no longer **justify its architectural choices**. *"Why this structure instead of another?"*

**You're not alone.**

**Development by Convergent Constraints (DC²)** is a structured software engineering methodology that enables you to harness the power of LLMs without compromising quality, maintainability, or your expertise. It's a return to software engineering fundamentals (documentation, TDD, collaborative refactoring) **optimized for the era of intelligent automation**.

**This methodology rests on solid theoretical foundations**: understanding the intrinsic limitations of LLMs, how Convergent Constraints guide their reasoning, and why Triple Inspection delivers 10-100x ROI on critical systems.

→ [**Explore the Theoretical Foundations**](/fondements-theoriques) to understand why DC² works

---

## Why DC2 Now? {#pourquoi-dc2}

### For Decision-Makers {#pour-decideurs}

Your teams use ChatGPT and GitHub Copilot. Initial velocity is impressive. But how can you ensure that generated code won't create **invisible technical debt** that will explode in 6-12 months?

**DC2 delivers the AI governance you're looking for**:
- **Continuous audit**: Optional Triple Inspection detects issues before production (10-100x ROI)
- **Measurable quality**: Exhaustive tests, up-to-date documentation, systematic refactoring
- **Preserved skills**: Teams progress instead of stagnating as passive verifiers
- **Sustained ROI**: Stable 3-5x acceleration over time (no -20%/year degradation)

AI is a lever. DC2 ensures it remains a **strategic asset**, not a **technical liability**.

---

### For Architects {#pour-architectes}

LLMs are **probabilistic, non-deterministic, opaque by construction** components. Their naive integration into critical systems creates invisible architectural risks.

**DC2 treats AI as a full-fledged architectural component**:

**Core principle**: *Externalize intelligence, internalize control*
- Intelligence can be probabilistic
- Control must never be

**Architectural mechanisms**:
- **Convergent constraints**: Specifications + tests + types guide the LLM toward a restricted solution space
- **External validation**: The LLM never validates its own output
- **External memory**: Documentation = source of truth (the LLM has no operational memory)
- **Explicit checkpoints**: Critical Transfer = human alignment before the first line of code

DC2 isn't "a dev method with LLMs" — it's an **integration framework for non-deterministic AI components**.

→ [**Read the Architectural Foundations**](/fondements-theoriques#ia-comme-composant) to understand the underlying pattern

---

### For Developers {#pour-developpeurs}

The LLM writes the code. You verify. Three months later, you realize: you're no longer progressing, you're **verifying**.

**The trap**: AI accelerates writing but erodes skills. Seniors become verifiers. Juniors are no longer engaged (they don't yet have the skills to judge generated code).

**DC2 restores learning through practice**:

**Structure before generation**:
- Phase 1-2: You design architecture and plan (65% human)
- Phase 3: You define ALL tests before code (with LLM assistant)
- Phase 4: LLM generates implementation (you supervise)
- **Phase 5: You refactor under senior guidance** (70% human)

**Result**:
- You **understand** the delivered code (not just verified)
- You **progress** in skills (guided collaborative refactoring)
- You **own** the system (collective ownership)
- You **accelerate** without sacrificing quality (sustained 3-5x)

The LLM is a **tactical accelerator**, not a substitute. You remain the architect of your code.

---

## The Problem Without Structure

LLMs generate code based on statistical patterns. They don't truly "understand"—they imitate what is statistically probable. Without a rigorous framework, you get:

- **Invisible duplication**: Two functions do the same thing with different names
- **Incoherent architecture**: Each component follows a different style depending on the LLM's mood
- **Subtle bugs**: Code passes basic tests but fails on forgotten edge cases
- **Explosive technical debt**: Invisible for 3-6 months, then unexpected major refactoring
- **Expertise erosion**: The team becomes a spectator rather than an actor, progressively losing the ability to solve complex problems without assistance

**Result**: You ship faster initially, then slow down dramatically when technical debt catches up with the team. Worse: your team no longer knows **why** the code works this way.

---

## The DC² Solution

DC² structures LLM adoption through 6 complementary phases where **humans maintain strategic control** and LLMs accelerate tactical execution.

### Founding Principles

**Documentation as the single source of truth**
Every architectural decision is explicitly documented. The LLM cannot improvise—it follows your detailed plan.

**TDD as the quality foundation**
Exhaustive tests are generated BEFORE any implementation. The LLM then generates code that MUST pass all these tests.

**Collaborative refactoring under expert guidance**
The development team transforms functional code into elegant code. **The team improves through practice**.

**Convergent Constraints**
The combination (tactical specifications + exhaustive tests + type hints) guides the LLM toward a restricted solution space where only correct implementations survive. The LLM then converges toward the most natural solution for the language used.

---

## The 6 Phases of DC²

![Diagram of the 6 phases](/img/overview_a.png)

### Phase 1: Strategic Architecture
**⏱️⏱️⏱️ | 65% Human / 35% LLM**

The architect and Product Owner define the architectural vision, document major decisions (ADR), and establish technical and business constraints. This phase creates the explicit "mental map" that the LLM naturally lacks.

### Phase 2: Tactical Plan + Critical Transfer
**⏱️⏱️ | 45% Human / 55% LLM**

The LLM generates a detailed implementation plan that the team reviews during **Critical Transfer**—the most important meeting in DC². The team actively challenges the plan, identifies risks, and validates feasibility before any coding begins.

**Link to Agile**: Equivalent to Story Refinement and Sprint Planning. A User Story becomes 3-5 components with exhaustive specifications.

### Phase 3: TDD RED - Test Generation
**⏱️ | 30% Human / 70% LLM**

The LLM generates an exhaustive test suite (95%+ coverage) BEFORE any implementation. These tests become the "rails" that guide the LLM in Phase 4 and prevent derailments.

### Phase 4: TDD GREEN - Implementation
**⏱️ | 25% Human / 75% LLM**

The LLM generates minimal code to pass all tests. Thanks to Convergent Constraints (specifications + tests + types), the code is correct on the first try in the majority of cases.

### Phase 5: REFACTOR - Collaborative Improvement
**⏱️⏱️⏱️ | 70% Human / 30% LLM**

The development team transforms functional code into production-quality code. The senior identifies opportunities, the team executes refactoring in parallel, the senior continuously reviews. **Improvement through practice, scalability, collective ownership.**

### Phase 6: Triple Inspection (Optional)
**⏱️ | 40% Human / 60% LLM**

For critical systems: three automated inspections detect future technical debt (Fagan), hidden weak tests (Tests), and multi-vector vulnerabilities (Security). An investment that prevents costly refactoring or incidents later.

---

## Why DC² Works

DC² doesn't fight LLM limitations—**it systematically compensates for them**:

- **No internal representation** → Phase 1 creates ADR + explicit schemas
- **No architectural understanding** → Phase 1 documents the why, not just the what
- **Forgets edge cases** → Phase 3 forces exhaustive tests including edge cases
- **No internal verification** → Phase 3-4: tests validate everything
- **"Average internet code"** → Phase 5: team transforms into production quality

**The result**: A methodology that produces superior code quality while training the team and maintaining high velocity over the long term.

---

## Who DC² Is For

**DC² is particularly suitable for**:
- Teams wanting to adopt LLMs without sacrificing quality
- Organizations where maintenance represents 80%+ of total cost
- Critical projects (finance, health, infrastructure)
- Teams wanting to train their developers, not replace them
- Long-lived systems (>2 years of planned evolution)

**DC² might not be suitable if**:
- You're building throwaway prototypes
- Short-term speed trumps everything
- You don't have access to an experienced architect or senior developer
- Your team resists structured processes

---

## Begin Your Adoption

**Two entry points depending on your needs**:

### You want to implement now
→ [**Start with Phase 1: Strategic Architecture**](/phase1-architecture-strategique)

### You want to understand why DC² works
→ [**Explore the Theoretical Foundations**](/fondements-theoriques)

---

**The methodology works with or without LLMs.** LLMs simply accelerate it 3 to 5 times.
