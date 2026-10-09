---
id: project-profile
kind: project
status: active
scope: []
evidence: []
supersedes: []
---

# Project Overlay

## Narrative

The prose in this file is explanatory; machine-read declarations use typed fences.

```handler:identity
{
  "repository_identity": "handler-publication-acceptance"
}
```

```handler:conventions
{
  "branch_prefix": "",
  "integration_branch": "main",
  "worktree_pattern": ""
}
```

```handler:floor
{
  "level": "standard"
}
```

```handler:forbidden
{
  "globs": [
    ".github/**",
    ".handler/**",
    "ci/**"
  ]
}
```

```handler:surface
{
  "globs": [
    "acceptance/**"
  ],
  "level": "standard",
  "profile": {
    "commands": [
      {
        "argv": [
          "sh",
          "ci/check.sh"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      }
    ],
    "name": "acceptance-check",
    "profile_id": "a4f41eb66b4f81dd26df019538ad32d3d544b2e089f86f99a609bc9d48f03828"
  }
}
```

```handler:context
{
  "allow_required_only": true,
  "max_pack_bytes": 65536,
  "required_paths": [
    "project.md",
    "decisions/acceptance-target.md"
  ]
}
```
