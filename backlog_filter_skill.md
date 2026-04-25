---
name: backlog_filter
description: >
  Use this skill when prioritizing backlog items or deciding what work to tackle next.
  Analyzes work items by clarity of understanding (not size/complexity) and outputs
  prioritization recommendations, sequencing logic, and action plans. Handles roadmaps,
  user stories, features, or any work items needing prioritization. Even if they don't
  explicitly mention "backlog" or "prioritization" — any situation where you need to
  decide what to work on first based on risk and understanding level.
---

# Backlog Filter

## Purpose
Filter and prioritize upcoming work based on **clarity of understanding**, not complexity or size — high-clarity work proceeds confidently when resourced, low-clarity work requires discovery before commitment.

## Core Principle
**Clarity ≠ Complexity**: A large, well-understood feature is lower risk than a small, ambiguous one. Map work by understanding level to apply appropriate action logic.

---

## When to Use This Skill
- User needs to prioritize work items, backlog, roadmap, or project queue
- User is deciding what to work on next and needs risk-based sequencing
- User has multiple work items and needs to determine which are ready vs need discovery
- Context: sprint planning, roadmap creation, portfolio prioritization, release planning

**Do NOT use this skill when:**
- User needs detailed task breakdown or effort estimation without clarity assessment
- User wants to skip discovery and just get estimates (this skill prevents that)
- Adjacent tasks: use `strategy_ecosystem_mapper` for competitive landscape analysis

## Input Requirements
What the user needs to provide:
- **Required**: List of work items (titles + brief descriptions minimum)
- **Optional**: Known dependencies, stakeholder concerns, timeline pressures
- **Format**: Any format — bullet list, user stories, roadmap items, features, epics

## Processing Steps

### Step 1: Assess Clarity Level
For each work item, evaluate 5 dimensions:
1. **Requirements Clarity**: Is "done" clearly defined?
2. **Technical Approach**: Is implementation path understood?
3. **Dependencies**: Are external needs identified and resolvable?
4. **Expertise**: Does team have/access to required skills?
5. **Acceptance Criteria**: Can specific success measures be defined?

**Classification:**
- 🔵 **High Clarity**: All 5 dimensions are clear → Can proceed
- 🟡 **Medium Clarity**: 2-4 dimensions unclear → Needs discovery
- 🔴 **Low Clarity**: 0-1 dimensions clear → Cannot estimate or commit

### Step 2: Apply Sequencing Logic
For items classified, apply three sequencing principles:
1. **Dependencies First**: Pull forward work that blocks other teams
2. **Cost of Delay**: Prioritize by value lost if waiting
3. **Learning Value**: Sequence items that reduce uncertainty for others

### Step 3: Generate Action Plans
By clarity level:
- **High Clarity**: Sequence → Assign → Estimate → Execute
- **Medium Clarity**: Time-box discovery → Experiments → Re-assess
- **Low Clarity**: Research → Expert consultation → Learning backlog

## Output Structure
What the user receives:
- **Primary Output**: Categorized work items (High/Medium/Low clarity) with action recommendations
- **Secondary Outputs**: Sequenced priority order, dependency map, discovery plans for unclear items
- **Format**: Structured table + narrative explanation + next steps

## Key Principles
1. **Clarity ≠ Complexity**: Large + clear is safer than small + ambiguous
2. **Estimates are for decisions**: Never spend more on estimation than the decision is worth
3. **Discovery before commitment**: Low-clarity work gets learning investments, not deadlines
4. **Dependencies de-risk first**: Work blocking others gets priority

## Common Patterns

### Pattern: "Everything feels urgent"
- **Indicators**: User says all items are high priority, no clear sequencing
- **Approach**: Force clarity assessment first, then apply cost of delay question: "What happens if we wait 3 months?"
- **Output adjustments**: Emphasize that High Clarity + High Cost of Delay = true priority

### Pattern: "Just give me an estimate"
- **Indicators**: User demands estimates for unclear work
- **Approach**: Refuse to estimate Low/Medium clarity items; estimate discovery work instead
- **Output adjustments**: Provide discovery timeline ("2-week spike") not delivery timeline

### Pattern: "Hidden dependencies"
- **Indicators**: Items seem independent but team mentions waiting on others
- **Approach**: Explicitly ask "Who is blocked waiting for this?" for each item
- **Output adjustments**: Re-sequence to pull dependent work forward

## Quality Checks
Before delivering output, verify:
- ✅ Each item is classified with justification (which clarity dimensions are clear/unclear)
- ✅ Sequencing rationale references dependencies or cost of delay explicitly
- ✅ Low-clarity items have specific discovery activities, not vague "learn more"
- ✅ No estimates provided for Low-Clarity items (only discovery estimates)

## Examples

### Example 1: Product Roadmap Prioritization
**Input**: 
- "Mobile app redesign" - marketing wants it Q1
- "API v2 migration" - engineering knows scope, 3 teams depend on it
- "AI feature exploration" - leadership heard about AI, no specifics yet

**Output**:
| Item | Clarity | Action | Priority Rationale |
|------|---------|--------|-------------------|
| API v2 migration | 🔵 High | Sequence & estimate | Blocks 3 teams, de-risks delivery |
| Mobile app redesign | 🟡 Medium | 1-week discovery on technical approach | Marketing urgency but unclear implementation |
| AI feature exploration | 🔴 Low | Learning backlog: market research + prototype | Cannot estimate without problem definition |

### Example 2: Sprint Planning
**Input**: "We have 8 user stories for sprint planning. Story A-C have clear acceptance criteria and the team built similar features before. Story D-F mention 'integrate with partner API' but we don't know their capabilities yet. Story G-H are large refactoring efforts the team understands well."

**Output**: 
- **Proceed to estimation**: Stories A-C, G-H (High Clarity)
- **Discovery sprint needed**: Stories D-F (Low Clarity - unknown dependencies)
- **Sequencing**: If D-F are blockers, start with 1-week spike to understand partner API before committing

## Attribution
Original framework by Kim Ballestrin and Dr. Saeed Shalbafan  
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)
