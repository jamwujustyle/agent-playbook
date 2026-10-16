# Personal agent playbook

Portable working preferences and two optional procedures for coding agents.

| File | Purpose |
| --- | --- |
| [global/AGENTS.md](global/AGENTS.md) | Personal preferences applied across projects |
| [project/AGENTS.template.md](project/AGENTS.template.md) | A short scaffold for each project's own instructions |
| [prompt-engineering](skills/prompt-engineering/SKILL.md) | Diagnose and change LLM behavior without accumulating prompt patches |
| [evidence-audit](skills/evidence-audit/SKILL.md) | Evaluate changes across repeated observation windows |

## Use with Codex

A GitHub link lets an agent read the files for the current task when asked. It does
not install persistent instructions or skills. For regular use, clone this repository
into a permanent directory and install it once:

```bash
git clone https://github.com/jamwujustyle/agent-playbook.git
cd agent-playbook
python3 install.py         # Preview
python3 install.py --apply # Install
```

Requires Git, Python 3, and symbolic link support; intended for Linux/macOS.
The installer copies the personal rules to `~/.codex/AGENTS.md` (or `$CODEX_HOME/AGENTS.md`)
and links the skills into `~/.agents/skills`. A different nonempty instructions file,
an active override, or an unrelated existing skill causes it to stop before writing.
Merge those conflicts manually. Custom destinations use `--codex-home` and `--skills-dir`.

Start a new Codex chat after installation and check that the rules and skills are
available. Skills are selected for matching tasks; invoke `$prompt-engineering` or
`$evidence-audit` explicitly when desired. See the official
[instructions guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and
[skills guide](https://learn.chatgpt.com/docs/build-skills).

For one project only, merge the personal rules into its `AGENTS.md` and copy the
needed skill folders into `.agents/skills/`. Adapt the project template with verified
local facts. Other machines and cloud environments need their own installation;
other agents may use different discovery paths.

## Updates

Review incoming changes, then update the checkout with `git pull --ff-only`.
Linked skills use the updated files. Compare and merge changes into the copied
`AGENTS.md`; the installer preserves an existing file that differs. Keep the clone
at the same path so skill links remain valid.

## Maintenance

Keep a rule only if it changes a decision that a capable agent would otherwise make.
Personal preferences belong in `AGENTS.md`, repeatable procedures in skills, and
project facts in that project's own instructions. Prefer replacing a conflicting
rule over adding another exception.
