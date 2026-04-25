---
name: backlog_filter
description: >
  Use this skill when analyzing, prioritizing, or sequencing backlog items based on clarity of understanding.
  Applies to sprint planning, roadmap refinement, dependency management, and estimation decisions.
  Triggers even if users say "what should we work on next," "how do we order these stories," or "this feels risky"
  without explicitly mentioning "backlog" or "filter."
compatibility:
  required_tools: ["FileSystemTools", "ShellTools"]
---

# Backlog Filter

Analyzes work items by **clarity of understanding** (not size or complexity) to determine prioritization, sequencing, and action logic.

## Core Principle

**High-clarity items proceed confidently when resourced, regardless of size.** Low-clarity items require discovery before commitment.

## When to Use This Skill

- User provides a list of backlog items, user stories, or initiatives to prioritize
- Team is deciding what to work on next in sprint/iteration planning
- Stakeholders ask "why is this blocked?" or "what's the risk here?"
- Need to sequence work based on dependencies and cost of delay
- Estimation discussions where uncertainty is high
- **Even if** user doesn't explicitly say "backlog" but describes work ordering challenges

## Input Requirements

Accepts input in any format:
- Raw list of work items (pasted text, file path, or conversation)
- Existing backlog export (CSV, JSON, markdown)
- Verbal description of upcoming work
- Jira/Azure DevOps/GitHub issue references

If input is unstructured, ask clarifying questions about:
1. What work items are under consideration?
2. What dependencies exist between items or teams?
3. Are there known external expertise requirements?
4. What is the time horizon (this sprint, next quarter, etc.)?

## Processing Steps

### Step 1: Assess Clarity Level

For each work item, evaluate understanding using these criteria:

**HIGH CLARITY** (Proceed with confidence):
- Requirements are specific and testable
- Team has done similar work before
- Dependencies are identified and resolved
- Success criteria are agreed upon
- *Action:* Can be estimated and committed to immediately

**MEDIUM CLARITY** (Needs refinement):
- General direction is clear but details are fuzzy
- Some dependencies unknown or unresolved
- Team has partial relevant experience
- Success criteria need clarification
- *Action:* Timebox discovery spikes, gather missing information

**LOW CLARITY** (Requires discovery):
- Problem space is ambiguous
- No relevant team experience
- Major dependencies unidentified
- Success criteria undefined
- *Action:* Do not estimate; run experiments, prototypes, or research spikes

### Step 2: Apply Sequencing Logic

Order work using these rules (in priority order):

1. **Dependencies First:** Prioritize work that unblocks other teams or items
2. **Cost of Delay:** Sequence work where delay impacts other teams' expertise availability
3. **Clarity Progression:** Move low-clarity → medium-clarity → high-clarity before committing
4. **Value Flow:** Among equal-clarity items, prioritize highest value delivery

### Step 3: Determine Estimation Approach

Match estimation effort to clarity level:

| Clarity | Estimation Strategy |
|---------|---------------------|
| **High** | Provide confident estimates; treat as commitments |
| **Medium** | Range estimates with explicit assumptions; include discovery tasks |
| **Low** | **Do not estimate**; use timeboxed experiments instead |

**Critical Rule:** Never spend more time estimating than the decision value justifies. If an estimate won't change the decision, skip it.

### Step 4: Generate Action Plan

For each item, output:
- Clarity assessment with justification
- Recommended next action (proceed, spike, experiment, defer)
- Dependencies to resolve
- Estimation guidance (or explicit "do not estimate" flag)
- Suggested sequence position

## Output Structure

Return results in this format:

```markdown
## Backlog Filter Analysis

### Summary
- **Total Items:** [count]
- **Ready to Proceed:** [count] (High clarity)
- **Needs Refinement:** [count] (Medium clarity)  
- **Requires Discovery:** [count] (Low clarity)

### Item Analysis

#### [Item Name]
- **Clarity Level:** HIGH|MEDIUM|LOW
- **Rationale:** [specific observations]
- **Dependencies:** [list or "none identified"]
- **Recommended Action:** [proceed/spike/experiment/defer]
- **Estimation Guidance:** [confident estimate/range with assumptions/do not estimate]
- **Sequence Priority:** [1st, 2nd, 3rd, etc. or "after X is resolved"]

### Recommended Sequence
1. [First item] - [reason: e.g., "unblocks 3 other items"]
2. [Second item] - [reason]
3. ...

### Next Steps
- Immediate actions for team
- Information gaps to fill
- Stakeholder conversations needed
```

## Key Principles

1. **Clarity Over Size:** A large, well-understood item is lower risk than a small, ambiguous one
2. **Estimates Support Decisions:** Only estimate when it changes the decision; otherwise, skip estimation
3. **Collaborative Estimation:** Most accurate estimates come from people who will do the work
4. **De-risk Through Sequencing:** Order work to expose risks early and leverage dependencies
5. **Timebox Discovery:** Use fixed-time experiments, not open-ended analysis

## Common Patterns

### Pattern: "Everything Feels Uncertain"
When all items rate as Low/Medium clarity:
- Recommend stopping planning
- Propose a single discovery sprint focused on reducing uncertainty
- Identify 2-3 critical questions that, if answered, would increase clarity most

### Pattern: "Hidden Dependencies"
When dependencies emerge mid-analysis:
- Flag as critical risk
- Re-sequence to address dependency first
- Recommend inter-team alignment conversation (use `interteam_agreement_designer` skill)

### Pattern: "Estimation Debate"
When team argues about story points/hours:
- Redirect to clarity assessment: "What don't we understand yet?"
- If clarity is low, declare estimation premature
- Propose a timeboxed spike instead

## Quality Checks

Before delivering output, verify:
- [ ] Each item has explicit clarity justification (not just a label)
- [ ] Sequencing logic references specific dependencies or cost-of-delay factors
- [ ] Low-clarity items explicitly say "do not estimate"
- [ ] Recommendations are actionable within next 1-3 days
- [ ] Output avoids false precision (ranges over point estimates for medium clarity)

## Examples

### Example Input
```
We have these items for next sprint:
1. Migrate user authentication to OAuth2
2. Add dark mode toggle to settings page
3. Integrate with new payment provider API
4. Fix performance issues in dashboard loading
```

### Example Output (Abbreviated)
```markdown
## Backlog Filter Analysis

### Summary
- **Total Items:** 4
- **Ready to Proceed:** 2 (High clarity)
- **Needs Refinement:** 1 (Medium clarity)  
- **Requires Discovery:** 1 (Low clarity)

### Item Analysis

#### 1. Migrate user authentication to OAuth2
- **Clarity Level:** MEDIUM
- **Rationale:** Team has OAuth experience but new provider specifics unknown; security requirements need validation
- **Dependencies:** Security team review, new provider credentials
- **Recommended Action:** 2-day spike to validate provider integration approach
- **Estimation Guidance:** Range estimate only after spike completes
- **Sequence Priority:** 2nd (after payment API discovery)

#### 3. Integrate with new payment provider API
- **Clarity Level:** LOW
- **Rationale:** Zero team experience with this provider; compliance requirements unclear; API documentation incomplete
- **Dependencies:** Legal/compliance approval, sandbox access
- **Recommended Action:** Do not estimate; run 3-day experiment with sandbox
- **Estimation Guidance:** DO NOT ESTIMATE - too much unknown
- **Sequence Priority:** 1st (highest risk, blocks other payment work)

### Recommended Sequence
1. Payment provider integration experiment - exposes compliance risks early
2. OAuth migration spike - informs authentication timeline
3. Dark mode toggle - high clarity, quick win
4. Dashboard performance - depends on findings from above

### Next Steps
- Request payment provider sandbox access today
- Schedule security team review for OAuth approach
- Timebox both discovery items to prevent analysis paralysis
```

## Available Scripts

- **`scripts/batch_filter.py`** - Process multiple backlog items from CSV/JSON files and generate prioritization reports

Usage:
```bash
uv run scripts/batch_filter.py --input backlog.csv --output analysis.md
```

## References

- **`references/estimation_principles.md`** - Detailed guidance on estimation anti-patterns and alternatives
- **`references/dependency_mapping.md`** - Techniques for identifying and visualizing work dependencies

## Attribution

Original framework by Kim Ballestrin and Dr. Saeed Shalbafan  
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)
