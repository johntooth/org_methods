# Estimation Principles

## Core Philosophy

**Estimates exist to support decisions, not to predict the future.**

If an estimate won't change a decision, don't create it. The cost of estimation often exceeds the value of the information gained.

## Anti-Patterns

### 1. Estimating Low-Clarity Work

**Problem:** Providing point estimates for work with ambiguous requirements or unknown dependencies.

**Why it fails:**
- Creates false precision and confidence
- Becomes a commitment before understanding exists
- Leads to blame when estimates prove wrong
- Wastes time on speculation

**Better approach:**
- Declare "DO NOT ESTIMATE" explicitly
- Propose timeboxed discovery (1-3 days)
- Define learning objectives for the spike
- Re-assess clarity after discovery

### 2. Over-Investing in Estimation

**Problem:** Spending hours debating story points or hours for uncertain work.

**Rule of thumb:** Never spend more time estimating than you would save by preventing a bad decision.

**Examples:**
- ❌ 2-hour planning poker session for a $500 decision
- ✅ 10-minute clarity assessment, then timeboxed spike
- ❌ Detailed breakdown of unknown integration work
- ✅ "We need sandbox access before we can estimate"

### 3. Treating Estimates as Commitments

**Problem:** Converting estimates into deadlines without accounting for uncertainty.

**Why it fails:**
- Ignores the inherent uncertainty in knowledge work
- Creates pressure to cut corners
- Damages trust when dates slip
- Discourages honest estimation

**Better approach:**
- Use ranges for medium-clarity work: "3-5 days assuming X"
- State assumptions explicitly: "This estimate assumes no API changes"
- Separate estimates from commitments: "Here's our best guess; here's what we're committing to"
- Re-estimate when assumptions change

### 4. Estimating Without the Doers

**Problem:** Managers or architects estimating work that developers will execute.

**Why it fails:**
- Missing implementation details only doers know
- Removes ownership from the team
- Creates resentment and disengagement
- Less accurate than collaborative estimation

**Better approach:**
- Bring experts together in collaborative sessions
- Let the people who will do the work provide estimates
- Use estimation as a team alignment tool, not just prediction

### 5. Ignoring Clarity Levels

**Problem:** Applying the same estimation approach to all work items.

**Better approach by clarity:**

| Clarity | Estimation Method | Output | Confidence |
|---------|------------------|--------|------------|
| **HIGH** | Team consensus | Point estimate | High - treat as commitment |
| **MEDIUM** | Range with assumptions | "3-5 days if X is true" | Medium - validate assumptions first |
| **LOW** | No estimation | "Need 2-day spike first" | None - discovery required |

## Decision Framework

### When to Estimate

✅ **Estimate when:**
- Clarity is HIGH (specific requirements, known domain)
- The estimate will change a decision (go/no-go, priority ordering)
- The team has relevant experience
- Dependencies are resolved
- Success criteria are clear

❌ **Don't estimate when:**
- Clarity is LOW (ambiguous problem, new domain)
- The decision is already made regardless of estimate
- Major dependencies are unresolved
- You're estimating someone else's work
- More than 20% of the work is unknown

### When to Spike Instead

Run a timeboxed discovery spike when:
- You can't answer "What exactly are we building?"
- Key technical approaches are unproven
- External dependencies (APIs, vendors) are unvalidated
- Team has zero relevant experience
- Requirements conflict or are incomplete

**Spike output should be:**
- Specific answers to unknown questions
- Working prototype or proof of concept
- Updated clarity assessment
- Basis for confident estimation

## Practical Techniques

### 1. Clarity-First Conversations

Before discussing estimates, ask:
- "What parts are unclear?"
- "What have we not done before?"
- "What dependencies haven't we validated?"
- "If this failed, what would be the most likely reason?"

### 2. Assumption Surfacing

For every estimate, document:
```
Estimate: 5 days
Assumptions:
- API documentation is accurate
- No security review delays
- Test environment available
- Team member X available full-time
```

If any assumption is uncertain, reduce confidence level.

### 3. Range Estimation

Instead of single numbers, use ranges:
- **Optimistic:** Everything goes perfectly (2 days)
- **Realistic:** Normal conditions (4 days)
- **Pessimistic:** Things go wrong (8 days)

The spread indicates uncertainty level.

### 4. Reference Class Forecasting

Look at similar past work:
- "The last OAuth migration took 3 weeks"
- "Our payment integrations average 5 days"
- "Dashboard performance work typically reveals unexpected complexity"

Use historical data over gut feel.

### 5. Timebox Discovery

When clarity is low, propose:
```
"We don't know enough to estimate. 
Let's spend 2 days:
- Validating the payment provider API
- Building a minimal integration prototype  
- Documenting compliance requirements

After that, we'll provide a confident estimate."
```

## Metrics That Matter

Track these instead of estimate accuracy:

1. **Clarity Velocity:** How quickly do items move from LOW → MEDIUM → HIGH clarity?
2. **Discovery ROI:** What percentage of spikes lead to successful delivery vs. pivots?
3. **Decision Quality:** How often do estimates actually change decisions?
4. **Team Confidence:** Does the team feel estimates are realistic and owned?

## Quick Reference

### Red Flags 🚩

- "Just give me a rough guess" → Rough guesses become commitments
- "We'll figure out the details later" → Details are where risks hide
- "This should be simple" → Unexamined complexity
- Estimating in isolation → Missing collective wisdom
- Pressure to reduce estimates → Creating unrealistic expectations

### Green Lights ✅

- "We need more information before estimating" → Healthy boundary
- "Here's our range and the assumptions behind it" → Transparent communication
- "Let's run a spike first" → Appropriate discovery
- Team collectively owns estimates → Shared accountability
- Re-estimating when scope changes → Adaptive planning

---

*Part of the Backlog Filter Skill framework*  
*Original principles by Kim Ballestrin and Dr. Saeed Shalbafan*
