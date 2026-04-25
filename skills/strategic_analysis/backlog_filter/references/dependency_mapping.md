# Dependency Mapping Techniques

## Why Map Dependencies?

Unidentified dependencies are the primary cause of delivery delays. Mapping them early allows you to:
- Sequence work to de-risk delivery
- Identify cross-team coordination needs
- Expose hidden bottlenecks before they block progress
- Make informed prioritization decisions

## Dependency Types

### 1. Technical Dependencies

**Definition:** Work items that require other technical components to exist first.

**Examples:**
- API must be built before frontend can integrate
- Database schema changes before data migration
- Authentication service before user-facing features

**Identification questions:**
- "What systems/components must exist before we can start?"
- "What interfaces need to be defined?"
- "Are there infrastructure prerequisites?"

### 2. Knowledge Dependencies

**Definition:** Work requiring specific expertise or information held by others.

**Examples:**
- Need domain expert to clarify business rules
- Require security team review before deployment
- Waiting for vendor documentation

**Identification questions:**
- "Who has knowledge we need?"
- "What don't we understand yet?"
- "Whose input is required before we can proceed?"

### 3. Temporal Dependencies

**Definition:** Work that must happen in a specific sequence due to timing constraints.

**Examples:**
- Marketing campaign must coordinate with feature launch
- Training materials needed before user rollout
- Compliance audit before production deployment

**Identification questions:**
- "What external events constrain our timeline?"
- "What must happen in parallel vs. sequence?"
- "Are there regulatory or compliance gates?"

### 4. Resource Dependencies

**Definition:** Competition for shared resources (people, environments, tools).

**Examples:**
- Same developer assigned to multiple critical items
- Shared test environment booked by another team
- Limited budget across competing initiatives

**Identification questions:**
- "Who else needs this resource?"
- "Are there capacity conflicts?"
- "What happens if the resource isn't available when needed?"

## Mapping Techniques

### Technique 1: Dependency Matrix

Create a simple grid showing relationships between work items.

**Format:**
```
        | Item A | Item B | Item C | Item D |
--------|--------|--------|--------|--------|
Item A  |   -    |   ←    |   →    |   -    |
Item B  |   →    |   -    |   -    |   ←    |
Item C  |   ←    |   -    |   -    |   -    |
Item D  |   -    |   →    |   -    |   -    |
```

**Legend:**
- `→` : This item depends on column item
- `←` : Column item depends on this item
- `-` : No direct dependency

**When to use:** Small sets of items (5-15), quick visual scan

### Technique 2: Dependency Flow Diagram

Visual map showing directional flow of dependencies.

**How to create:**
1. Write each item on a sticky note or card
2. Arrange items left-to-right by intended sequence
3. Draw arrows from dependent items to their prerequisites
4. Look for patterns (bottlenecks, cycles, long chains)

**Patterns to identify:**
- **Bottleneck:** One item with many incoming arrows (blocks everything)
- **Chain:** Long sequence of dependencies (high risk, slow feedback)
- **Cycle:** Circular dependencies (must be broken)
- **Island:** Items with no dependencies (can start anytime)

**When to use:** Team workshops, complex initiatives, visual thinkers

### Technique 3: Pre-Mortem for Dependencies

Imagine the project failed and work backward to identify what dependencies were missed.

**Process:**
1. Assume it's 3 months from now and delivery failed spectacularly
2. Ask: "What dependencies did we fail to identify?"
3. For each answer, add to dependency map
4. Create mitigation plans for newly discovered dependencies

**Prompt examples:**
- "We couldn't start because we were waiting on..."
- "We didn't realize we needed access to..."
- "The integration failed because we assumed..."

**When to use:** High-stakes projects, teams with history of missed dependencies

### Technique 4: Cross-Team Interface Mapping

For multi-team initiatives, explicitly map team boundaries and handoffs.

**Template:**
```
Team A → Team B Interface
--------------------------
What Team A provides:
- [Deliverable 1]
- [Deliverable 2]

What Team A needs from Team B:
- [Requirement 1]
- [Requirement 2]

Integration points:
- [API endpoint / contract]
- [Shared data model]
- [Coordination meetings]

Risks:
- [Risk 1 with mitigation]
- [Risk 2 with mitigation]
```

**When to use:** Multi-team initiatives, organizational launches

## Sequencing Strategies

Once dependencies are mapped, use these strategies to order work:

### Strategy 1: Dependency-First Sequencing

**Rule:** Always do prerequisite work before dependent work.

**Rationale:** Reduces risk of rework, exposes integration issues early.

**Example:**
1. Build authentication API (prerequisite)
2. Build user management UI (depends on auth API)
3. Build password reset feature (depends on both)

### Strategy 2: Risk-Based Sequencing

**Rule:** Among items with similar dependencies, do highest-risk first.

**Rationale:** If high-risk items will fail, discover it early when course-correction is cheaper.

**Risk factors:**
- New technology/domain for team
- External dependencies outside your control
- Complex integrations
- Regulatory/compliance requirements

### Strategy 3: Value-Flow Sequencing

**Rule:** When dependencies allow, prioritize items that deliver value independently.

**Rationale:** Generates early wins, builds momentum, provides learning.

**Look for:**
- Items with no outgoing dependencies (nothing waits on them)
- Items that deliver user value without waiting for other work
- Quick wins that build confidence

### Strategy 4: Parallel Path Optimization

**Rule:** Maximize parallel work streams while respecting dependencies.

**Approach:**
1. Identify independent work streams
2. Assign separate teams/resources to each stream
3. Plan integration points explicitly
4. Buffer time for integration surprises

## Common Anti-Patterns

### ❌ Hidden Dependencies

**Problem:** Dependencies exist but aren't documented or visible.

**Symptoms:**
- "Oh, we also need X" discovered mid-sprint
- Work blocked unexpectedly
- Blame games between teams

**Prevention:**
- Explicit dependency mapping in planning
- Regular dependency reviews
- Cross-team visibility sessions

### ❌ Dependency Chains

**Problem:** Long sequences where each item waits on the previous one.

**Symptoms:**
- Slow delivery velocity
- Late discovery of problems
- Single points of failure

**Prevention:**
- Break chains by finding parallel paths
- Invest in modular architecture
- Create stubs/mocks to decouple work

### ❌ False Dependencies

**Problem:** Assuming dependency exists when it doesn't.

**Symptoms:**
- Unnecessary waiting
- Over-engineering "just in case"
- Missed opportunities for parallel work

**Prevention:**
- Challenge every dependency: "Do we really need this first?"
- Prototype to validate assumptions
- Separate hard constraints from soft preferences

### ❌ Dependency Hoarding

**Problem:** One team/item accumulates too many dependencies.

**Symptoms:**
- Bottleneck team overwhelmed
- Everything waits on one thing
- Single point of failure

**Prevention:**
- Distribute dependencies across teams
- Invest in self-service platforms
- Decouple architectures

## Tools and Artifacts

### Simple Dependency Log

```markdown
| Item | Depends On | Type | Status | Owner | Mitigation |
|------|------------|------|--------|-------|------------|
| Feature A | API Contract | Technical | Resolved | Team X | Contract signed off 2024-01-15 |
| Feature B | Security Review | Knowledge | Pending | Security Team | Scheduled for 2024-01-20 |
```

### Visual Board Layout

For physical or digital boards:
- Use colored strings/arrows to show dependencies
- Red = blocking dependency
- Yellow = soft dependency/preference
- Green = resolved dependency

### Integration Checklist

For each identified dependency:
- [ ] Dependency clearly defined
- [ ] Owner assigned
- [ ] Timeline agreed
- [ ] Integration approach documented
- [ ] Test strategy defined
- [ ] Rollback plan if integration fails

## Metrics to Track

1. **Dependency Discovery Rate:** How many new dependencies found per sprint? (Should decrease over time)
2. **Dependency Resolution Time:** Average time from identification to resolution
3. **Blocked Time:** Percentage of sprint time lost to waiting on dependencies
4. **Cross-Team Dependencies:** Count of dependencies requiring other teams (indicator of coupling)

---

*Part of the Backlog Filter Skill framework*  
*Original framework by Kim Ballestrin and Dr. Saeed Shalbafan*
