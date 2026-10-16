---
name: evidence-audit
description: Evaluate quality, release effects, or AI costs across repeated observation windows while retaining comparable evidence and unresolved findings. Use for before-and-after audits and model comparisons.
---

# Evaluate changes across observation windows

1. Carry forward the baseline and stable finding IDs. For each intervention, record
   its hypothesis, actual activation time, expected observable effect, and opposite
   failure. Separate intended changes from what was running during the sample.
2. Declare scope, time boundaries, eligibility, sampling, and evaluation criteria
   before assessing outcomes. Keep a repeatable general sample separate from a
   sample targeting known defects. Include missing and failed outcomes in the
   appropriate denominator; successful outputs alone cannot establish a failure rate.
3. Compare equivalent cases and record changes in their mix or operating conditions.
   Evaluate the first outcome separately from later corrections and recovery.
   Report eligible, reviewed, and affected counts; equal window lengths do not
   establish comparability.
4. Classify each intervention as improved, persisting, regressed, not exercised,
   or inconclusive. Zero eligible cases means not exercised. Distinguish an observed
   difference from evidence that the intervention caused it.
5. Append a dated result without replacing earlier baselines. Carry unresolved
   findings forward and state what the next window needs to exercise. Publish
   sanitized evidence and aggregates sufficient to assess the conclusion.

For model cost comparisons, keep inputs identical apart from the declared treatment;
record model settings, sampling/order, retries, cache behavior, and routing differences.
Separate actual charges from normalized estimates. Unmatched workloads or cache
conditions cannot establish a model cost ranking. Count retries toward the agreed
experiment budget.
