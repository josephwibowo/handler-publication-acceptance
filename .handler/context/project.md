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
  "repository_identity": "seed"
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
    "secrets/**"
  ]
}
```

```handler:surface
{
  "globs": [
    "src/**",
    "docs/**"
  ],
  "level": "standard",
  "profile": {
    "commands": [
      {
        "argv": [
          "true"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      }
    ],
    "name": "seed",
    "profile_id": "c126011201dad09e87db523af6fae1a726753b3707854d54cfea14dc11d4615b"
  }
}
```

```handler:claim
{
  "anchor_paths": [],
  "as_of_commit": "commit",
  "content_hash": "",
  "declared_scope": "src",
  "source_dossier": "",
  "symbols": [],
  "text": "seed-claim"
}
```

```handler:context
{
  "allow_required_only": true,
  "max_pack_bytes": 65536,
  "required_paths": [
    "project.md",
    "decisions/required.md"
  ]
}
```
