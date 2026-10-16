# Project rules

This is a template: adapt it to the actual repository and task before installation.
Remove sections that do not apply. It supplements personal rules rather than
duplicating them. Do not invent commands, access, or approvals; explicitly mark
anything unknown.

## Purpose and sources

Briefly describe the product and expected outcome. Identify the existing sources:
the main README, runtime/architecture, UI, data, and deployment documentation.
Clarify which sources describe required behavior and which are historical reports.

## Environment and verification

Record the current project's actual commands for running, checking, and building it.
State whether container/shared-service lifecycle operations are authorized and where
test data is located. Do not copy Docker/just/Next.js from the source projects if this
project uses a different stack.

## Invariants

Specify the product's own constraints, data owners, shared UI, precision of monetary
data where applicable, and compatibility boundaries. Document customer settings and
permissions to change them separately.

## Delivery and permissions

Record the current permissions for commit, push, PR, merge, and deployment, the target
branch/environment, and explicit prohibitions. Do not transfer permissions from
another project. If they have already been granted in the task, do not ask for them
again. If the project has a production environment, specify the runbook, checks,
and risk-based backup and rollback requirements.

## Optional procedures

Add the references below only after installing the corresponding files and only
for the relevant areas; do not leave references to missing files.

- For LLM behavior: the prompt-engineering skill.
- For quality/cost audits and release impact: the evidence-audit skill.
- For releases: the locally adopted release-policy.md and the specific runbook.
- For money/webhooks/ledgers: money-events.md and the local contract.
