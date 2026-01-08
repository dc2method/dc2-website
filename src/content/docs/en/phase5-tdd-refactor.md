---
title: "Phase 5: TDD REFACTOR - Continuous Quality"
description: "Improve code quality without changing behavior"
sidebar_position: 6
lang: en
---

# Phase 5: TDD REFACTOR—Production Quality

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile: Code Review + Refactoring
  </span>
  <span style={{background: '#64748b', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Duration: 6-12 hours
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Roles: Dev Team (guided by Senior)
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Human: 70%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM: 30%
  </span>
</div>

Phase 5 transforms the functional GREEN state code into production-grade implementation. The development team, guided by an experienced senior engineer, applies software craftsmanship principles to improve architectural clarity, optimize performance, and ensure long-term maintainability. This is the phase where collective human expertise transforms "it works" into "it's excellent."

As we saw in the introduction, LLMs produce "average internet code"—functional but generic solutions that reflect the most common patterns found online. This code works but often lacks architectural elegance, context-specific optimizations, and maintainability considerations specific to your system. Phase 5 solves this by applying collective human expertise: the team knows your architecture, your quality standards, your performance constraints, and your future maintainability needs. The senior guides the team in identifying and applying patterns appropriate for your specific context.

Without this phase, code remains at "average internet" level: functional but not optimal, with duplication, suboptimal algorithms, and structure that erodes over time. Refactoring becomes technical debt that accumulates. With Phase 5, this debt is systematically eliminated before merge. The 6-12 hour investment in Phase 5 avoids 40+ hours of future rework and maintains stable velocity long-term.

**Why the team, not senior solo**: Phase 5 led by the team (rather than senior alone) creates several critical advantages. The team develops refactoring skills through guided practice rather than passive observation. The senior becomes a force multiplier by guiding multiple developers simultaneously rather than a bottleneck doing everything alone. The team develops strong code ownership through collective refinement. And crucially, it scales: multiple components can be refactored in parallel by different team members under senior supervision, rather than one component at a time by the senior.

---

**Inputs**:

- GREEN state implementation (output from Phase 4)
- Passing test suite
- Quality standards (complexity limits, coupling metrics)
- Performance requirements (latency, throughput, memory)

**Activities**:

1. **Identify Refactoring Opportunities** (Team 60%, Senior 40%)

    - Team reviews GREEN state code collectively
    - Identify code smells (duplication, long functions, deep nesting)
    - Identify performance bottlenecks (profiling)
    - Senior guides analysis and prioritizes improvements
    - Collective review of architectural patterns to apply

2. **Apply Architectural Patterns** (Team 70%, Senior 30%)

    - Senior recommends appropriate design patterns
    - Team applies patterns under guidance
    - Extract functions/classes for Single Responsibility
    - Apply dependency inversion if necessary
    - LLM assists with mechanical code transformation
    - Senior validates correct pattern application

3. **Performance Optimization** (Team 75%, Senior 25%)

    - Team profiles code, identifies hot spots
    - Senior guides algorithm selection (O(n²) → O(n log n))
    - Team implements caching if beneficial
    - Optimize database queries, API calls
    - LLM generates optimized code under team direction

4. **Documentation Enhancement** (Team 40%, LLM 60%)

    - Team defines what requires documentation
    - LLM generates detailed docstrings
    - Team adds inline comments for complex logic
    - LLM updates README, architecture docs
    - Senior reviews documentation quality

5. **Quality Validation** (Team 50%, Senior 50%)

    - Run all tests (must still pass 100%)
    - Run quality metrics (complexity, coupling)
    - Performance benchmarking
    - Code review by team with senior approval

**Definition of Done—Phase 5**:

This phase is considered complete when:

1. All Phase 3 tests still pass at 100% (no regressions introduced)
2. Cyclomatic complexity reduced to < 10 per function
3. Code duplication eliminated (DRY principle applied)
4. Performance benchmarks met or exceeded (if specified)
5. SOLID principles applied where appropriate
6. Documentation complete (docstrings, inline comments, architecture)
7. Senior approves code as production-ready

**Outputs**:

- Production-grade code meeting all quality standards
- Improved architectural clarity
- Optimized performance (benchmarks documented)
- Complete documentation

**Validation Criteria**:

:::tip[Validation Criteria]
- All tests still pass (100%—no regressions)
- Cyclomatic complexity reduced (target: < 10 per function)
- Code duplication eliminated (DRY principle)
- Performance benchmarks met or exceeded
- SOLID principles applied where appropriate
- Documentation complete and accurate
- Senior approves for production
:::

**Time Estimation**:

- Refactoring: 6-12 hours per component
- Performance optimization: 2-4 hours
- Documentation: 2-3 hours
- Quality validation: 2-3 hours
- **Total**: 12-22 hours per component

**Example Workflow (GREEN → REFACTOR)**:

_GREEN State_ (from Phase 4):

```python
def calculate_confidence(weighted_presence, total_similarity, n_contributors, top_k_similar):
    if total_similarity > 0:
        confidence_raw = weighted_presence / total_similarity
        sample_size_penalty = min(n_contributors / top_k_similar, 1.0)
        if n_contributors < 3:
            statistical_penalty = 0.5 + (n_contributors / 6.0)
        else:
            statistical_penalty = 1.0
        return confidence_raw * sample_size_penalty * statistical_penalty
    return 0.0
```

_Team Identifies Improvements (guided by Senior)_:

1. Extract penalty calculations (Single Responsibility)
2. Add type hints (mypy compliance)
3. Add detailed docstrings (explain formulas)
4. Add logging (support debugging)

_REFACTOR State_ (Production):

```python
import logging
from typing import float

logger = logging.getLogger(__name__)

def calculate_confidence(
    weighted_presence: float,
    total_similarity: float,
    n_contributors: int,
    top_k_similar: int
) -> float:
    """Calculate prediction confidence with sample size and statistical penalties.

    Applies two penalties to reduce overconfidence in predictions:
    1. Sample size penalty: Reduces confidence when n_contributors < top_k_similar
    2. Statistical penalty: Additional reduction for very small samples (n < 3)

    Args:
        weighted_presence: Sum of (similarity * a_composed) across contributors
        total_similarity: Sum of similarity scores for all contributors
        n_contributors: Number of foods that contributed to the prediction
        top_k_similar: Target number of similar foods (typically 5)

    Returns:
        Confidence score in [0, 1], penalized for small sample sizes

    Example:
        >>> calculate_confidence(1.0, 1.0, 2, 5)
        0.33  # Penalized: only 2/5 contributors, n < 3
    """
    if total_similarity <= 0:
        logger.warning("total_similarity is zero or negative, returning confidence 0")
        return 0.0

    confidence_raw = weighted_presence / total_similarity
    sample_penalty = _calculate_sample_penalty(n_contributors, top_k_similar)
    stat_penalty = _calculate_statistical_penalty(n_contributors)

    final_confidence = confidence_raw * sample_penalty * stat_penalty

    logger.debug(
        f"Confidence calculation: raw={confidence_raw:.3f}, "
        f"sample_penalty={sample_penalty:.3f}, stat_penalty={stat_penalty:.3f}, "
        f"final={final_confidence:.3f}"
    )

    return final_confidence


def _calculate_sample_penalty(n_contributors: int, top_k: int) -> float:
    """Calculate penalty based on contributor/target ratio.

    Returns 1.0 when n_contributors >= top_k (no penalty).
    Returns n_contributors/top_k when fewer contributors (linear penalty).
    """
    return min(n_contributors / top_k, 1.0)


def _calculate_statistical_penalty(n_contributors: int) -> float:
    """Calculate additional penalty for very small samples.

    For n >= 3: No penalty (returns 1.0)
    For n < 3: Linear penalty from 0.5 (n=0) to 0.833 (n=2)

    This addresses statistical instability with < 3 data points.
    """
    if n_contributors < 3:
        return 0.5 + (n_contributors / 6.0)
    return 1.0
```

**Value Added by Team (guided by Senior)**:

- Extraction of two functions (Single Responsibility Principle)
- Addition of complete docstrings with formulas explained
- Addition of logging for debugging
- Improved error handling (warning on invalid input)
- Addition of type hints everywhere
- Better variable naming (`stat_penalty` vs `statistical_penalty`)

**Quality Checklist**:

:::tip[Quality Criteria]
- **SOLID Principles**: Single Responsibility (focused functions), Open/Closed (extensible)
- **DRY**: No code duplication
- **Performance**: O(1) complexity maintained
- **Documentation**: Complete docstrings, inline comments for complex logic
- **Error Handling**: Validates inputs, logs warnings
- **Testability**: Pure functions, easy to test
- **Maintainability**: Future developers can easily understand and modify
:::

**Common Pitfalls**:

:::danger[Avoid]
- **Over-refactoring**: Abstract too much, lose clarity
- **Breaking tests**: Refactoring changes behavior, tests fail
- **Premature abstraction**: Create patterns not yet needed
- **Obscuring business logic**: Refactoring hides what code does
- **Ignoring performance**: Code is beautiful but slow
- **Endless refactoring**: Refactor indefinitely instead of delivering
- **Senior does everything**: Team passive, loses learning opportunity
:::
