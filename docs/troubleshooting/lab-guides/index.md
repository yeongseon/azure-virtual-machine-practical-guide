---
description: Azure Virtual Machines troubleshooting lab guides hub — planned reproducible experiments, lab methodology, and the current scaffolded lab catalog.
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
| Extension Failures | [Extension Failures](../playbooks/connectivity/extension-failures.md) | Scaffolded | Reproduces a deterministic Custom Script extension failure and falsifies it with a successful redeploy. |
| Cannot RDP or SSH | [Cannot RDP or SSH](../playbooks/connectivity/cannot-rdp-or-ssh.md) | Scaffolded | Reproduces a deterministic admin-path connectivity failure where an NSG deny rule blocks inbound TCP 22 even though the VM remains healthy. |

## Why this is a scaffold

This page intentionally stays focused on the hub and lab shape. Individual troubleshooting labs are authored separately so each experiment can be reviewed as a focused, evidence-rich document instead of a placeholder bundle.

## See Also

- [Troubleshooting](../index.md)
- [Playbooks](../playbooks/index.md)
- [Cannot RDP or SSH](../playbooks/connectivity/cannot-rdp-or-ssh.md)
- [Extension Failures](../playbooks/connectivity/extension-failures.md)
- [Tutorial Lab Guides](../../tutorials/lab-guides/index.md)
