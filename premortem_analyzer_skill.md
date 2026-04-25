---
name: premortem_analyzer
description: >
  Use this skill when assessing risks for projects, initiatives, or strategic decisions before commitment.
  Takes project/initiative description and systematically generates failure scenarios, root causes,
  prevention strategies, and mitigation actions. Applies sequential structured analysis to imagine
  future failure and work backwards to prevent it. Even if they don't explicitly mention "premortem"
  or "risk assessment" — any situation where you need to stress-test plans, identify blind spots,
  or build contingency strategies before investing significant resources.
---

# Pre-Mortem Analyzer

## Purpose
Systematically identify failure modes before they happen by imagining the project has failed and working backwards to uncover root causes and prevention strategies.

## Core Principle
**Imagine failure to prevent it**: By assuming catastrophic failure has occurred, teams bypass optimism bias and surface risks that traditional risk assessment misses.

---

## When to Use This Skill
- User is planning a major project, initiative, or strategic decision
- User needs to stress-test assumptions before committing resources
- User wants to build contingency plans or mitigation strategies
- Context: project kickoff, investment decisions, product launches, organizational changes

**Do NOT use this skill when:**
- User needs real-time incident response (project already failing)
- User wants post-mortem analysis of completed failure (different methodology)
- Adjacent tasks: use `backlog_filter` for prioritizing which risks to address first

## Input Requirements
What the user needs to provide:
- **Required**: Project/initiative description with objectives
- **Required**: Timeline and key milestones
- **Optional**: Known constraints, dependencies, stakeholders
- **Format**: Any format — narrative, bullet points, project charter excerpt

## Processing Steps

### Step 1: Set the Stage
Establish the pre-mortem frame:
- Assume we are [timeline duration] in the future
- The project has failed catastrophically (not just delayed — FAILED)
- All stakeholders agree it was a complete disaster
- Our task: explain HOW this happened

### Step 2: Generate Failure Scenarios
Use sequential thinking to explore failure modes across dimensions:

**Technical/Execution Failures:**
- Technology didn't work as expected
- Architecture couldn't scale
- Integration points failed
- Quality degraded over time

**Market/Customer Failures:**
- Customers didn't adopt as expected
- Competitor response neutralized advantage
- Market timing was wrong
- Value proposition didn't resonate

**Organizational Failures:**
- Key people left the project
- Leadership support evaporated
- Team couldn't collaborate effectively
- Decision-making paralyzed progress

**Resource Failures:**
- Budget ran out before value delivered
- Critical skills unavailable
- Dependencies blocked progress indefinitely
- Opportunity cost became unacceptable

**External Failures:**
- Regulatory changes blocked approach
- Economic conditions shifted
- Partner/supplier failures cascaded
- Black swan events disrupted plans

### Step 3: Trace Root Causes
For each failure scenario, apply "Five Whys":
1. Why did this failure occur? (surface cause)
2. Why was that condition present?
3. Why wasn't it prevented?
4. Why wasn't the prevention detected?
5. Why did our systems allow this? (root cause)

### Step 4: Develop Prevention Strategies
For each root cause, identify:
- **Prevention**: What could we do NOW to prevent this?
- **Mitigation**: If prevention fails, how do we minimize impact?
- **Detection**: What early warning signals should we monitor?
- **Response**: If detected, what's our action plan?

### Step 5: Prioritize Actions
Rank prevention strategies by:
- **Likelihood**: How probable is this failure mode?
- **Impact**: How severe would the consequences be?
- **Actionability**: Can we actually prevent/mitigate this?
- **Cost-effectiveness**: Is prevention cost less than potential loss?

## Output Structure
What the user receives:
- **Primary Output**: Failure scenarios with root cause analysis
- **Secondary Outputs**: Prevention strategies, early warning indicators, contingency plans
- **Format**: Structured risk register + prioritized action list + monitoring dashboard recommendations

## Key Principles
1. **Assume failure happened**: Don't ask "might this fail?" — ask "how did this fail?"
2. **Psychological safety**: Frame as learning exercise, not blame assignment
3. **Specificity matters**: Vague risks ("communication issues") become specific failures ("requirements doc v3 contradicted v2, team built wrong feature")
4. **Actionable outputs**: Every identified risk needs prevention, detection, or mitigation strategy

## Common Patterns

### Pattern: "Nothing could go wrong"
- **Indicators**: Team struggles to generate failure scenarios, excessive optimism
- **Approach**: Force specificity — "It's 18 months from now, the project was cancelled after burning $2M. Write the headline."
- **Output adjustments**: Start with extreme failure to break mental barriers, then work backwards

### Pattern: "We've thought of everything"
- **Indicators**: Team produces generic risks they claim to have mitigated already
- **Approach**: Challenge each mitigation — "That control failed. How?"
- **Output adjustments**: Introduce external perspective — "What would a competitor say will kill this?"

### Pattern: "Too many risks, paralysis"
- **Indicators**: Hundreds of failure scenarios, team overwhelmed
- **Approach**: Force prioritization — "If only 3 things kill this project, what are they?"
- **Output adjustments**: Create risk matrix (likelihood × impact), focus on top quadrant only

## Quality Checks
Before delivering output, verify:
- ✅ At least 5 distinct failure scenarios generated across different dimensions
- ✅ Each scenario traced to root cause (not just symptoms)
- ✅ Prevention strategies are specific and actionable (not "communicate better")
- ✅ Early warning indicators are observable/measurable
- ✅ Top 3-5 priorities clearly identified with owners recommended

## Examples

### Example 1: Product Launch Pre-Mortem
**Input**: 
"Launching new AI-powered analytics feature Q2. 6-month timeline, $500K budget, team of 8. Goal: 30% adoption by existing customers within 90 days of launch. Depends on new ML infrastructure and integration with legacy data platform."

**Output**:

**Failure Scenario 1: "Launch delayed 6 months, feature obsolete"**
- Root Cause: ML infrastructure dependencies underestimated; legacy platform integration required undocumented API reverse-engineering
- Prevention: 
  - Week 1-2: Spike on legacy platform integration complexity
  - Architectural review with platform team before sprint 1
  - Define "minimum viable integration" vs "ideal integration"
- Detection: 
  - Integration stories consistently miss estimates by >50%
  - Platform team unavailable for scheduled reviews
- Mitigation: 
  - Parallel track: manual data export process as fallback
  - Phased launch: start with customers on new platform only

**Failure Scenario 2: "Launched on time, 5% adoption (target 30%)"**
- Root Cause: Feature solved engineer problem, not customer problem; no customer validation during development
- Prevention:
  - Customer discovery interviews before sprint 1 (10+ target customers)
  - Weekly customer feedback sessions during development
  - Define adoption metrics upfront, instrument from day 1
- Detection:
  - Beta program sign-up rate <20%
  - Support tickets about feature confusion > threshold
- Mitigation:
  - Prepared education campaign (tutorials, webinars, in-app guidance)
  - Fast-follow iteration plan based on usage data

**Failure Scenario 3: "ML model accuracy degraded in production, trust lost"**
- Root Cause: Training data didn't represent production data distribution; no monitoring for drift
- Prevention:
  - Production data sampling for training set validation
  - Automated drift detection alerts
  - Human-in-the-loop validation for first 30 days
- Detection:
  - Model confidence scores dropping
  - Customer complaints about incorrect insights
- Mitigation:
  - Rollback procedure documented and tested
  - Manual review queue for low-confidence predictions

**Prioritized Actions:**
| Priority | Action | Owner | Timeline |
|----------|--------|-------|----------|
| 1 | Customer discovery interviews (10+) | PM | Week 1-2 |
| 2 | Legacy platform integration spike | Tech Lead | Week 1-2 |
| 3 | Define drift detection metrics | ML Engineer | Sprint 1 |
| 4 | Instrumentation plan for adoption tracking | Data Engineer | Sprint 1 |

### Example 2: Organizational Restructure Pre-Mortem
**Input**: "Merging two engineering teams (12 + 15 people) into single platform organization. 3-month transition. Goal: reduce duplication, improve velocity. Concerns about culture clash and key person risk."

**Output**:

**Failure Scenario 1: "Top 3 engineers from each team quit within 60 days"**
- Root Cause: Role ambiguity, perceived status loss, conflicting management directives during transition
- Prevention:
  - Individual conversations with key talent before announcement
  - Clear role definitions published Day 1
  - Retention bonuses or equity refresh for critical roles
- Detection:
  - Increased 1:1 cancellations
  - Passive job search signals (LinkedIn activity)
- Mitigation:
  - Emergency retention conversations playbook
  - Contractor bench ready for knowledge transfer

**Failure Scenario 2: "Velocity drops 50%, never recovers"**
- Root Cause: Decision-making bottlenecked by new leadership layer; teams waiting for alignment instead of executing
- Prevention:
  - Decision rights matrix defined before merge
  - Escalation SLA (48-hour max for blocking decisions)
  - Preserve team autonomy on implementation details
- Detection:
  - Stories stuck in "waiting" column >3 days
  - Meeting load increases >30%
- Mitigation:
  - Temporary "decision SWAT team" empowered to unblock
  - Revert to previous structure if velocity doesn't recover in 60 days

**Prioritized Actions:**
| Priority | Action | Owner | Timeline |
|----------|--------|-------|----------|
| 1 | Key talent retention conversations | VP Eng | Before announcement |
| 2 | Decision rights matrix | New Director | Week 1 |
| 3 | Baseline velocity metrics captured | EMs | Week 1 |
| 4 | 30/60/90-day check-ins scheduled | HR BP | Week 1 |

## Attribution
Adapted from Strategic Pre-Mortem framework  
Original methodology: Gary Klein, Daniel Kahneman  
Licensed for educational and commercial use
