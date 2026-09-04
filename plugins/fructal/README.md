# Fructal Cap Design plugin

This directory is a generated distribution wrapper around the canonical
Fructal Cap Design skill at
<https://github.com/PaolaShultz/shr-skills/blob/main/skills/fructal/SKILL.md>.
It supplies both the OpenAI and Claude plugin manifests while keeping one
byte-identical mirrored skill.

Run <code>scripts/sync-distribution.py</code> from the repository root after
changing the canonical skill. Distribution validation fails if the mirror
drifts.

The plugin adds instructions only. It does not include an MCP server, executable
hook, hosted service, or authentication flow.
