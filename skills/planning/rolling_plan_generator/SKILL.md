---
name: rolling_plan_generator
description: >
  Use this skill when creating roadmaps, planning work across time horizons, or managing rolling planning cycles.
  Applies to quarterly planning, roadmap creation, portfolio planning, and adaptive planning.
  Triggers even if users say "what should we work on next quarter," "how do we plan ahead," or "we need a roadmap"
  without explicitly mentioning "rolling planning" or "horizons."
---

# Rolling Plan Generator

Creates Now/Next/Later roadmaps with dependency sequencing and adaptive planning cycles.

## Core Principle

**Plan in horizons, not fixed dates:** Commit to now, prepare for next, explore later. This balances focus with flexibility.

## When to Use This Skill

- Quarterly or iteration planning needed
- Roadmap creation or update requested
- Portfolio prioritization required
- Adaptive planning approach needed
- **Even if** user doesn't mention "rolling planning" but describes planning across time

## Input Requirements

- Work items or initiatives to plan
- Planning horizon (quarters, months, iterations)
- Capacity constraints
- Strategic priorities or goals
- Known dependencies

## Output Structure

```markdown
## Rolling Plan: [Team/Organization]

### Planning Context
**Time horizon:** [e.g., Q1-Q4 2025]
**Planning cadence:** [How often this is updated]
**Capacity:** [Available resources per period]

### Horizon 1: NOW (Committed)
[Current period - high confidence]

| Initiative | Owner | Outcome | Dependencies | Confidence |
|------------|-------|---------|--------------|------------|
| [Item] | [Who] | [What result] | [What blocked by] | High |

**Key focus:** [Theme for this period]
**Risks:** [What could derail commitments]

### Horizon 2: NEXT (Preparing)
[Next period - medium confidence]

| Initiative | Owner | Outcome | Prep Needed | Confidence |
|------------|-------|---------|-------------|------------|
| [Item] | [Who] | [What result] | [What to prepare] | Medium |

**Key questions to answer:** [What needs clarity before commitment]
**Discovery work:** [Spikes or research planned]

### Horizon 3: LATER (Exploring)
[Future periods - low confidence]

| Initiative | Strategic Fit | Unknowns | Next Look |
|------------|---------------|----------|-----------|
| [Item] | [Why it matters] | [What we don't know] | [When to revisit] |

**Strategic themes:** [Areas of exploration]
**Signals to watch:** [What would move this to NEXT]

### Dependency Sequencing

#### Critical Sequence
1. [First item] → enables → [Second item]
2. [Second item] → enables → [Third item]

#### Parallel Streams
[Work that can happen concurrently]

### Planning Cadence

| Cadence | Focus | Participants | Output |
|---------|-------|--------------|--------|
| Weekly | Progress & adjustments | Team | Updated board |
| Monthly | Horizon review | Team + Stakeholders | Re-prioritized NEXT |
| Quarterly | Full replan | All | New NOW/NEXT/LATER |

### Decision Rules

**Move LATER → NEXT when:**
- [Criteria 1]
- [Criteria 2]

**Move NEXT → NOW when:**
- [Criteria 1]
- [Criteria 2]

**De-prioritize when:**
- [Criteria for moving back or dropping]

### Success Metrics
[How we measure planning effectiveness]
```

## Key Principles

1. **Confidence Matches Horizon:** NOW = committed, NEXT = probable, LATER = possible
2. **Explicit Movement Criteria:** Clear rules for shifting between horizons
3. **Regular Rhythm:** Predictable cadence for review and adjustment
4. **Dependencies Drive Sequence:** Order by enablement, not just priority

## Quality Checks

- [ ] Each horizon has appropriate confidence level
- [ ] Movement criteria are explicit
- [ ] Dependencies are sequenced logically
- [ ] Planning cadence is realistic
- [ ] Capacity is acknowledged
