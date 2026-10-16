# Rule provenance and reading limits

Snapshot: October 16, 2026, Asia/Almaty. This is an extraction of rules from local
documents, not an audit of code, production, or whether external research is still current.
Direct user rules from AGENTS are distinguished from generalizations of engineering
contracts. The portable wording is an editorial consolidation, not a verbatim quotation.

## Source map

The paths below are relative to their respective source repositories; line numbers
refer to the local snapshot that was read and may change later.

| Portable principle | Basis | Included in |
| --- | --- | --- |
| Relevant reading, code/tests as evidence of actual behavior, maintained documentation | Nara AGENTS:37–71; Lite AGENTS:38–90 | global |
| One owner for each rule, durable guidance separate from history | Nara and Lite docs/prompts.md:6–22, 67–80 | global, prompt-engineering |
| Fix the class of defects in a shared location | Nara docs/prompts.md:48–65; client/README:54–56; Lite client/README:251 | global, prompt-engineering |
| Shared UI, states, keyboard/touch/themes, preservation of user input | Nara client/README:78–93, 248–250, 632–638; Lite AGENTS:103–127; client/README:2409 | global |
| Exact amounts, compact display | Lite AGENTS:115; Partner Desk docs/commission-rules:51 | global, money-events |
| Small, verified commits and preservation of others' changes | Nara AGENTS:87–89; Lite AGENTS:455–463 | global |
| Accurate history and meaningful PRs | Lite AGENTS:546–625 | global, release-policy |
| Do not change customer settings | Partner Desk AGENTS:14; Lite AGENTS and docs/prompts | global |
| Separate environments, secrets, and development credentials | Nara AGENTS:94–104; Partner Desk README:37–41; Lite AGENTS:649–663 | global |
| Temporary resources belong to a task and have a defined end | Lite AGENTS:512–531 | global, release-policy |
| Visible reports, clear outcomes, accurate status | Lite AGENTS:627–650 | global |
| Requirements, proposals, and measurements are distinct sources | Partner Desk docs/affiliate-model-rationale:9–32, 93, 128 | global, evidence-audit |
| Shared invariants, semantics/determinism, the opposite failure | Nara and Lite docs/prompts.md | prompt-engineering |
| Synchronize the model-visible contract when the flow changes | Lite AGENTS:92–99 | prompt-engineering |
| Stable rubric, cutover, general/targeted samples, failure denominator | Lite AGENTS:150–210; docs/catalog-retrieval-eval:3 | evidence-audit |
| Comparable payloads, caching, actual/calculated cost | Lite AGENTS:64–77; docs/cost-audit, normative sections | evidence-audit |
| Backups scoped to risk, documentation-only releases, verification of what is actually running | Lite AGENTS:473–511, 614; Nara AGENTS:124–136 | release-policy |
| Verified events, exact monetary values, atomic/idempotent grants, immutable ledger | Lite docs/direct-service-payments:37, 90, 109; Partner Desk docs/integration:34–101, 126; commission-rules:93–107 | money-events |

## Conflict resolution

1. **Permissions were not combined.** Nara AGENTS:83–89 requires an explicit request
   for development-container lifecycle operations, push, and merge. Lite authorizes
   ongoing delivery. The shared foundation requires applying the current project's
   permissions; neither policy is automatically assigned to a new project.
2. **The stack was not generalized.** Nara/Lite use Docker/just and prohibit running
   Go/Node on the host; Partner Desk permits local Node. The principle of using the
   project's established commands was carried over. The preference to "not write
   comments for Go functions" (Nara AGENTS:90, Lite AGENTS:535) can be explicitly
   adopted in a local Go profile.
3. **Risk-based backups are a proposed portable profile.** Partner Desk
   deployment:35–36 requires a volume copy on every update. Lite's more recent
   practice requires backups scoped to risk. release-policy does not override
   Partner Desk's existing stricter rule without a separate change to its policy.
4. **History does not become a rule.** Old niche versions, withdrawn payment routes,
   incomplete integrations, and past rollout holds are not included in the shared
   set. Example: Lite prompt-layers-context:213 retains old pinning that has already
   been superseded by the current AGENTS and the beginning of that same document.
5. **A hypothesis does not become a universal fact.** The docs/prompts claim that
   "the cause is almost always excessive constraints" was replaced with a diagnostic
   sequence that can be tested.
6. **No prohibitions were invented.** No universal ban on fallbacks or tests was
   extracted: the sources prohibit inventing conversational content during validation
   and require relevant checks, but allow meaningful recovery mechanisms.
7. **The Markdown boundary was clarified.** The prohibition concerns automatically
   including repository documentation in the product's runtime prompts, not reading
   AGENTS/SKILL.
8. **Financial rules were made technically precise.** Atomicity applies to the local
   acceptance of proof, financial recording, and entitlement grants. An external
   network requires state reconciliation; no promise of a shared transaction with
   that network was added.

## What was deliberately left in the projects

Addresses, domains, SSH commands, server paths, secrets, customers, bot IDs, unlimited
entitlements, specific financial terms, roles and budgets, model settings, gambling
tone, payment histories, permissions for specific operations, and deployment
authorization. Original private text, raw conversations, and credentials were not
copied into the shared package.

## Coverage

- Nara: all 10 authored Markdown files found were read in full (4,397 lines).
- Partner Desk: all 7 authored Markdown files were read in full (573 lines);
  OpenAPI text descriptions were also read, without a full review of its schemas.
- Lite: all 48 visible Markdown files outside credentials and generated/vendor
  content were inventoried. AGENTS, prompts, direct-service-payments,
  catalog-retrieval-eval, and notes were read in full; the rest were covered by
  reviewing headings, searching for normative wording, and reading the relevant
  sections. The large deployment/engine/cost-audit logs and historical reports were
  not read in full line by line. This is complete coverage of the document inventory
  for rule extraction, not a claim to have read all of Lite's approximately 33
  thousand lines. notes was used only for cross-checking, not as a normative source.
- credentials, .env, raw customer backups, vendor, and generated content were not used.
- Production, external systems, and the validity of commercial research were not checked.
- The source projects were not edited. Existing uncommitted working-tree changes
  were preserved.


The detailed source-file inventory, local checkout paths, and revisions are retained
in a separate local report. They are not needed for installation and are not included
in the public package. The map above preserves the provenance of the portable
principles.
