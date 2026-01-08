---
title: "Phase 6: Triple Inspection - Multi-Perspective Validation"
description: "Technical, business and content inspection for quality assurance"
sidebar_position: 7
lang: en
---

# Phase 6: Triple Inspection

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#f59e0b', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Status: OPTIONAL (recommended for critical systems)
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile: Definition of Done / Quality Gates
  </span>
  <span style={{background: '#64748b', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Duration: 4-6 hours
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Roles: Team validates (3 LLM inspections)
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Human: 40%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM: 60%
  </span>
</div>

Phase 6 executes three specialized inspections to detect invisible defects and future technical debt before they become costly. This phase embodies the philosophy "invest 4-6 hours now to avoid 40-80 hours of rework later." The three LLM-automated inspections detect maintainability-risk patterns that the human eye systematically misses.

As we saw in the introduction, LLMs produce "average internet code"—functional but with subtle patterns that will cause problems 6-12 months later. Phase 6 solves this by applying three complementary inspection perspectives: (1) Fagan Inspection detects architectural technical debt, (2) Tests Inspection reveals false confidence from empty coverage metrics, and (3) Security Inspection finds multi-vector vulnerabilities invisible to humans alone. Together, these three inspections create an exhaustive assessment of real code quality.

**The Fagan resurrection**: Fagan Inspection, developed by Michael Fagan at IBM in 1976, was revolutionary—capable of detecting 60-90% of defects before production with 10-100x ROI. But it was impractical: 30 hours per component (2-4 hour meeting + 2 hours preparation × 6-8 people). The industry abandoned it in the 1990s as too expensive. LLMs change everything: what took 30 hours in 1976 now takes 10 minutes of LLM generation + 30 minutes of human validation. Structured LLM resurrects a proven technique by finally making it practical. The best practices of the 1970s were correct—they were just impossible to apply at the time.

**The danger of weak tests**: A test suite with 95% coverage creates a false sense of security if the tests are low quality. Tests that verify `assert result is not None` instead of validating actual values, tests coupled to implementation details that break with minor refactoring, tests ignoring critical edge cases—all create a reassuring metric but do not protect against bugs. The Tests Inspection reveals this illusion: it distinguishes "code coverage" (executed lines) from "semantic coverage" (validated business behaviors). A weak test suite costs more than it returns: constant maintenance, false positives that erode confidence, and bugs that pass despite "95% coverage."

**The economics of security**: Fixing a vulnerability in production costs 30-100x more than in development. A SQL injection detected in Phase 6 takes 15 minutes to fix. The same vulnerability discovered after deployment requires: incident response, emergency patch, complete audit, customer notification, reputational costs. Security Inspection detects the six major attack vectors (injection, authentication, sensitive data, infrastructure, business logic, monitoring) before merge. It is preventive quality assurance: the inspection cost (1-2h) is negligible compared to the cost of a single production vulnerability.

Without this phase, code enters production with latent defects that silently accumulate. Six months later, the team faces major rework because technical debt has become unmanageable, tests constantly break, and a critical vulnerability forces an emergency patch. Phase 6 transforms these unpredictable future costs into predictable and controlled investment.

**Status: OPTIONAL** (recommended for critical systems)

After Phase 5 (team-led refactoring), your code is already acceptable production quality. Phase 6 is NOT a mandatory quality gate—it is a **preventive excellence opportunity**. Invest 4-6 hours now to avoid 40-80 hours of future rework and costly production incidents.

**When to do Phase 6**:
- Critical code (finance, healthcare, infrastructure)
- Long lifespan (>2 years planned evolution)
- High production bug cost (reputation, money, security)
- Strict regulatory compliance

**When you might skip Phase 6**:
- Prototypes, POCs, throwaway code
- Simple components, low business criticality
- Very senior team with already excellent standards
- Justified tight time constraints

## 🚀 The Advantage of LLM-Based Inspection

**LLM-based code inspection is not a compromise—it is a strategic advantage.**

LLMs possess inspection capabilities that **exceed human capabilities** in critical dimensions:

### 1. Exhaustiveness Without Fatigue

**Human**:
- Begins rigorous, fatigues after 30 minutes
- Loses concentration, skims repetitive patterns
- Forgets checklist items under pressure
- Verifies perhaps 30% of rules in practice

**LLM**:
- Identical rigor from first to last item
- Verifies 100% of checklist systematically
- No cognitive fatigue, no forgetfulness
- Applies same standards to 1st and 100th test

**Concrete example**: A suite of 200 tests. Humans will inspect the first 20 deeply, skim the next 50, and quickly scan the last 130. LLM analyzes all 200 with identical rigor.

### 2. No Cognitive Bias

**Human**:
- Confirmation bias: seeks what confirms hypotheses
- Anchoring bias: influenced by first impression
- Authority bias: hesitates to criticize senior code
- Decision fatigue: standards erode over time

**LLM**:
- Evaluates each pattern objectively
- No emotional attachment to code
- Critiques CTO code like junior code
- Constant standards independent of context

**Concrete example**: A senior wrote complex code. Humans hesitate to flag excessive complexity. LLM objectively reports "cyclomatic complexity 15 (threshold: 10)."

### 3. Perfect Memory of Standards

**Human**:
- Remembers common patterns
- Forgets rare but critical rules
- Standards evolve in their head over time
- Subjective interpretation of guidelines

**LLM**:
- Applies 100% of defined rules
- Rare patterns verified with same care as common ones
- Constant and reproducible standards
- Zero interpretation drift

**Concrete example**: An obscure security rule about chemical IDs. Humans probably will not remember it. LLM checks it systematically if in the checklist.

### 4. Expertise Scalability

**Human**:
- Expert senior limited to 1-2 inspections/day
- Organizational bottleneck
- High cost per inspection
- Impossible to parallelize

**LLM**:
- Same expertise applied to 10 components simultaneously
- No bottleneck
- Marginal cost near-zero after setup
- Trivial parallelization

**Concrete example**: 10 components to inspect. An experienced senior would take 2 weeks (1-2 days per component). LLM inspects all in 2 hours (parallel), with human validation 4-6h.

### 5. Automatic Continuous Improvement

**Human**:
- Slow learning of new patterns
- Expensive continuous training
- Informal knowledge sharing
- Standards diverge between reviewers

**LLM**:
- Checklist updated instantly for everyone
- New patterns added without retraining
- Perfectly consistent standards
- Collective improvement immediate

**Concrete example**: A new OWASP vulnerability discovered. Adding the rule to checklist takes 10 minutes, and all future inspections check it automatically. Training all developers would take weeks.

### What Humans Do Better

LLM inspection does not replace humans—it transforms their role:

**LLM = Systematic Inspector**
- Exhaustive checklist execution
- Technical pattern detection
- 100% rule coverage

**Human = Strategic Decider**
- Prioritize findings (CRITICAL vs IMPROVEMENT)
- Evaluate business impact
- Contextual decisions (fix/defer/accept)
- Define new standards

### The Perfect Combination

```
Fagan Inspection 1976 (human alone):
├─ Exhaustive but too expensive (30h)
└─ Abandoned by industry

Automated Inspection 2000s (scripts):
├─ Fast but superficial
└─ Missing business context

LLM Inspection 2024 (hybrid):
├─ Fagan exhaustiveness + Automation speed
├─ Business context + Human judgment
└─ Practical and economical (40min)
```

**Phase 6 is not a compromise—it is the best inspection available.**

The 3 inspections (Fagan, Tests, Security) exploit these LLM advantages while preserving human judgment where it is irreplaceable. The result: inspection quality superior to what a human alone could achieve, at a fraction of the cost.

---

**Inputs**:

- REFACTOR state code (output from Phase 5)
- Complete test suite with results
- Requirements documents (strategic architecture, tactical plan)
- Quality standards and benchmarks

## The 3 Specialized Inspections

### 1. Fagan Inspection—Code Quality & Maintainability

**Objective**: Detect future technical debt and maintainability-risk patterns before they become expensive.

**Focus**: Multi-perspective code evaluation across 5 critical dimensions.

**Duration**: 10 minutes LLM generation + 30 minutes human validation

**Target score**: ≥ 80/100

**Evaluated dimensions**:

1. **Simplicity** (20 points)
   - Clear code, no over-engineering
   - Appropriate abstractions for the problem
   - Cyclomatic complexity < 10 per function

2. **Business Logic** (20 points)
   - Explicit domain names
   - Clear and documented business rules
   - Contextual error handling

3. **Robustness** (20 points)
   - Complete edge case handling
   - Exhaustive input validation
   - Graceful error recovery

4. **Maintainability** (20 points)
   - Future evolution facilitated
   - Minimal coupling
   - Appropriate documentation

5. **Performance** (20 points)
   - Validated scalability
   - Appropriate optimizations
   - No obvious bottlenecks

**Example Fagan Inspection Prompt**:

```
Perform a systematic Fagan inspection of this code across 5 perspectives:

CODE TO INSPECT:
[paste REFACTOR state code]

SPECIFICATIONS:
[paste tactical spec]

EVALUATE EACH DIMENSION /20:

1. SIMPLICITY (/20)
   - Is code clear and direct?
   - Appropriate abstractions (no over-engineering)?
   - Acceptable cyclomatic complexity?
   - Identify overly complex patterns

2. BUSINESS LOGIC (/20)
   - Do names reflect the domain?
   - Are business rules explicit and documented?
   - Contextual error handling?
   - Identify obscure logic

3. ROBUSTNESS (/20)
   - Are edge cases handled (null, empty, boundary)?
   - Complete input validation?
   - Graceful error recovery?
   - Identify uncovered scenarios

4. MAINTAINABILITY (/20)
   - Is future evolution facilitated?
   - Minimal coupling?
   - Sufficient documentation?
   - Identify future technical debt

5. PERFORMANCE (/20)
   - Appropriate algorithmic complexity?
   - Validated scalability?
   - Performance bottlenecks?
   - Identify performance risks

REPORT FORMAT:
- Total score: /100
- Score per dimension with justification
- Top 3 risks detected (CRITICAL/IMPORTANT/IMPROVEMENT)
- Specific recommendations with code examples
```

**Example Fagan Report**:

```markdown
# Fagan Inspection—calculate_confidence()

## Overall Score: 82/100

### Scores by Dimension
- Simplicity: 18/20 — Clear code, appropriate function extraction
- Business Logic: 15/20 — Good naming but formulas under-documented
- Robustness: 17/20 — Edge cases covered, validation present
- Maintainability: 16/20 — Evolution facilitated, minimal coupling
- Performance: 16/20 — O(1) maintained, no bottlenecks

## Detected Risks

### IMPORTANT
- **Mathematical formulas under-documented**: Penalty calculations
  (0.5 + n/6.0) lack business justification. Add references to
  statistical studies or business decisions motivating these values.

### IMPROVEMENT
- **DEBUG logging level**: For production, consider configurable
  level to avoid excessive verbosity in production.
```

### 2. Tests Inspection—Test Suite Effectiveness

**Objective**: Distinguish real business coverage from empty coverage metrics that create false confidence.

**Focus**: Real test quality vs superficial metrics.

**Duration**: 10 minutes LLM generation + 30 minutes human validation

**Target score**: ≥ 80/100

**Evaluated dimensions**:

1. **Semantic Coverage** (20 points)
   - Tests validate business behavior, not just execution
   - Critical scenarios covered
   - Complete user flows tested

2. **Assertion Quality** (20 points)
   - Specific assertions, not generic
   - Explicit expected values
   - Clear error messages

3. **Test Maintainability** (20 points)
   - Tests resistant to refactoring
   - No over-coupling to implementation
   - Clear and readable structure

4. **Edge Case Coverage** (20 points)
   - Boundary conditions tested
   - Error conditions covered
   - Edge case scenarios validated

5. **Performance & Stability** (20 points)
   - Acceptable execution speed
   - No flaky tests
   - Test isolation guaranteed

**Example Tests Inspection Prompt**:

```
Evaluate the real quality of this test suite:

TESTS TO EVALUATE:
[paste test suite]

CODE UNDER TEST:
[paste code being tested]

EVALUATE EACH DIMENSION /20:

1. SEMANTIC COVERAGE (/20)
   - Do tests validate business behavior or just execution?
   - Are critical business scenarios covered?
   - Are complete user flows tested?
   - Identify business coverage gaps

2. ASSERTION QUALITY (/20)
   - Are assertions specific (exact values) or generic (is not None)?
   - Are error messages clear and useful?
   - Do tests verify the "what" not the "how"?
   - Identify weak assertions

3. TEST MAINTAINABILITY (/20)
   - Do tests break during legitimate refactoring?
   - Over-coupling to implementation details?
   - Clear structure, readable tests?
   - Identify brittle tests

4. EDGE CASE COVERAGE (/20)
   - Are boundary conditions (0, null, max, min) tested?
   - Are error conditions covered?
   - Are edge cases validated?
   - Identify missing edge cases

5. PERFORMANCE & STABILITY (/20)
   - Acceptable execution speed (<1s for unit tests)?
   - Flaky tests (non-deterministic)?
   - Test isolation guaranteed?
   - Identify stability problems

REPORT FORMAT:
- Total score: /100
- Score per dimension with problematic test examples
- Tests to improve (CRITICAL/IMPORTANT/IMPROVEMENT)
- Specific recommendations
```

**Example Tests Report**:

```markdown
# Tests Inspection—calculate_confidence() Test Suite

## Overall Score: 78/100

### Scores by Dimension
- Semantic Coverage: 16/20 — Good business scenario coverage
- Assertion Quality: 14/20 — Some generic assertions
- Test Maintainability: 18/20 — Well-structured tests
- Edge Case Coverage: 15/20 — Missing negative edge cases
- Performance & Stability: 15/20 — Some slow tests

## Tests to Improve

### IMPORTANT
- **Generic assertions**: `test_basic_calculation` verifies
  `assert result > 0` instead of precise expected value.
  Change to `assert result == pytest.approx(0.67, rel=0.01)`.

### IMPROVEMENT
- **Missing edge case**: No test for negative n_contributors.
  Add test validating behavior with invalid inputs.
```

### 3. Security Inspection—Multi-Vector Defensive Posture

**Objective**: Detect vulnerabilities before deployment when fix cost is 30-100x lower than production.

**Focus**: Multi-vector threat analysis.

**Duration**: 10 minutes LLM generation + 30 minutes human validation

**Target score**: ≥ 80/100

**Analyzed vectors**:

1. **Injection & Validation** (20 points)
   - SQL injection, code injection
   - Complete input validation
   - Appropriate sanitization

2. **Authentication & Authorization** (20 points)
   - Appropriate access controls
   - Secure session management
   - Privilege escalation prevention

3. **Sensitive Data Protection** (20 points)
   - Encryption at rest/transit
   - No sensitive data in logs
   - GDPR/CCPA compliance

4. **Infrastructure & Network** (20 points)
   - Secure configuration
   - Appropriate TLS/SSL
   - Minimal exposure

5. **Business Logic & Monitoring** (20 points)
   - No business logic bypass
   - Appropriate security logging
   - Anomaly detection

**Example Security Inspection Prompt**:

```
Perform multi-vector security analysis of this code:

CODE TO ANALYZE:
[paste code]

SYSTEM CONTEXT:
[paste architecture/dependencies]

EVALUATE EACH VECTOR /20:

1. INJECTION & VALIDATION (/20)
   - SQL/code injection risks?
   - Complete and appropriate input validation?
   - User data sanitization?
   - Identify potential injection points

2. AUTHENTICATION & AUTHORIZATION (/20)
   - Appropriate access controls?
   - Secure session management?
   - Privilege escalation prevention?
   - Identify auth/authz flaws

3. SENSITIVE DATA PROTECTION (/20)
   - Appropriate encryption (at rest/transit)?
   - Sensitive data in logs/debug?
   - Privacy compliance (GDPR/CCPA)?
   - Identify data exposure

4. INFRASTRUCTURE & NETWORK (/20)
   - Secure configuration (TLS, certificates)?
   - Minimal service exposure?
   - Appropriate network segmentation?
   - Identify infrastructure flaws

5. BUSINESS LOGIC & MONITORING (/20)
   - Business logic bypass possible?
   - Security event logging?
   - Suspicious behavior detection?
   - Identify logic flaws

REPORT FORMAT:
- Total score: /100
- Score per vector with detected vulnerabilities
- Vulnerabilities (CRITICAL/HIGH/MEDIUM)
- Priority fix recommendations
```

**Example Security Report**:

```markdown
# Security Inspection—API Module

## Overall Score: 72/100

### Scores by Vector
- Injection & Validation: 18/20 — Good input validation
- Authentication & Authorization: 12/20 — Weak access controls
- Sensitive Data Protection: 16/20 — Encryption present, logs to verify
- Infrastructure: 14/20 — TLS configuration needs strengthening
- Business Logic: 12/20 — Missing rate limiting

## Detected Vulnerabilities

### CRITICAL
None detected

### HIGH
- **Missing Rate Limiting**: API endpoints without rate limiting.
  Vulnerable to DoS attacks. Implement rate limiting
  (e.g., 100 req/min per IP).

- **Weak Authorization Controls**: `delete_user()` function
  verifies authentication but not authorization (any authenticated
  user can delete any user). Add check `user.id == target_id or user.is_admin`.

### MEDIUM
- **Potential Sensitive Data Logging**: DEBUG logging
  could expose tokens. Verify production logs do not include
  credentials/tokens.
```

---

## Consolidated Improvement Process

**Activities**:

1. **Execute 3 Inspections** (LLM 90%, Team 10%)
   - All 3 inspections run in parallel (automated)
   - Fast generation: 3 × 10 minutes = 30 minutes total
   - Team receives 3 detailed reports with scores

2. **Consolidate Findings** (Team 70%, LLM 30%)
   - Team reviews 3 reports collectively
   - Group similar items across reports
   - Prioritize: CRITICAL → HIGH/IMPORTANT → MEDIUM/IMPROVEMENT
   - LLM generates consolidated dashboard

3. **Decisions & Actions** (Team 80%, LLM 20%)
   - CRITICAL items: Immediate fix (block merge)
   - HIGH/IMPORTANT items: Plan in current sprint
   - MEDIUM/IMPROVEMENT items: Opportunistic backlog
   - LLM generates action items with assignment

4. **Final Validation** (Team 90%, LLM 10%)
   - Re-run inspections after critical fixes
   - Verify scores ≥ 80/100 across 3 axes
   - Team approves for production
   - LLM documents decisions (accept/fix/defer)

**Definition of Done—Phase 6**:

This phase is considered complete when:

1. All 3 inspections executed with complete reports generated
2. Fagan Inspection score ≥ 80/100 (production code quality)
3. Tests Inspection score ≥ 80/100 (real business coverage)
4. Security Inspection score ≥ 80/100 (solid defensive posture)
5. All CRITICAL items resolved (merge blocked otherwise)
6. HIGH/IMPORTANT items planned with owners assigned
7. Team reviews and approves code as production-ready

**Outputs**:

- Three detailed inspection reports (Fagan, Tests, Security)
- Consolidated dashboard with scores and trends
- Prioritized action item list with owners
- Technical debt registry (for deferred items)

**Validation Criteria**:

:::tip[Validation Criteria]
- All 3 inspections executed and documented
- Scores ≥ 80/100 on each inspection
- All CRITICAL items resolved before merge
- HIGH items planned in current sprint
- Quality dashboard up to date and shared
- Team approves for production deployment
:::

**Time Estimation**:

- Execute 3 inspections: 30 minutes (parallel, automated)
- Human validation of reports: 90 minutes (30 min × 3)
- Consolidation & prioritization: 60 minutes
- Fix CRITICAL items: 60-120 minutes (variable)
- Final validation: 30 minutes
- **Total**: 4-6 hours per component

**Phase 6 ROI**:

```
Investment: 4-6 hours preventive inspection
Avoids: 40-80 hours future rework + production incident costs

Fagan Inspection (50 years proven): 10-100x historical ROI
Now practical: 30h (1976) → 40min (2024)

Technical debt avoided: Major refactoring 6 months later
Weak tests avoided: False security, production bugs
Vulnerabilities avoided: Production fix cost = 30-100x development

Phase 6 = Preventive quality assurance at negligible cost
```

**Common Pitfalls**:

:::danger[Avoid]
- **Ignore low scores**: Score < 80 = red flag, do not merge
- **Defer CRITICAL items**: Always fix before merge, no exceptions
- **False confidence in metrics**: 95% coverage ≠ good test quality
- **Neglect security**: "We'll fix later" → production vulnerability
- **Unread reports**: Generating reports then ignoring them = wasted time
- **Fix without re-inspection**: Validate that fix did not break something else
:::

**Quality Standards**:

**Target Scores**:
- Fagan Inspection: ≥ 80/100 (excellent: ≥ 90)
- Tests Inspection: ≥ 80/100 (excellent: ≥ 90)
- Security Inspection: ≥ 80/100 (excellent: ≥ 90)

**Golden Rules**:
1. CRITICAL blocks merge (non-negotiable)
2. ≥ 80 across 3 axes to merge
3. HIGH items planned before sprint end
4. Re-inspect after CRITICAL fixes
5. Document decisions (accept/fix/defer)

**Philosophy**:
"Invest 4-6h now to avoid 40-80h future rework. Phase 6 transforms unpredictable future costs into predictable, controlled investment."
