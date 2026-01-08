---
title: "Phase 4: TDD GREEN - Guided Implementation"
description: "Implement code to pass the tests"
sidebar_position: 5
lang: en
---

# Phase 4: TDD GREEN—Minimal Implementation

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile: Implementation Sprint
  </span>
  <span style={{background: '#64748b', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Duration: 45 minutes
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Roles: Dev + LLM
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Human: 25%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM: 75%
  </span>
</div>

Phase 4 generates the minimal code to pass all tests. This is the phase where the "Spec Sandwich" shows its full power: with tactical specifications (Phase 2) AND complete tests (Phase 3), the LLM has such a precise constraint system that only one valid solution exists. The result: correct code on the first attempt in more than 90% of cases.

As we saw in the introduction, LLMs have no internal verification of code correctness. They generate code that "seems plausible" but cannot verify whether it actually works. Phase 4 solves this by providing immediate and exhaustive external verification: the test suite. Every line of generated code can be validated instantly against the tests. If the code does not pass the tests, the LLM knows immediately and can correct it. This rapid feedback loop transforms code generation from "educated guess" to "guided iterative validation."

Furthermore, LLMs lack operational memory between interactions. Without persistent context, they forget established constraints or previous decisions. Thanks to the "Spec Sandwich" (tactical specifications + tests + type hints), all constraints are present simultaneously in the Phase 4 prompt. The LLM does not have to "remember"—all necessary context is there. Tests define the WHAT (exact expected behavior), specs define the WHY (business context), and type hints define the HOW (data structures). This triple constraint reduces the space of possible solutions to essentially one correct implementation.

**The "90%+ on first attempt" phenomenon**: In measured practice, code generated in Phase 4 passes all tests on the first attempt in more than 90% of cases. This is not luck or magic—it is the mathematical result of the Spec Sandwich. When you give the LLM: (1) a precise specification of behavior, (2) 20+ tests defining exactly the expected inputs/outputs, and (3) type constraints, there remains only one way to implement that satisfies all these constraints. The LLM essentially solves a system of equations with a unique solution. The remaining 10% of failures are typically due to residual ambiguities in specs or untested edge cases—which are quickly identified and corrected.

Without this structured phase, traditional development requires 3-5 implementation-test-debug cycles. With the Spec Sandwich, one cycle suffices in 90%+ of cases. The debugging time is not "reduced"—it is "eliminated." This is the fundamental difference that enables moving from 6-12 hours to 45 minutes per component.

---

**Inputs**:

- RED state test suite (output from Phase 3)
- Tactical specifications for component behavior
- Interface definitions and type signatures
- Code quality standards (linting, type checking)

**Activities**:

1. **Minimal Code Generation** (LLM 80%, Senior Developer 20%)

    - LLM generates the simplest code to pass each test
    - Focus on correctness, not elegance
    - Acceptable: duplication, simple algorithms, basic structure
    - Senior developer validates that code matches specs

2. **Test Execution** (LLM 70%, Human 30%)

    - Run test suite (target: all tests pass)
    - Debug failing tests (rare with Spec Sandwich)
    - LLM fixes implementation bugs
    - Human validates that corrections do not break other tests

3. **Basic Quality Gates** (Human 50%, LLM 50%)

    - Run linter (fix style issues)
    - Run type checker (fix type errors)
    - Ensure code compiles/imports correctly
    - Senior developer approves GREEN state

**Definition of Done—Phase 4**:

This phase is considered complete when:

1. All Phase 3 tests pass at 100% (GREEN state verified)
2. Code passes linter without errors (warnings acceptable)
3. Code passes type checking (mypy, pyright, or equivalent)
4. Basic error handling is in place (no uncaught critical exceptions)
5. No critical security vulnerabilities (injection, basic XSS verified)
6. Code matches interface signatures specified in Phase 2
7. Developer approves code correctly implements tactical specifications

**Outputs**:

- Functional implementation (all tests pass)
- Code that respects basic quality standards (linting, type checks)
- Known limitations documented (will be addressed in REFACTOR)

**Validation Criteria**:

:::tip[Validation Criteria]
- All tests pass (100% success rate)
- No regressions (existing tests still pass)
- Code respects basic quality (linting, type checks)
- Implementation matches tactical specifications
- Error handling exists (even if basic)
- Senior developer confirms correctness
:::

**Time Estimation**:

- LLM code generation: 15-20 minutes (90%+ first attempt)
- Test execution + validation: 15-20 minutes
- Quality gate validation: 10-15 minutes
- **Total**: ~45 minutes per component (measured actual time)

**Prompt Examples**:

_Prompt 1—Minimal Implementation_:

```
Generate MINIMAL code to pass this test suite:
[paste RED state tests]

Requirements:
- Pass ALL tests with the simplest possible code
- DO NOT optimize or refactor yet (that comes in Phase 5)
- Acceptable: code duplication, simple algorithms, basic error handling
- Focus on CORRECTNESS, not elegance

Component specification:
[paste tactical spec]

Generate Python code with:
- Type hints for all functions
- Basic docstrings
- Simple and readable logic
- No premature abstractions

This is the GREEN phase—perfection comes later in REFACTOR.
```

_Prompt 2—Debug Failing Tests_:

```
These tests are failing:
[paste test failures]

Current implementation:
[paste code]

Fix the implementation to pass these tests. Maintain simplicity—do not over-engineer the solution. Show what changed and why.
```

**Acceptable in GREEN State**:

:::tip[Acceptable]
- **Code duplication**: Same logic in multiple places (extract in REFACTOR)
- **Simple algorithms**: O(n²) instead of O(n log n) (optimize in REFACTOR)
- **Basic error handling**: Simple try/except (improve in REFACTOR)
- **Minimal comments**: Code mostly self-explanatory
- **Direct structure**: No design patterns yet
- **Hardcoded values**: Some configuration hardcoded (externalize in REFACTOR)
:::

**Not Acceptable in GREEN State**:

:::danger[Not Acceptable]
- **Failing tests**: All tests must pass before moving to REFACTOR
- **Type errors**: Code must pass type checking
- **Critical security gaps**: SQL injection, XSS vulnerabilities (must be addressed)
- **Missing error handling**: Unhandled exceptions that crash the program
- **Silent failures**: Errors swallowed without logging
- **Broken interfaces**: Does not match interface signatures specified
:::

**Example Code in GREEN State**:

```python
def calculate_confidence(
    weighted_presence: float,
    total_similarity: float,
    n_contributors: int,
    top_k_similar: int
) -> float:
    """Calculate prediction confidence with sample size penalty.

    Simple implementation—will be refactored for clarity and performance.
    """
    if total_similarity > 0:
        confidence_raw = weighted_presence / total_similarity
        sample_size_penalty = min(n_contributors / top_k_similar, 1.0)

        # Additional penalty for very small samples
        if n_contributors < 3:
            statistical_penalty = 0.5 + (n_contributors / 6.0)
        else:
            statistical_penalty = 1.0

        return confidence_raw * sample_size_penalty * statistical_penalty
    return 0.0
```

**What is OK Here**:

- Direct if/else logic
- Simple arithmetic calculations
- Basic parameter validation
- All tests pass

**What Will Improve in REFACTOR**:

- Extract penalty calculations into separate functions
- Add detailed docstrings explaining formulas
- Improve variable naming
- Add logging for debugging

**Common Pitfalls**:

:::danger[Avoid]
- **Over-engineering**: Adding design patterns not yet needed
- **Premature optimization**: Optimizing before measuring performance
- **Skipping validation**: Moving to REFACTOR with failing tests
- **Scope creep**: Adding functionality not in the tactical plan
- **Perfectionism**: Spending hours polishing code that will be refactored anyway
:::
