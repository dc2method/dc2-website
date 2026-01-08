---
sidebar_position: 4
---

# Phase 3: TDD RED—Test Generation

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile: Test-First Development
  </span>
  <span style={{background: '#64748b', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Duration: 1.5 hours
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Roles: Senior Dev + LLM
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Human: 30%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM: 70%
  </span>
</div>

Phase 3 generates the complete test suite BEFORE any implementation. These tests become the executable specification of expected behavior and serve as a guidance system for the LLM in Phase 4. This is the phase where vague intentions transform into precise and verifiable expectations.

As we saw in the introduction, LLMs lack an internal representation of the program. In Phase 3, tests create this representation as executable specifications. Each test precisely defines expected behavior with concrete inputs and outputs. The LLM no longer guesses "what should this function do"—the tests declare it explicitly with verifiable examples.

Furthermore, LLMs have low reliability on edge cases and error conditions. They tend to implement the "happy path" and forget validations, extreme cases, or error scenarios. Phase 3 forces systematic articulation of all these cases before coding. Each edge case (null value, empty list, division by zero, limit exceeded) becomes a test that MUST pass, eliminating the possibility that the LLM forgets it in Phase 4.

**Tests as a guidance system**: In Phase 4, the LLM receives the tactical specifications AND the complete test suite. Tests become "rails" that guide implementation and prevent derailments. If the LLM begins implementing an approach that would not satisfy the tests, it can detect this immediately and adjust. It is like driving with GPS: tests continuously indicate whether you are on the right road or drifting from your destination. This additional constraint drastically reduces the space of possible solutions and increases the probability that the generated code is correct on the first attempt.

Without this phase, the LLM in Phase 4 codes based solely on textual specifications (ambiguous). Edge case oversights, subtle misunderstandings, and incorrect assumptions are discovered only in integration tests or production. With Phase 3, these problems are impossible—the code does not pass the tests if it is not correct.

---

**Inputs**:

- Tactical Implementation Plan (output from Phase 2)
- Code structure and interface definitions
- Quality standards (coverage targets, naming conventions)
- Test framework and tools (pytest, unittest, etc.)

**Activities**:

1. **Test Suite Generation** (LLM 85%, Senior Developer 15%)

    - LLM generates comprehensive test cases from the tactical plan
    - Unit tests for each component/function
    - Integration tests for component interactions
    - Edge cases and error conditions
    - Senior developer validates test completeness

2. **Coverage Validation** (Human 40%, LLM 60%)

    - Run coverage analysis (target: 95%+)
    - Identify gaps in test coverage
    - LLM generates additional tests for uncovered paths
    - Senior developer validates that edge cases align with business logic

3. **RED State Verification** (Human 90%, LLM 10%)

    - Run test suite (all tests must fail)
    - Verify tests fail for correct reasons (NotImplementedError, missing code)
    - Ensure there are no false positives (tests passing without implementation)
    - Commit test suite in RED state

**Definition of Done—Phase 3**:

This phase is considered complete when:

1. A complete test suite covers ≥95% of planned code paths
2. All tests are in RED state (fail as expected, no false positives)
3. Critical edge cases are covered (null values, empty lists, overflows, errors)
4. Tests follow naming conventions (describe expected behavior)
5. Each test has a clear assertion that validates a specific behavior
6. Test fixtures are in place for reusable setup/teardown
7. Senior developer approves the quality and completeness of the test suite

**Outputs**:

- Complete test suite (failing)
- Test coverage report (target 95%+ coverage)
- Test documentation (what each test validates)

**Validation Criteria**:

:::tip[Validation Criteria]
- All tests fail initially (RED state verified)
- Test coverage ≥95% of planned code
- Edge cases and error conditions covered
- Tests are clear and well-named (describe expected behavior)
- No brittle tests (tightly coupled to implementation details)
- Senior developer approves test quality
:::

**Time Estimation**:

- LLM test generation: 45-60 minutes per component
- Coverage validation: 20-30 minutes
- RED state verification: 15 minutes
- **Total**: ~1.5 hours per component (measured actual time)

**Prompt Examples**:

_Prompt 1—Initial Test Generation_:

```
Generate a complete test suite for this component:
[paste component specification from tactical plan]

Requirements:
- Target: 95%+ code coverage
- Test framework: pytest
- Include:
  - Unit tests for each public method
  - Edge cases (empty inputs, boundary values, null/None)
  - Error conditions (invalid inputs, exceptions)
  - Integration tests (if component interacts with others)
- Naming convention: test_<method>_<scenario>_<expected_result>
- Use test fixtures for reusable setup/teardown
- All tests must fail initially (no implementation yet)

Format as Python code with clear docstrings explaining what each test validates.
```

_Prompt 2—Edge Case Generation_:

```
Revise this test suite for missing edge cases:
[paste generated tests]

Component specification:
[paste component spec]

Identify missing test cases for:
1. Boundary values (min/max, zero, negative)
2. Empty or null inputs
3. Invalid input types
4. Concurrent access scenarios (if applicable)
5. Resource exhaustion (large datasets, memory limits)
6. Error recovery (what happens after exceptions)

Generate additional tests for each identified gap.
```

**Quality Standards**:

**Test Naming**:

```python
# GOOD: Describes behavior and expected result
def test_calculate_confidence_with_zero_contributors_returns_zero()
def test_calculate_confidence_with_small_sample_applies_penalty()

# BAD: Vague or focused on implementation
def test_calculate_confidence()
def test_function1()
```

**Assertion Clarity**:

```python
# GOOD: Clear assertion with context
result = calculate_confidence(weighted_presence=1.0, total_similarity=1.0,
                               n_contributors=2, top_k=5)
assert result == pytest.approx(0.33, rel=0.01), \
    "Confidence should be penalized for small sample (2/5 contributors)"

# BAD: Unclear assertion
assert result == 0.33
```

**Setup/Teardown Patterns**:

```python
# Use test fixtures for reusable setup
@pytest.fixture
def sample_data():
    return {"food": "Peppermint", "compounds": [6022, 6134, 6138]}

def test_with_fixture(sample_data):
    result = process_food(sample_data)
    assert result is not None
```

**Common Pitfalls**:

:::danger[Avoid]
- **Tests pass immediately**: Implementation already exists (not RED state)
- **Insufficient edge cases**: Only happy path tested, missing error conditions
- **Brittle tests**: Tests break when implementation details change
- **Unclear test names**: Impossible to tell what test validates from the name
- **Missing assertions**: Test runs but does not validate behavior
- **Over-mocking**: Mocks hide integration problems
:::
