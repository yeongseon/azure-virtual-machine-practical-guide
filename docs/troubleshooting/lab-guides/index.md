---
description: Azure Virtual Machines troubleshooting lab guides hub — planned reproducible experiments, lab methodology, and the first scaffolded lab candidate.
---

# Lab Guides

These troubleshooting labs turn VM failure scenarios into reproducible experiments. Use this hub to find upcoming labs, understand the lab methodology, and see how each lab pairs with an existing troubleshooting playbook.

## What belongs here

- Reproducible failure scenarios, not general how-to tutorials.
- Evidence-driven experiments that validate or falsify a troubleshooting hypothesis.
- Companion material for canonical playbooks when a scenario benefits from hands-on reproduction.

## Canonical lab shape

Future labs in this section will follow the series lab-guide contract:

1. `## Lab Metadata`
2. `## 1) Background`
3. `## 2) Hypothesis`
4. `## 3) Runbook`
5. `## 4) Experiment Log`
6. Evidence section using either:
    - `## Expected Evidence`, or
    - `## 5) Verification Queries` and `## 6) Portal Evidence`
7. `## Clean Up`
8. `## Related Playbook`
9. `## See Also`
10. `## Sources` when external references are cited

Within that structure, each lab is expected to cover the full troubleshooting methodology: question, setup, hypothesis, prediction, experiment, execution, observation, measurement, analysis, conclusion, falsification, evidence, solution, prevention, takeaway, and support takeaway.

## Planned lab catalog

| Planned lab | Paired playbook | Status | Notes |
|---|---|---|---|
| Extension Failures | [Extension Failures](../playbooks/connectivity/extension-failures.md) | Scaffolded | First candidate for a reproducible lab based on VM agent health, outbound connectivity, OS support, and extension payload troubleshooting. |

## Why this is a scaffold

This page intentionally stops at the hub and starter shape. The first full troubleshooting lab will be authored separately so the initial lab can be reviewed as a focused, evidence-rich experiment instead of a placeholder.

## See Also

- [Troubleshooting](../index.md)
- [Playbooks](../playbooks/index.md)
- [Extension Failures](../playbooks/connectivity/extension-failures.md)
- [Tutorial Lab Guides](../../tutorials/lab-guides/index.md)
