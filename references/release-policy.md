# Optional release policy

This is a portable draft policy based on Nara Lite practices. Including this
file in a repository does not itself grant permission to push, merge, or act in production.
First record authorized operations and environments in the local AGENTS.md.
Any stricter policy currently in force for the project remains in effect until changed.

- Release a complete, verified batch together: implementation, necessary tests,
  and documentation. Prefer a separate PR for a meaningful independent change;
  do not fragment one task or generate cosmetic activity for counters.
- When merging is authorized, preserve original commits with a regular merge or fast-forward.
  Follow branch protections and checks. Verify that completed commits are reachable
  from the remote primary branch; do not guess the branch name or account.
- First compare the candidate with the version actually running to avoid rolling back
  a newer release. Deploy only committed code according to the local runbook.
  Do not run seeds that change user settings without a corresponding instruction.
- After release, verify health and the relevant user workflow.
  A healthy process does not prove correct behavior. Record the version and cutover.
- For documentation-only changes, updating the checkout and checking status is usually
  enough, without rebuilding, restarting, migrations, or seeds, if the deployment supports this.
- Assess backups according to data risk. Routine code, UI, documentation, and purely
  additive migrations do not by themselves require a full dump and media archive.
  Deletion, incompatible migrations, bulk rewrites, data relocation,
  changes to encryption, or changes to financial calculation history require an appropriate, verified backup.
  State the specific risk and affected scope; do not duplicate a usable backup on a retry.
- Before changing a production environment or certificate file, save a small copy of the affected
  file with its original permissions. Do not copy an unchanged environment file on every release.
- Check resource headroom before building. Thresholds, paths, and authorized cleanup
  belong in the local runbook. Do not delete existing backups or production images,
  terminate other people's processes, or add recurring cleanup without separate authorization.
- If blocked, identify the exact step that failed. Pushing a branch, opening a PR, and local
  verification do not replace merging or deployment when those are part of the agreed delivery.
