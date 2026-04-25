---
name: leadership_map_analyzer
description: >
  Use this skill when analyzing leadership development needs, assessing leadership effectiveness, or planning leadership interventions.
  Applies to leadership coaching, executive development, organizational design, and team effectiveness.
  Triggers even if users say "our leadership isn't working," "how can we develop better leaders," or "help assess our leadership team"
  without explicitly mentioning "Integral Theory" or "quadrants."
---

# Leadership Map Analyzer

Applies Integral Theory quadrants to analyze leadership development needs and generate targeted intervention strategies.

## Core Principle

**Effective leadership requires development across all four quadrants:** Individual interior (mindset), individual exterior (behavior), collective interior (culture), and collective exterior (systems).

## When to Use This Skill

- User describes leadership challenges or development needs
- Executive or leadership team assessment requested
- Organizational culture or effectiveness concerns
- Leadership transition or succession planning
- **Even if** user doesn't mention "leadership map" but describes leadership problems

## Processing Steps

### Step 1: Assess Four Quadrants

**Upper-Left (Individual Interior):** Mindset, values, beliefs, emotional intelligence
**Upper-Right (Individual Exterior):** Behaviors, skills, actions, communication style
**Lower-Left (Collective Interior):** Culture, shared values, relationships, trust
**Lower-Right (Collective Exterior):** Systems, structures, processes, metrics

### Step 2: Identify Development Gaps

For each quadrant, assess:
- Current state strengths
- Current state weaknesses
- Desired state
- Gap magnitude (small/medium/large)

### Step 3: Generate Interventions

Match interventions to quadrant gaps:
- **UL:** Coaching, reflection practices, mindset work
- **UR:** Training, skill building, behavioral feedback
- **LL:** Team development, culture work, relationship building
- **LR:** Structural changes, process redesign, metric alignment

## Output Structure

```markdown
## Leadership Map Analysis

### Quadrant Assessment

| Quadrant | Focus | Current State | Desired State | Gap |
|----------|-------|---------------|---------------|-----|
| UL (Mindset) | Individual Interior | [assessment] | [target] | [size] |
| UR (Behavior) | Individual Exterior | [assessment] | [target] | [size] |
| LL (Culture) | Collective Interior | [assessment] | [target] | [size] |
| LR (Systems) | Collective Exterior | [assessment] | [target] | [size] |

### Key Insights
[Patterns across quadrants]

### Recommended Interventions

#### Immediate (0-3 months)
- [UL intervention if needed]
- [UR intervention if needed]
- [LL intervention if needed]
- [LR intervention if needed]

#### Medium-term (3-12 months)
- [Sustained development activities]

### Success Indicators
[How to measure progress in each quadrant]
```

## Quality Checks

- [ ] All four quadrants assessed
- [ ] Interventions matched to specific gaps
- [ ] Mix of individual and collective interventions
- [ ] Success indicators are observable
