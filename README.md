# Business Startup Cost Estimator — Claude Skill

A source-aware Claude skill for answering: **How much money do I really need to start this business?**

Designed for coffee shops, restaurants, retail, studios, workshops, light manufacturing, ecommerce, and service businesses.

## Produces
- Minimum / realistic / premium startup scenarios
- Detailed CAPEX and pre-opening budget
- Deposits and non-expense cash requirements
- Opening inventory
- Hiring and training
- Launch marketing
- Monthly OPEX
- 3- and 6-month working capital
- Contingency
- Total funding requirement
- Break-even revenue and units/customers
- Sensitivity analysis
- Hidden-cost checklist
- Regulatory/licensing checklist
- Source and confidence tracking

## Example
> Estimate the full amount of capital I need to open an 80 m² specialty coffee shop in Girne, with 30 seats, one 2-group espresso machine, 4 staff, mid-premium positioning, and six months of working capital.

## Structure
```text
business-startup-cost-estimator/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
├── templates/
├── scripts/
└── examples/
```

## Installation
Copy this folder into the skills directory used by your Claude/agent environment. `SKILL.md` is the primary instruction file.

## Accuracy
This skill is a planning tool, not legal, tax, architectural, or regulated professional advice. Verify permits, taxes, fire/food rules, employment law, and construction requirements with current official local sources.

## License
MIT
