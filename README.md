# Personal development playbook

Prepared on 16 October 2026 (Asia/Almaty) from the documentation of Nara, Nara Lite, and Partner Desk.
Source repository: [jamwujustyle/agent-playbook](https://github.com/jamwujustyle/agent-playbook).
Publishing this repository does not install its rules in Codex. Installation is a separate step.

## Recommended structure

| Layer | Contents | Installation |
| --- | --- | --- |
| [Global AGENTS.md](global/AGENTS.md) | Persistent working preferences | `~/.codex/AGENTS.md` or `$CODEX_HOME/AGENTS.md` |
| [Project template](project/AGENTS.template.md) | Project stack, commands, invariants, and permissions | Adapt into `<project>/AGENTS.md` |
| [prompt-engineering](skills/prompt-engineering/SKILL.md) | Designing LLM product behavior | User or project skills directory |
| [evidence-audit](skills/evidence-audit/SKILL.md) | Quality audits, release outcomes, and cost comparisons | User or project skills directory |
| [Release policy](references/release-policy.md) | PRs, deployment, and backups based on data risk | Adopt and adapt only when the project has a release process |
| [Money and events](references/money-events.md) | Precision, authorization, evidence, and idempotency | Apply only to the relevant area |

This playbook carries personal working rules across projects regardless of their purpose.
The two skills extract repeatable procedures from the source documentation; their full
instructions are needed only for a matching task.
The Go/Next/Docker stack, domains, keys, accounts, payment history, gambling policies,
and production permissions remain in their original projects. The preference against
Go function comments is retained in SOURCES as a candidate for a local Go profile,
not a rule for every language.

Global AGENTS instructions are read together with local instructions. Guidance closer
to the working directory refines earlier guidance; an `.override` file can replace
an ordinary file at the same level. Skills load according to the task, so mandatory
working rules should not live exclusively in a skill. See the
[official AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

The original Nara Lite AGENTS file is 47,196 bytes; the documented default limit for
the instruction chain is 32 KiB. This creates a risk of truncation during normal
discovery, not evidence that explicitly supplied instructions were lost in the
source conversation. Raising the limit does not remove duplication or outdated history.

## Install once

Git and Python 3 are required. The installer is designed for Linux/macOS with symbolic
link support; it has not been tested on Windows. Clone into a permanent directory:

```bash
git clone https://github.com/jamwujustyle/agent-playbook.git
cd agent-playbook
```

Preview the installation plan:

```bash
python3 install.py
```

This command displays the plan without changing anything. After reviewing it, install:

```bash
python3 install.py --apply
```

The installer copies the global AGENTS file into Codex home and links the two skill
directories into `~/.agents/skills`, the current user skills location in the
[official skills documentation](https://learn.chatgpt.com/docs/build-skills).
It does not replace a different nonempty AGENTS file or existing unrelated directories
or links: it reports the conflict and stops before making changes. Merge existing
instructions deliberately instead of overwriting them.
Use `--codex-home` and `--skills-dir` to specify custom destinations.

The installer checks the current file contents on every run.
Skill links depend on this directory's location; after installation, do not move it
without updating the links. Updating the copied AGENTS file requires another comparison;
skills read their files through the links. Installation creates no startup jobs,
network requests, or production permissions.

After installation, start a new project chat and ask which instruction sources are
active. Check that the skills are available; restart Codex if the update does not appear.
Do not duplicate skills already shown by the application from another location:
skills with the same name are not merged automatically. The installer leaves other
skill directories unchanged.

## Install for a single project

Copy the needed skills into `<project>/.agents/skills/` and merge the global and local
rules into `<project>/AGENTS.md`. Do not replace existing instructions wholesale.
Copy release-policy/money-events only when needed, then add valid links to the
project's documentation map. The template is not a ready-to-use policy on its own.

Global files from this computer do not appear automatically on another computer or
in a cloud environment. Install them in that environment or include the required
files in the project. For another coding tool, check its supported instruction and
skill locations.

Examples of explicit skill use:

> Use prompt-engineering to fix repeated questions while preserving the objective and tone.

> Use evidence-audit to compare a release with the previous observation window, retaining finding IDs.

In interfaces with a skill picker, use that picker. Codex CLI/IDE supports mentions
such as `$prompt-engineering` and `$evidence-audit`.

## GitHub and updates

This repository versions the playbook and lets you move it between computers.
The public package contains portable rules and a concise source map; original product
documents, local paths, customer data, and credentials are not included.

GitHub provides storage and updates. A link in a chat does not install persistent
instructions: clone and install once, then review diffs when updating.
Changes do not sync automatically. Update the local checkout after reviewing the diff;
linked skills will then read the new version. To update the copied AGENTS file, compare
and merge it with the updated base. The installer deliberately refuses to overwrite a
different nonempty file.

For distribution to other people through a plugin catalog, the skills can
later be packaged as a plugin. A directory and Git are sufficient for this personal
setup. The official documentation
[distinguishes persistent instructions, skills, and plugins](https://learn.chatgpt.com/docs/customization/overview).

## Maintenance

When a mistake recurs, update its single authoritative source. A universal principle
belongs in the global rules; a procedure in a skill; product specifics in its AGENTS;
and history in a report. Do not add a permanent rule after every isolated incident
or copy an entire overgrown project AGENTS into a new project. Check for the opposite
failure as well.

[SOURCES.md](SOURCES.md) records where the rules came from, how conflicts were resolved,
and the limits of the source review. [VALIDATION.md](VALIDATION.md) records the checks actually performed.
