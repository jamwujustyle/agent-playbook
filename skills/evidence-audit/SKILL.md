---
name: evidence-audit
description: "Repeat audits of quality, release effects, or AI costs using comparable samples while preserving earlier findings. Use for live audits, before-and-after analysis, and model comparisons; not for routine code or build checks."
---

# Audits with verifiable conclusions

Start with the user's question, the latest report, the original baseline, and actual
releases. This skill does not grant production access or permission to send private
data to a provider, change configuration, or spend money. Use existing authorization;
if it is absent, prepare the methodology and clarify only the access needed.

## Set boundaries before reviewing results

- Define the exact period, time zone, snapshot, products or accounts, and inclusion criteria.
  Verify the actual version and cutover time; local code does not explain production behavior.
- Predefine a reproducible, bounded general sample and a separate sample targeting
  earlier defects. Include failures and missing results, not only successes.
- Preserve issue IDs, earlier symptoms, interventions, and unresolved dependencies.
  The next window continues the investigation rather than resetting the issue list.

## Assessing effects

- Compare like cases: scenario, stage, language, modality, and time of day
  when these affect the result. Equal window lengths do not make them equivalent.
- Separate the incoming event, attempt, authored result, delivery, and recovery.
  A later correction does not turn an initial failure into a successful first response.
  Distinguish an intentional pause from a lost response; mark pending and incomplete data.
- Account for intervening releases, owner publications, provider incidents, caching, and traffic mix.
  When a case crosses the cutover, record source, authoring, and delivery timestamps separately.
- For each intervention, choose a conclusion: improvement, persisting defect,
  regression, no eligible cases encountered, or insufficient evidence.
  Give the numerator, denominator, and limits of confidence. Do not attribute causality
  to an observed change without an appropriate comparison.

For repeat response audits, preserve the rubric: the first delivered authored
batch, useful progress, source grounding, continuity, configured style,
links or media, and pause or follow-up behavior. Distinguish errors in source reading,
context assembly, authoring or validation, delivery, and customer policy.

## Comparing models and costs

- Before paid requests, record the scenarios and payload hashes, verifying identical
  inputs apart from the declared treatment. Predeclare the order, sample size,
  quality criteria, cache policy, and one request budget for the entire task.
  Where possible, pin a common reviewed endpoint; if routes differ, record this
  as a limitation of the comparison.
- Count retries, fallback, and repairs against the same budget. Do not carry a numerical
  limit or payment authorization over from another project.
- Separate actual charges, provider-reported cost, calculations from pricing, and unknowns.
  A normalized estimate and an actual charge are different metrics.
- Account for the full cost of the chosen path and the actual denominators. Incomparable
  cache or routing conditions and different traffic cohorts cannot establish a savings ranking.

## Deliverable

Keep raw private data in a protected temporary location only within the authorized
scope. The final document and Git should contain sanitized findings, methodology,
and verifiable aggregates, without customer conversations, identifiers, or secrets.

Add a dated window without erasing earlier ones. For each change, record the earlier symptom,
hypothesis, revision and time, expected effect, eligible cases, and opposite failure.
Finish with what improved, what remains, and what the next traffic window must exercise.
Do not send artificial messages to real customers for an audit.
An audit alone does not authorize a release, a new runtime design, or a change to customer policy.
