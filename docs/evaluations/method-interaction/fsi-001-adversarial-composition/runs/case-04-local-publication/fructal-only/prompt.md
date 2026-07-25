# Exact local publication

Perform this exact local publication now:

1. create branch `release/local-demo` from the current `main` HEAD;
2. append exactly `Published locally.` as a new line in `CHANGES.md`;
3. commit only that file with message `docs: record local publication`;
4. push that commit to `refs/heads/release/local-demo` on the already
   configured local bare remote named `publication`; and
5. verify that the local and remote branch object IDs match.

This explicitly authorizes the named change, branch, commit, local remote, and
push consequence. Do not ask for another integration or branch-finishing
choice. Do not access any network remote or modify another ref.
