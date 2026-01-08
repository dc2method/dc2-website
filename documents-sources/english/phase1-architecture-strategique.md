---
sidebar_position: 2
---

# Phase 1: Strategic Architecture

<div style={{display: 'flex', gap: '10px', marginBottom: '25px', flexWrap: 'wrap'}}>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Agile: Sprint 0 / Inception
  </span>
  <span style={{background: '#64748b', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Duration: 1-2 days
  </span>
  <span style={{background: '#8b5cf6', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Roles: Designer + Product Owner
  </span>
  <span style={{background: '#2563eb', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    Human: 65%
  </span>
  <span style={{background: '#10b981', color: 'white', padding: '6px 14px', borderRadius: '20px', fontSize: '13px', fontWeight: '600'}}>
    LLM: 35%
  </span>
</div>

Phase 1 is the first step in "context engineering," which situates the module to be developed within its broader application context. It establishes the level of architectural abstraction by documenting strategic decisions, technical constraints, and business trade-offs. This phase creates the informational foundation that will enable the LLM to generate code coherent with the system's overall vision.

As we saw in the introduction, LLMs lack an internal representation of the program. They do not know how components fit together, what critical dependencies exist, or how a local decision impacts the overall architecture. The ADRs (Architecture Decision Records) and architecture schemas produced during Phase 1 create this explicit representation. Each decision is documented with its context, the alternatives considered, and its consequences. The LLM thus receives the "mental map" that it naturally lacks.

Furthermore, LLMs have no understanding of architecture's role. They do not understand why a component exists or what architectural constraints it must respect (performance, scalability, security). Without this context, they propose generic solutions disconnected from real needs. Thanks to the documentation produced in Phase 1, the LLM knows why this component exists, what business problem it solves, and what architectural trade-offs have been accepted.

Without this phase, the LLM generates code based on generic patterns found on the internet, without understanding your system's specific context. For example, without documentation explaining the choice of a vector database for similarity search, the LLM will systematically propose a standard relational database in subsequent phases. This fundamental architectural error would require a complete system overhaul once discovered later in the cycle.

---

### **Inputs**:

- Business requirements and success criteria
- Technical constraints (existing systems, technology standards, performance requirements)
- Organizational constraints (team skills, timeline, budget, political considerations)
- Stakeholder priorities and concerns
- Existing system documentation (if refactoring/extension)

### **Activities**:

1. **Problem Crystallization** (Designer 80%, LLM 20%)

    - The designer clearly articulates the business problem
    - The LLM helps identify unstated assumptions
    - Separate symptoms from root causes
    - Quantitatively define success criteria

2. **Constraint Mapping** (Designer 60%, LLM 40%)

    - The designer identifies constraints from experience
    - The LLM generates a comprehensive constraint checklist
    - Prioritize constraints (must-have vs. nice-to-have)
    - Document organizational and political constraints

3. **Solution Generation** (Designer 50%, LLM 50%)

    - The designer provides 1-2 initial solution directions
    - The LLM generates 2-3 alternative approaches
    - Ensure at least one innovative/unconventional approach
    - Document each approach with architecture diagrams

4. **Trade-off Analysis** (Designer 70%, LLM 30%)

    - The designer evaluates approaches against business priorities
    - The LLM generates a trade-off comparison matrix
    - Identify risks and mitigation strategies for each approach
    - The designer makes the final decision with documented justification

### **Definition of Done—Phase 1**:

This phase is considered complete when:

1. The business problem is clearly articulated with quantified success criteria
2. At least 3 ADRs (Architecture Decision Records) document major decisions
3. A high-level architecture schema exists (C4 diagrams levels 1-2)
4. Critical technical constraints are identified and prioritized
5. The chosen solution includes clear justification of trade-offs vs. alternatives
6. Main architectural risks are documented with mitigation strategies
7. The Product Owner validates that the proposed solution meets business needs

### **Outputs**:

Strategic Architecture Document (2,000-4,000 words) containing:

- **Executive Summary**: Problem statement + recommended solution (200 words)
- **Problem Definition**: Root cause analysis, success criteria
- **Constraints**: Technical, organizational, timeline, budget
- **Solution Approaches**: 2-4 approaches with diagrams
- **Trade-off Analysis**: Comparison matrix, risk evaluation
- **Recommendation**: Chosen approach with justification
- **Success Metrics**: How to measure if the solution succeeds
- **Risk Mitigation**: Top 3-5 risks and mitigation strategies

### **Validation Criteria**:

:::tip[Validation Criteria]
- Stakeholders approve the problem definition and success criteria
- All major constraints documented (technical + organizational)
- At least 2 solution approaches evaluated (no single-approach analysis)
- Trade-offs explicitly stated (not just benefits)
- Decision justification references business priorities
- Risks identified with mitigation strategies
:::

### **Time Estimation**:

- Initial draft: 4-6 hours (Designer + LLM collaboration)
- Stakeholder review: 2-4 hours (may require 1-2 cycles)
- Final approval: 1-2 hours
- **Total**: 1-2 days elapsed time

### **Prompt Examples**:

_Prompt 1—Problem Crystallization_:

```
I am designing a solution for [business problem]. Here is my initial problem statement:
[problem description]

Help me crystallize this problem by:
1. Identifying any unstated assumptions in my description
2. Separating symptoms from root causes
3. Suggesting 3-5 quantitative success criteria
4. Highlighting potential scope creep risks

Format your response as a structured analysis with each section clearly labeled.
```

_Prompt 2—Solution Generation_:

```
Given this problem definition and constraints:
[paste problem + constraints]

I have identified this solution approach:
[initial solution]

Generate 2-3 alternative solution approaches that:
- Address the same problem differently
- Work within the stated constraints
- Include at least one unconventional/innovative approach
- Are technically feasible for our context

For each solution, provide:
- High-level architecture (components + interactions)
- Key advantages and disadvantages
- Estimated complexity (low/medium/high)
- Main risks
```

_Prompt 3—Trade-off Analysis_:

```
Create a trade-off comparison matrix for these solution approaches:
[paste 3-4 solution approaches]

Compare across these dimensions:
- Development time (estimation in weeks)
- Technical complexity (scale 1-10)
- Maintainability (long-term cost)
- Performance (meets requirements?)
- Risk level (low/medium/high)
- Organizational fit (team skills, culture)
- Scalability (future growth)

For each dimension, briefly explain the rating. Then recommend which approach best balances trade-offs for this context: [paste business priorities].
```

### **Common Pitfalls**:

:::danger[Avoid]
- **Single-approach analysis**: Evaluating only one solution (no true alternatives)
- **Technology-first thinking**: Choosing the technology stack before understanding the problem
- **Ignoring organizational constraints**: Designing a perfect solution the team cannot execute
- **Analysis paralysis**: Generating 10+ approaches instead of focusing on 2-4 viable ones
- **Vague success criteria**: "Improve performance" instead of "Reduce p95 latency to < 100ms"
- **Missing stakeholder buy-in**: Designer decides alone without stakeholder validation
:::
