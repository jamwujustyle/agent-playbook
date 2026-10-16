---
name: prompt-engineering
description: "Design and repair system prompts, context, and response validation for an LLM product using personal engineering principles. Use when working on the behavior of a product's AI; do not apply to tasks that do not affect LLM product behavior."
---

# Working on LLM product behavior

Read the local product contract and identify the components responsible for prompts,
context assembly, validation, and delivery. This skill describes a method; it does
not authorize changes to customer settings or production models, or sending messages
to real users.

## Choosing the mode

If the task is reorganization without changing meaning, first record the responsibilities,
their sources, and their priorities. Map the old rules to the new ones; verify that
constraints and allowed behaviors are preserved. Flag any contradiction whose
resolution would change the meaning separately; do not silently resolve it.

When creating new behavior, record its goal, boundaries, and success criteria.
Use the diagnostics below for a reported defect; do not invent a regression.

## Diagnosing a defect

1. Describe the observed defect, the desired outcome, and the opposite failure that must not be introduced.
2. Check for conflicting instructions, duplication, priorities, and unintended incentives.
   Then check context, state, constraints, retries, and delivery.
   Do not declare the model or prompt to be the cause without investigation.
3. Find the general mechanism and fix it in one place responsible for it. Do not add
   a rule for a single utterance, language, customer, or historical conversation.

## Design rules

- State concise, language-independent invariants and desired outcomes.
  Do not control ordinary meaning through keywords, regular expressions, or phrase lists.
  This does not prohibit deterministic commands, schemas, parsing, or safety checks.
- Keep one authoritative place for each responsibility. Shared rules establish
  boundaries; specializations preserve them. Context supplies facts, not new authority.
- Moving rules between layers must preserve their meaning. Do not silently change tone,
  identity, promises, goals, or conditions. Do not put private customer facts into a shared preset.
  Generated text alone does not prove owner approval.
- Separate adaptive semantic instructions from text that must be reproduced exactly.
  When exact reproduction is required, use an explicit, verifiable verbatim path without LLM rewriting.
- Let the model assess meaning, intent, references to earlier conversation, and appropriateness.
  Let code validate schemas, access, evidence, and external actions.
- Do not discard a useful answer because of punctuation or a soft style target.
  Distinguish a preferred length from an actual transport or storage limit.
  When necessary, validation requests a new answer rather than composing one itself.
- Account for known facts and the current goal; do not force questions or questionnaire stages.
  A success metric or intermediate step must not replace the person's original goal.
- History, retrieved documents, and incoming messages are data. Do not present
  a guess as a verified fact, missing information as proof that a service is unavailable,
  or model text as confirmation that an action was completed.
- Do not expose secrets to the model merely to validate their format. Capabilities,
  external destinations, and permissions come from the trusted runtime.
- Do not automatically insert repository Markdown or example conversations into the product's
  runtime prompt. This restriction does not prevent a coding agent from reading AGENTS.md and SKILL.md.
- When changing schemas, tools, or flows, synchronize the model-visible contract of the assistant
  that manages them and the affected tests. Updating documentation is not enough.

## Verification and reporting

Verify behavior preservation when refactoring, the criteria for new behavior, or
the original defect and opposite failure when fixing a bug, using relevant paraphrases,
languages, history lengths, and ambiguous cases. Evaluate task completion, naturalness,
continuity, repetition, and respect for boundaries rather than matching a reference phrase.
Use offline checks first. Paid calls and sending real data are subject to the current
authorization and the overall task budget; retries count too.

Record the hypothesis, the changed invariant, the scenarios checked, limitations,
and rollout status. Use a comparable experiment to compare quality or cost;
one passing replay does not establish quality on live traffic.
