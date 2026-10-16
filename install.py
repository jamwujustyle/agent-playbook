#!/usr/bin/env python3
"""Preview or install this personal kit without replacing existing guidance."""

import argparse
import os
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Apply the displayed plan")
    parser.add_argument("--codex-home", type=Path,
                        default=Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")))
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".agents" / "skills")
    args = parser.parse_args()
    kit = Path(__file__).resolve().parent
    codex_dir = args.codex_home.expanduser().absolute()
    skills_dir = args.skills_dir.expanduser().absolute()
    source = kit / "global" / "AGENTS.md"
    target = codex_dir / "AGENTS.md"
    expected = source.read_bytes()
    actions = []
    conflicts = []

    override = codex_dir / "AGENTS.override.md"
    if override.is_symlink() or (override.exists() and
                                (not override.is_file() or override.stat().st_size)):
        conflicts.append(f"Resolve the global override first: {override}")
    if target.is_symlink() or (target.exists() and not target.is_file()):
        conflicts.append(f"Not an ordinary file; preserve and merge manually: {target}")
    elif target.exists() and target.read_bytes() not in (b"", expected):
        conflicts.append(f"Existing instructions differ; merge manually: {target}")
    elif not target.exists() or target.read_bytes() != expected:
        actions.append(("copy", source, target))

    for folder in sorted((kit / "skills").iterdir()):
        if not (folder / "SKILL.md").is_file():
            continue
        dest = skills_dir / folder.name
        if dest.is_symlink() and dest.resolve() == folder.resolve():
            continue
        if dest.exists() or dest.is_symlink():
            conflicts.append(f"Existing skill is preserved; resolve manually: {dest}")
        else:
            actions.append(("link", folder, dest))

    for kind, src, dest in actions:
        print(f"{kind}: {src} -> {dest}")
    if conflicts:
        for conflict in conflicts:
            print(f"CONFLICT: {conflict}", file=sys.stderr)
        print("Nothing changed.", file=sys.stderr)
        return 1
    if not actions:
        print("Already installed; nothing changed.")
        return 0
    if not args.apply:
        print("Preview only. Run with --apply to install.")
        return 0

    for kind, src, dest in actions:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if kind == "copy":
            # Recheck immediately before writing; never replace nonempty guidance.
            if dest.is_symlink() or (dest.exists() and dest.read_bytes() not in (b"", expected)):
                raise RuntimeError(f"Instructions changed during installation: {dest}")
            mode = "r+b" if dest.exists() else "xb"
            with dest.open(mode) as stream:
                stream.write(expected)
                stream.truncate()
        else:
            dest.symlink_to(src.resolve(), target_is_directory=True)
        print(f"Installed: {dest}")
    print("Start a new Codex chat and verify active instructions and skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
