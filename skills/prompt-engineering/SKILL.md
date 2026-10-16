---
name: prompt-engineering
description: Diagnose or refactor an LLM application's prompts, context assembly, and response validation. Use when changing model behavior or fixing recurring response defects.
---

# Change LLM behavior at its cause

Establish whether the task preserves behavior or intentionally changes it. For a
refactor, map existing responsibilities and priorities before moving rules;
contradictions that change meaning need an explicit decision.

For a defect, describe the observed failure and the opposite failure a fix could
introduce. Trace the responsible instruction, supplied context, conversation state,
validation, and execution path before adding another prompt rule. Fix the general
cause in its owning component; avoid patches for a remembered phrase or transcript.

Use these design preferences:

- Express semantic goals and boundaries in the prompt. Keep deterministic commands,
  schemas, and execution constraints in code; do not approximate ordinary intent
  with growing keyword or phrase lists.
- Give each behavior one owner. Resolve conflicting instructions instead of
  repeating a rule more forcefully in several places.
- Separate adaptive wording from required verbatim text. Route exact text through
  an explicit path that does not depend on the model reproducing it.
- Treat soft style targets as preferences. A validator should not discard a useful
  answer solely for punctuation or preferred length, or invent replacement prose;
  request regeneration when correction is necessary.
- When changing tools, schemas, or executable flows, update the model-visible
  contract used to operate them in the same change. Documentation alone cannot do this.

Check the original and opposite failures with relevant paraphrases and context
variations. Judge the resulting behavior, not resemblance to a reference sentence.
Record the changed responsibility, checks, and remaining uncertainty. Keep paid
experiments within the agreed total budget, including retries.
