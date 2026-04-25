# Agent Skills Library

A curated collection of 7 AI agent skills for strategic analysis and planning acceleration.

## Quick Start

Skills are organized by category and follow the Agent Skills specification. Each skill includes:
- `SKILL.md` - Core skill definition with optimized trigger description
- `eval_queries.json` - Trigger evaluation test set (10 positive, 10 negative examples)
- `scripts/` - Optional executable scripts (when applicable)
- `references/` - Optional detailed reference documentation

## Available Skills

### Strategic Analysis (4 skills)

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **backlog_filter** | Prioritize work by clarity of understanding | Clarity assessment, sequencing, estimation guidance |
| **premortem_analyzer** | Sequential risk analysis for projects | Failure scenarios, root causes, prevention strategies |
| **strategy_ecosystem_mapper** | Corporate Forest competitive mapping | Ecosystem map, leverage points, strategic questions |
| **leadership_map_analyzer** | Integral Theory leadership assessment | Quadrant gaps, targeted interventions |

### Planning (3 skills)

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **rolling_plan_generator** | Now/Next/Later roadmap creation | Horizon-based plan with movement criteria |
| **persistent_activities_mapper** | Capacity allocation analysis | Activity inventory, capacity health indicators |
| **virtual_obeya_architect** | Visual management design | Tiered dashboard architecture, metrics |

## Skill Structure

```
skills/
├── strategic_analysis/
│   ├── backlog_filter/
│   │   ├── SKILL.md
│   │   ├── eval_queries.json
│   │   ├── scripts/batch_filter.py
│   │   └── references/
│   ├── premortem_analyzer/
│   │   ├── SKILL.md
│   │   └── eval_queries.json
│   ├── strategy_ecosystem_mapper/
│   │   ├── SKILL.md
│   │   └── eval_queries.json
│   └── leadership_map_analyzer/
│       ├── SKILL.md
│       └── eval_queries.json
└── planning/
    ├── rolling_plan_generator/
    │   ├── SKILL.md
    │   └── eval_queries.json
    ├── persistent_activities_mapper/
    │   ├── SKILL.md
    │   └── eval_queries.json
    └── virtual_obeya_architect/
        ├── SKILL.md
        └── eval_queries.json
```

## Trigger Evaluation

Each skill includes `eval_queries.json` with 20 test queries (10 should-trigger, 10 should-not-trigger) for validating description accuracy. Run trigger evaluation to optimize skill activation:

```bash
# Example evaluation workflow
for skill in skills/*/; do
  echo "Testing $skill..."
  # Run trigger evaluation script against eval_queries.json
done
```

## Usage Principles

1. **Action-Accelerating Tools** - All skills produce immediately usable outputs, not facilitation guides
2. **Timeless Elements** - Focus on enduring principles over trendy frameworks
3. **Structured Output** - Consistent formats enable downstream automation
4. **Quality Checks** - Built-in verification before delivery

## Attribution

Frameworks adapted from organizational development literature including works by Kim Ballestrin, Dr. Saeed Shalbafan, Gary Klein, and Integral Theory practitioners. Licensed under CC BY 4.0 where applicable.
