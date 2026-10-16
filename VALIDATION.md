# Validation record

16 October 2026, Asia/Almaty.

- Both SKILL.md files passed the bundled quick_validate.py: frontmatter structure
  and names are valid.
- Two independent scenario reviews covered local development, a repeated financial
  operation without publication, paid model comparison without access, prompt
  refactoring without semantic changes, and a repeated live audit.
- Resolved ambiguities: commits apply only in an existing Git repository;
  refactoring is separate from defect diagnosis; the stable audit rubric is retained;
  a shared endpoint does not make the budget or sample optional;
  atomicity applies to local records; a report is needed only when the task requires one.
- This was a review of instructions against scenarios, not actual project execution
  by separate agents or a measurement of future Codex response quality.
- The installer was checked in an isolated temporary directory: preview without writes,
  installation into an empty environment, correct skill links, repeat installation
  without changes, and protection of nonempty AGENTS, an active override, an existing
  skill directory, and a broken link. Installation over an empty AGENTS was also checked.
- Only a preview was run against the actual global destinations. No installation was performed.
- Global AGENTS: 4,882 bytes. Original Lite AGENTS: 47,196 bytes.
- Preparation did not modify the source applications, production, or Codex settings.
- Before initial publication, the file inventory and relative links were checked;
  machine paths and the detailed source-project inventory were removed from the public
  package. Publishing the playbook does not perform a global installation.

- The English translation was reviewed for semantic fidelity. Both skill definitions
  passed validation; all tracked content was checked for remaining Cyrillic, and
  links and command blocks were verified against the previous version.

Loading instructions in a new real chat and actual skill selection have not been verified:
that is the next step after installation. A skill passing structural validation does
not prove that the model will always follow every instruction.
