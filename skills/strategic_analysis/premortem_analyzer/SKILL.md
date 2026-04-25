---
name: premortem_analyzer
description: >
  Use this skill when analyzing risks, failure modes, or potential problems in plans, projects, or initiatives.
  Applies to project kickoffs, major decisions, product launches, and strategic bets.
  Triggers even if users say "what could go wrong," "I'm worried about this plan," or "help me think through risks"
  without explicitly mentioning "premortem" or "risk analysis."
---

# Pre-Mortem Analyzer

Sequential structured risk analysis that takes an initiative/project input and systematically generates failure scenarios, root causes, and prevention strategies.

## Core Principle

**Imagine the project has failed spectacularly. Work backward to determine what caused the failure.** This psychological technique surfaces risks that optimistic planning misses.

## When to Use This Skill

- User describes a plan, project, or initiative and asks for risk analysis
- Team is about to commit significant resources to a strategic bet
- Stakeholders express concerns but can't articulate specific risks
- Major product launch, reorganization, or technical migration planned
- **Even if** user doesn't say "premortem" but expresses worry or asks "what could go wrong?"

## Input Requirements

Accepts input in any format:
- Project description or plan (pasted text, file path, or conversation)
- Strategic initiative summary
- Product roadmap or launch plan
- Technical architecture or migration proposal
- Organizational change proposal

If input lacks detail, ask clarifying questions about:
1. What is the primary objective?
2. What is the timeline?
3. Who are the key stakeholders?
4. What resources are committed?
5. What does success look like?

## Processing Steps

### Step 1: Establish the Failure Scenario

Frame the analysis with vivid specificity:

*"It is [timeline] months from now. The project has failed catastrophically - not just underperformed, but completely collapsed. Stakeholders are asking 'what happened?' Write the story of this failure."*

### Step 2: Generate Failure Modes

Systematically explore failure across these dimensions:

**Technical/Execution Failures:**
- Technology choices proved wrong
- Integration complexities underestimated
- Performance/scalability issues emerged
- Quality problems accumulated
- Technical debt became unmanageable

**People/Organization Failures:**
- Key team members left
- Skills gaps emerged
- Team dysfunction (conflict, disengagement)
- Leadership changes disrupted momentum
- Stakeholder alignment fractured

**Market/External Failures:**
- Customer needs shifted
- Competitor launched superior solution
- Regulatory changes blocked approach
- Economic conditions changed
- Partner/vendor failures

**Process/Planning Failures:**
- Timeline was unrealistic from start
- Dependencies weren't identified
- Scope crept uncontrollably
- Decision-making bottlenecks emerged
- Communication broke down

**Resource Failures:**
- Budget was cut mid-project
- Critical resources unavailable
- Tooling/infrastructure inadequate
- Competing priorities diverted attention

### Step 3: Identify Root Causes

For each failure mode, dig deeper using "Five Whys":

1. Why did this happen?
2. Why was that condition present?
3. Why wasn't it addressed earlier?
4. Why did our processes allow this?
5. Why didn't we see this coming?

### Step 4: Develop Prevention Strategies

For each root cause, generate:

**Prevention Actions** (eliminate the cause):
- Specific steps to prevent this failure mode
- Early warning indicators to monitor
- Decision points where course-correction happens

**Mitigation Actions** (reduce impact if it occurs):
- Contingency plans
- Fallback positions
- Risk transfer strategies

**Detection Mechanisms** (catch it early):
- Metrics to track
- Checkpoints for review
- Feedback loops to establish

### Step 5: Prioritize by Risk Exposure

Rank risks using: **Probability × Impact × Detectability**

| Priority | Characteristics | Action Required |
|----------|----------------|-----------------|
| **CRITICAL** | High probability, high impact, low detectability | Immediate action before proceeding |
| **HIGH** | High probability OR high impact | Address in first sprint/phase |
| **MEDIUM** | Moderate on all dimensions | Monitor with specific triggers |
| **LOW** | Low probability, manageable impact | Accept with awareness |

## Output Structure

Return results in this format:

```markdown
## Pre-Mortem Analysis: [Project Name]

### Executive Summary
- **Critical Risks:** [count requiring immediate action]
- **High Risks:** [count requiring near-term action]
- **Key Themes:** [patterns across failure modes]

### Failure Scenario Narrative
[Vivid 2-3 paragraph story of catastrophic failure]

### Risk Analysis

#### CRITICAL RISKS (Immediate Action Required)

**Risk:** [Name]
- **Failure Mode:** [What happens]
- **Root Cause:** [Why it happens - deep cause, not symptom]
- **Early Warning Signs:** [Specific indicators to monitor]
- **Prevention Actions:** [Concrete steps to eliminate cause]
- **Mitigation Plan:** [What to do if warning signs appear]
- **Owner:** [Who should own monitoring/prevention]
- **Decision Point:** [When to reassess or pivot]

#### HIGH RISKS (Address in First Phase)

[Same structure as above]

#### MEDIUM RISKS (Monitor with Triggers)

[Same structure, focused on detection mechanisms]

### Cross-Cutting Themes
[Patterns that appear across multiple risks - often indicate systemic issues]

### Recommended Next Steps
1. [Immediate actions before project proceeds]
2. [First-sprint risk reduction activities]
3. [Ongoing monitoring mechanisms to establish]
4. [Stakeholder conversations needed]

### Risk Register Summary
| Risk | Probability | Impact | Detectability | Priority | Owner |
|------|-------------|--------|---------------|----------|-------|
| [Risk 1] | H/M/L | H/M/L | H/M/L | CRITICAL | [Name] |
| ... | ... | ... | ... | ... | ... |
```

## Key Principles

1. **Psychological Safety First:** Frame as learning exercise, not criticism of the plan
2. **Specificity Over Generality:** "API integration will fail" → "Third-party API rate limits will throttle our sync process causing data inconsistencies"
3. **Actionable Outputs:** Every risk must have concrete prevention/mitigation actions
4. **Early Detection Focus:** Emphasize warning signs over post-mortem analysis
5. **Ownership Matters:** Assign specific owners for risk monitoring

## Common Patterns

### Pattern: "Optimism Bias"
When the team struggles to imagine failure:
- Share examples of similar projects that failed
- Ask "What would a cynical competitor say will go wrong?"
- Use "Five Whys" aggressively to push past surface answers

### Pattern: "Vague Risks"
When risks are generic ("requirements might change"):
- Force specificity: "What specifically will change and why?"
- Connect to concrete failure scenarios
- Demand actionable prevention strategies

### Pattern: "Too Many Critical Risks"
When everything is rated as critical:
- Force ranking: "If you could only fix three, which would they be?"
- Look for common root causes that address multiple risks
- Separate symptoms from root causes

### Pattern: "No Ownership"
When risks lack clear owners:
- Ask "Who has the information/skills to detect this earliest?"
- Assign monitoring responsibility even if prevention is collective
- Escalate ownership gaps as a meta-risk

## Quality Checks

Before delivering output, verify:
- [ ] Failure scenario is vivid and specific (not generic)
- [ ] Root causes go beyond surface symptoms
- [ ] Every risk has at least one prevention AND one mitigation action
- [ ] Early warning signs are observable/measurable
- [ ] Owners are assigned to critical/high risks
- [ ] Recommended next steps are actionable within 1 week

## Examples

### Example Input
```
We're launching a new customer portal in Q2. It will replace our legacy system, 
integrate with our CRM and billing systems, and provide self-service capabilities. 
Timeline is aggressive: 3 months to build and launch. Team of 6 developers, 
1 designer, 1 PM. CTO is sponsoring, VP of Sales is key stakeholder.
```

### Example Output (Abbreviated)
```markdown
## Pre-Mortem Analysis: Customer Portal Launch

### Executive Summary
- **Critical Risks:** 2 requiring immediate action
- **High Risks:** 4 requiring near-term action
- **Key Themes:** Integration complexity underestimated, timeline optimism, stakeholder alignment fragility

### Failure Scenario Narrative

It's July and the portal launch has been indefinitely delayed. The March deadline came and went with only 40% of features complete. Integration with the billing system revealed undocumented APIs that require custom adapters. The CRM team reprioritized their roadmap, leaving your integration requests unaddressed for 6 weeks. Two senior developers quit in April due to unsustainable pressure. The VP of Sales, frustrated by lack of visibility, demanded a scope freeze that demoralized the team. Customers who were promised self-service capabilities are escalating complaints. The legacy system is now running on borrowed time with key maintainers reassigned.

### Risk Analysis

#### CRITICAL RISKS (Immediate Action Required)

**Risk:** Integration Complexity Catastrophe
- **Failure Mode:** Billing and CRM integrations prove far more complex than estimated, blocking all dependent features
- **Root Cause:** No technical discovery performed on third-party APIs; assumptions based on marketing documentation rather than technical reality
- **Early Warning Signs:** 
  - API sandbox access delayed beyond Week 1
  - Discovery spike reveals undocumented endpoints
  - Third-party support response time > 48 hours
- **Prevention Actions:**
  - Week 1: Mandatory integration discovery spikes for both systems
  - Build working prototype of critical integration paths before committing to timeline
  - Establish direct technical contact at vendor companies
- **Mitigation Plan:** If complexity emerges, immediately descope non-essential features and negotiate phased integration
- **Owner:** Tech Lead (Sarah)
- **Decision Point:** End of Week 2 - if prototypes aren't working, renegotiate timeline or scope

**Risk:** Key Person Dependency
- **Failure Mode:** Loss of one senior developer derails critical path work
- **Root Cause:** Only one person understands legacy system internals needed for migration; no knowledge sharing planned
- **Early Warning Signs:**
  - Single developer consistently working late
  - Questions about legacy system always routed to same person
  - No pair programming or documentation occurring
- **Prevention Actions:**
  - Immediately schedule legacy system knowledge transfer sessions
  - Implement pair rotation for all legacy-related work
  - Document critical integration patterns in shared wiki
- **Mitigation Plan:** Cross-train backup developer within 2 weeks; identify contractor options as emergency capacity
- **Owner:** Engineering Manager
- **Decision Point:** Weekly check-in on knowledge distribution

[Additional risks continue...]
```

## Attribution

Adapted from Gary Klein's pre-mortem technique and organizational learning frameworks  
Licensed under principles of open organizational practices
