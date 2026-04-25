---
name: strategy_ecosystem_mapper
description: >
  Use this skill when mapping competitive landscapes or making strategy accessible to diverse stakeholders.
  Applies the Corporate Forest metaphor to translate complex ecosystems into intuitive nature imagery
  (Giant Oaks, Fast Redwoods, Wildflowers, Kudzu disruptors, Bees/Birds customers). Outputs ecosystem
  maps, position hypotheses, resource flow analysis, and strategic leverage points. Even if they don't
  explicitly mention "ecosystem" or "Corporate Forest" — any situation where you need to understand
  competitive dynamics, market positioning, or strategic opportunities in a way everyone can engage with.
---

# Strategy Ecosystem Mapper

## Purpose
Make strategy accessible by mapping competitive landscapes using the Corporate Forest metaphor — enabling meaningful participation from all stakeholders regardless of strategic expertise.

## Core Principle
**Metaphor enables engagement**: When you articulate strategy as an ecosystem with familiar natural elements, non-strategists can contribute meaningfully to strategic conversations.

---

## When to Use This Skill
- User needs to understand competitive landscape or market positioning
- User is facilitating strategy discussions with diverse stakeholders
- User wants to identify strategic opportunities or threats
- Context: strategy offsites, board presentations, team alignment, market analysis

**Do NOT use this skill when:**
- User needs detailed financial modeling or quantitative market sizing
- User wants tactical execution planning (use `backlog_filter` for work prioritization)
- Adjacent tasks: use `premortem_analyzer` for risk assessment on strategic initiatives

## Input Requirements
What the user needs to provide:
- **Required**: Organization/company name and brief description of what they do
- **Required**: Known competitors or market segment
- **Optional**: Customer types, partners, investors, recent market changes
- **Format**: Any format — bullet list, narrative, links to research

## Processing Steps

### Step 1: Map the Corporate Forest
Categorize ecosystem participants using forest metaphors:

**Companies (Trees):**
- 🌳 **Giant Oak**: Dominant incumbent (Amazon, Microsoft) — controls resources, slow to change
- 🌲 **Fast Redwood**: Rising challenger (Tesla, TikTok) — rapid growth, gaining height quickly
- 🍁 **Maple Tree**: Adaptable player — changes strategies seasonally, survives through flexibility
- 🌸 **Dogwood**: Specialized niche — premium offerings, deep but narrow market
- 🌻 **Wildflowers**: Fast-growing startups — most die, few survive, beautiful but fragile
- 🌿 **Ferns**: Service providers/consultants — grow in shade of larger trees

**Relationships (Animals):**
- 🐝 **Bees**: Loyal customers who pollinate/spread word
- 🐦 **Birds**: Big customers who carry you to new markets
- 🍄 **Mushrooms**: Investors/VCs — feed on dead companies, help new growth

**Disruptors (Forces):**
- 🌿 **Invasive Kudzu**: Disruptors that change everything
- 🔥 **Fire**: Economic crashes/major disruptions
- 🌴 **Strangler Fig**: Platform businesses — starts small, eventually dominates

**Resources:**
- ☀️ **Sunlight**: Revenue/customer attention/market share
- 🌧️ **Rainfall**: Market awareness/brand visibility
- 🌱 **Soil Quality**: Talent, capital, strategic assets

### Step 2: Hypothesize Position
Determine where the organization sits in the forest:
- What tree type best describes current position?
- What leverage/access do they have?
- What resources are abundant vs scarce?
- Which direction is growth possible?

### Step 3: Identify Strategic Opportunities
Based on ecosystem map:
- Where are resource flows blocked or inefficient?
- Which relationships could be strengthened?
- What disruptor forces are emerging?
- Where can the organization carve unique position?

## Output Structure
What the user receives:
- **Primary Output**: Corporate Forest ecosystem map with all participants categorized
- **Secondary Outputs**: Position hypothesis, resource flow analysis, strategic opportunity areas
- **Format**: Visual metaphor description + actionable insights + discussion questions for stakeholders

## Key Principles
1. **Metaphor democratizes strategy**: Nature imagery makes abstract concepts concrete for everyone
2. **Position is dynamic**: Organizations can change tree types through strategic choices
3. **Resources flow to value**: Sunlight (revenue) goes where value is created
4. **Disruption is natural**: Kudzu and fire clear space for new growth

## Common Patterns

### Pattern: "We're invisible in the forest"
- **Indicators**: User says they're unknown, struggling for attention
- **Approach**: Map as Wildflower or Fern — identify path to Maple or Dogwood
- **Output adjustments**: Emphasize specific niche (Dogwood) or rapid adaptation (Maple) strategies

### Pattern: "Giant Oak crushing us"
- **Indicators**: User feels dominated by incumbent competitor
- **Approach**: Don't fight Oak directly — find unshaded sunlight, become Dogwood in niche
- **Output adjustments**: Identify Oak's blind spots, seasonal changes they can't make

### Pattern: "Kudzu is coming"
- **Indicators**: User sees disruptive threat emerging
- **Approach**: Map disruptor explicitly, identify whether to partner, acquire, or differentiate
- **Output adjustments**: Create early warning indicators, prepare response scenarios

## Quality Checks
Before delivering output, verify:
- ✅ Every major competitor assigned a tree type with justification
- ✅ Resource flows (sunlight, rainfall, soil) explicitly mapped
- ✅ Position hypothesis includes both current state and aspirational state
- ✅ At least 3 strategic opportunities identified from ecosystem dynamics

## Examples

### Example 1: SaaS Startup in Crowded Market
**Input**: 
"We're a project management tool for creative agencies. Competitors include Asana, Monday.com, Notion. We have 500 customers, mostly small agencies. Just raised Series A."

**Output**:
| Participant | Forest Type | Role |
|-------------|-------------|------|
| Asana, Monday.com | 🌳 Giant Oaks | Control mainstream sunlight (SMB market) |
| Notion | 🌲 Fast Redwood | Growing rapidly, expanding canopy |
| Your company | 🌻 Wildflower → 🌸 Dogwood path | Fragile now, can specialize for creative agencies |
| Creative agency customers | 🐝 Bees | Loyal, spread word within niche |
| Series A investors | 🍄 Mushrooms | Feeding growth, expect rapid scaling |

**Position Hypothesis**: Currently Wildflower (fragile, undifferentiated), path to Dogwood (specialized premium for creative agencies). Avoid direct sunlight competition with Oaks.

**Strategic Opportunities**:
1. Deep specialization: Become indispensable to creative agencies specifically
2. Partner with Birds: Large agency networks that can carry you to new markets
3. Soil investment: Hire talent with creative agency background (unfair advantage)

### Example 2: Traditional Retailer Facing Digital Disruption
**Input**: "Regional department store chain, 50 locations. Amazon and online retailers taking market share. Considering e-commerce investment."

**Output**:
| Participant | Forest Type | Role |
|-------------|-------------|------|
| Amazon | 🌳 Giant Oak + 🌴 Strangler Fig | Dominant incumbent AND platform enveloper |
| Online retailers | 🌲 Fast Redwoods | Growing fast, taking sunlight |
| Your company | 🌳 Aging Oak | Historically dominant, losing leaves |
| Local customers | 🐦 Birds (if retained) | Can carry you to community partnerships |
| Physical locations | 🌱 Soil quality | Underutilized asset if reimagined |

**Position Hypothesis**: Aging Oak facing Strangler Fig (Amazon platform). Cannot win on sunlight (price/selection) — must leverage unique soil (physical presence, community trust).

**Strategic Opportunities**:
1. Flip relationship: Make stores fulfillment centers for online (partner not compete)
2. Community canopy: Double-down on local events, experiences Amazon can't provide
3. Seasonal adaptation: Become Maple — pivot offerings by season/local needs

## Attribution
Original framework from Strategy Design methodology  
Adapted for AI skill implementation
