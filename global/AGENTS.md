# Personal working rules

Apply these preferences to the current task. User instructions and project-specific
rules refine their scope. This file does not transfer another project's permissions,
access rights, or business terms.

## Work and sources

- Before changing an area, read its current instructions and documentation.
  Use the documentation map; do not load the entire project history for every task.
- To establish actual current behavior, inspect executable code and tests, then
  maintained documentation. Old plans and reports do not prove current status.
  The task defines the desired new behavior; an existing code defect does not.
- Fix the cause with the smallest general change. Preserve the existing intent;
  reorganizing code or instructions does not authorize changes to product policy.
- Use the current project's commands and environment. Do not impose Docker,
  a language, framework, provider, or architecture from another project.
- When behavior changes, update the relevant maintained document with the code.
  Give each rule one current authoritative source. Keep lasting principles
  separate from settings, incidents, and release history.
- Do not change customer settings, terms, permissions, or stored data for
  implementation convenience without the corresponding authorization. If the
  solution depends on such a change, explain that dependency.

## Quality and interface

- Before changing UI, inspect the nearest existing screen and shared components.
  Reuse controls, themes, and visual conventions; extend shared components as needed.
- Check the affected flow at supported screen sizes and in supported themes.
  For interactive controls, check focus, keyboard use, nested menus, and Escape.
  Account for touch and reduced motion. Cover the affected loading, empty, error,
  success, unavailable, and conflict states. Preserve entered data on failures;
  a late response must not overwrite newer state. Do not expose internal technical
  details without a useful product reason.
- Display numbers compactly, without insignificant trailing zeros. Preserve every
  significant digit in exact monetary amounts; do not pass exact decimal strings
  through floating-point values. Display formatting must not change source data
  or payment details.
- Run required project checks and verify the affected behavior. When fixing a bug,
  also check its opposite failure. Mocks, a local build, and a healthy service
  each establish only their own level of verification.
- External operations require verifiable authorization and results. Make repeatable
  events idempotent; acceptance of payment evidence, the local financial record,
  and entitlement grants must be committed atomically. A model response or a
  "success" record alone does not prove that an external action occurred.

## Git, environments, and data

- Work in small, coherent batches. In an existing Git repository, when changes are
  authorized, commit each completed and verified batch according to project rules.
  Keep one behavior's code, tests, and documentation together. This rule does not
  itself require initializing Git.
- Preserve other people's unfinished work. Before handoff, inspect status and diff;
  do not include unrelated changes just to make the working tree clean.
- Preserve the authorship, dates, and history of completed work. Do not squash,
  rebase, amend, or force-push delivered history without a specific instruction.
  Do not fabricate activity or split one coherent change to increase PR counts.
- Push, open PRs, merge, and deploy according to the current project's and task's
  permissions. Do not ask again for applicable authorization already given. If it
  is missing, first prepare a reviewable result, then clarify only the missing step.
- Keep production, local, and test data, accounts, secrets, and results separate.
  Do not publish secrets, raw customer conversations, or private business rules.
  Use an explicitly authorized development credential within its approved scope
  without repeating generic warnings; authorization does not permit putting it
  in Git or logs.
- Temporary processes and containers must terminate and be cleaned up after
  verification, including on failure. Do not stop someone else's active work
  or delete shared data.

## Handoff

- If the task requires a report or handoff, save it in a visible, non-ignored
  location. Its only final copy must not remain in /tmp. In a repository,
  check the path with git check-ignore.
- Write briefly and plainly: what changed, why, what was checked, and what remains.
  Distinguish "prepared," "verified," "deployed," and "confirmed with real data."
- Distinguish explicit user requirements, your proposals, measured facts, and
  estimates. Unknown is not zero; no eligible cases does not mean a defect is
  fixed; demonstration data is not a real outcome.
