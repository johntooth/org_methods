---
name: persistent_activities_mapper
description: >
  Use this skill when identifying recurring work patterns, analyzing capacity allocation, or optimizing ongoing operational work.
  Applies to capacity planning, operational excellence, sustainability analysis, and workload balancing.
  Triggers even if users say "we're always firefighting," "where does our time go," or "how much capacity do we have for new work"
  without explicitly mentioning "persistent activities" or "capacity allocation."
---

# Persistent Activities Mapper

Identifies recurring work patterns and proposes capacity allocation for sustainable team performance.

## Core Principle

**Make the invisible visible:** Persistent activities (recurring work) consume capacity but often go unplanned. Explicit recognition enables sustainable allocation.

## When to Use This Skill

- Team feels overwhelmed but can't explain why
- Capacity planning for upcoming period
- Operational work vs. project work balance needed
- Burnout or sustainability concerns
- **Even if** user doesn't mention "persistent activities" but describes capacity or workload challenges

## Input Requirements

- Team context (size, function)
- Known recurring activities
- Project/initiative workload
- Current pain points or concerns
- Time period for analysis

## Output Structure

```markdown
## Persistent Activities Analysis: [Team]

### Activity Categories

#### Planned Persistent Activities
[Recurring work that is expected and planned]

| Activity | Frequency | Time Required | Owner | Notes |
|----------|-----------|---------------|-------|-------|
| [Activity] | [Daily/Weekly/etc.] | [Hours] | [Who] | [Context] |

#### Unplanned Persistent Activities
[Recurring work that emerges unexpectedly]

| Activity | Frequency | Time Required | Impact | Mitigation |
|----------|-----------|---------------|--------|------------|
| [Activity] | [Variable] | [Hours] | [Effect on team] | [How to reduce] |

#### Seasonal/Periodic Activities
[Recurring work tied to specific times]

| Activity | When | Duration | Preparation Needed |
|----------|------|----------|-------------------|
| [Activity] | [Time period] | [Hours/days] | [What to prepare] |

### Capacity Analysis

#### Total Available Capacity
- **Team size:** [Number]
- **Hours per period:** [Total available]
- **Effective capacity (after PTO, etc.):** [Adjusted total]

#### Capacity Allocation

| Category | Hours | Percentage |
|----------|-------|------------|
| Planned persistent | [X] | [%] |
| Unplanned persistent | [X] | [%] |
| Project work | [X] | [%] |
| Buffer/contingency | [X] | [%] |

#### Capacity Health Indicators
- **Sustainable threshold:** <80% allocated to known work
- **Current allocation:** [X]% - [Healthy/At Risk/Unsustainable]
- **Unplanned activity trend:** [Increasing/Stable/Decreasing]

### Patterns & Insights

#### High-Cost Activities
[Persistent activities consuming disproportionate time]

#### Automation Opportunities
[Candidates for reducing manual effort]

#### Elimination Candidates
[Activities that may not be necessary]

### Recommendations

#### Immediate Actions (This Period)
1. [Action to rebalance capacity]
2. [Activity to automate or eliminate]
3. [Boundary to set]

#### Medium-term Improvements (Next 2-3 Periods)
1. [Systemic improvement]
2. [Capability to build]
3. [Process to change]

#### Capacity Protection Strategies
[How to protect capacity for important but non-urgent work]

### Monitoring Plan

| Metric | Current | Target | Review Cadence |
|--------|---------|--------|----------------|
| % capacity on unplanned work | [X]% | [Y]% | [Frequency] |
| Team sustainability score | [Rating] | [Target] | [Frequency] |
| Persistent activity count | [Number] | [Trend] | [Frequency] |
```

## Key Principles

1. **Name It to Manage It:** Unnamed activities consume hidden capacity
2. **Distinguish Planned vs. Unplanned:** Different strategies for each
3. **Protect Buffer:** Sustainable teams leave capacity for emergence
4. **Review Regularly:** Persistent activities drift over time

## Quality Checks

- [ ] All recurring activities captured
- [ ] Time estimates are realistic (based on data if possible)
- [ ] Capacity allocation sums correctly
- [ ] Recommendations are actionable
- [ ] Monitoring plan is specific
