---
id: project-profile
kind: project
status: active
description: Standing project profile naming the writable surfaces, validation profile, and context policy that bound every objective.
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
          "python3",
          "src/protected/check_integration.py"
        ],
        "artifacts": [
          "reports/junit.xml"
        ],
        "expects": "junit_xml",
        "working_directory": ""
      }
    ],
    "name": "native-seed-observability",
    "profile_id": "7d4c2e27ac4b179d3a9b1dc96c6f95c6c7c8230467c247551441778d8856b12b"
  }
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
          "python3",
          "src/protected/check_first.py"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      }
    ],
    "name": "native-seed-first",
    "profile_id": "97e5a83fab2065ea269ffbaa34620fa63bda79e2920c3b1f4d749d598fe02051"
  }
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
          "python3",
          "src/protected/check_second.py"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      }
    ],
    "name": "native-seed-second",
    "profile_id": "c7949941f2205381a9afabbe48602fc546bf4f4eaed82919be21f13270a6bad2"
  }
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
          "python3",
          "src/protected/check_second.py"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      },
      {
        "argv": [
          "python3",
          "src/protected/check_obligation.py"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      }
    ],
    "name": "native-seed-obligation",
    "profile_id": "1efbf958679d95b0b7e562bdbf8188a3e2bf269c42bf7faf76cccd4d5ef2f1d4"
  }
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
          "python3",
          "src/protected/check_negatives.py"
        ],
        "expects": "exit_zero",
        "working_directory": ""
      }
    ],
    "name": "native-seed-negative",
    "profile_id": "0e4a9db501e86a0347033eba4a073e9072e52ec760a9a89fea0cfbf3e4b87205"
  }
}
```

```handler:capability
{
  "budgets": {
    "reworks": 1,
    "tokens": 10000,
    "wall_clock_seconds": 300
  },
  "env_allowlist": [
    "PATH"
  ],
  "level": "standard",
  "role": "planner",
  "worker_config": {
    "agent_server_version": "1.53.0",
    "apps_enabled": false,
    "auth_mode": "chatgpt",
    "cancel_grace_seconds": 8,
    "codex_cli_version": "0.160.1",
    "codex_sdk_version": "0.160.1",
    "container_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "endpoint": "http://127.0.0.1:62525",
    "environment": {
      "LANG": "C.UTF-8",
      "PATH": "/usr/local/bin:/usr/bin:/bin"
    },
    "idle_timeout_seconds": 90,
    "image_digest": "sha256:59859aa007ee2bea2402b0259ea104d871d90e8e8c6e8788da20d3bba3f528b4",
    "max_context_bytes": 65536,
    "mcp_servers": [],
    "model": "gpt-6.1-sol",
    "model_provider": "openai",
    "native_home": "/home/openhands",
    "native_python": "/home/openhands/spike-native-venv/bin/python",
    "permission_profile": "spike",
    "plugins_enabled": false,
    "profile_id": "planning-profile-planner-v1",
    "reasoning_effort": "high",
    "role": "planner",
    "schema_version": 1,
    "startup_timeout_seconds": 90,
    "tools": [
      "exec_command",
      "read_file"
    ],
    "validation_timeout_seconds": 10,
    "volume_name": "handler-planning-native-volume",
    "wall_clock_seconds": 300,
    "workspace_root": "/workspace/toy",
    "workspace_sdk_version": "1.53.0",
    "workspace_version": "1.53.0"
  }
}
```

```handler:capability
{
  "budgets": {
    "reworks": 1,
    "tokens": 10000,
    "wall_clock_seconds": 300
  },
  "env_allowlist": [
    "PATH"
  ],
  "level": "standard",
  "role": "reviewer",
  "worker_config": {
    "agent_server_version": "1.53.0",
    "apps_enabled": false,
    "auth_mode": "chatgpt",
    "cancel_grace_seconds": 8,
    "codex_cli_version": "0.160.1",
    "codex_sdk_version": "0.160.1",
    "container_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "endpoint": "http://127.0.0.1:62525",
    "environment": {
      "LANG": "C.UTF-8",
      "PATH": "/usr/local/bin:/usr/bin:/bin"
    },
    "idle_timeout_seconds": 90,
    "image_digest": "sha256:59859aa007ee2bea2402b0259ea104d871d90e8e8c6e8788da20d3bba3f528b4",
    "max_context_bytes": 65536,
    "mcp_servers": [],
    "model": "gpt-6.1-sol",
    "model_provider": "openai",
    "native_home": "/home/openhands",
    "native_python": "/home/openhands/spike-native-venv/bin/python",
    "permission_profile": "spike",
    "plugins_enabled": false,
    "profile_id": "planning-profile-reviewer-v1",
    "reasoning_effort": "high",
    "role": "reviewer",
    "schema_version": 1,
    "startup_timeout_seconds": 90,
    "tools": [
      "exec_command",
      "read_file"
    ],
    "validation_timeout_seconds": 10,
    "volume_name": "handler-planning-native-volume",
    "wall_clock_seconds": 300,
    "workspace_root": "/workspace/toy",
    "workspace_sdk_version": "1.53.0",
    "workspace_version": "1.53.0"
  }
}
```

```handler:capability
{
  "budgets": {
    "reworks": 1,
    "tokens": 10000,
    "wall_clock_seconds": 300
  },
  "env_allowlist": [
    "PATH"
  ],
  "level": "standard",
  "role": "implementer",
  "worker_config": {
    "agent_server_version": "1.53.0",
    "apps_enabled": false,
    "auth_mode": "chatgpt",
    "cancel_grace_seconds": 8,
    "codex_cli_version": "0.160.1",
    "codex_sdk_version": "0.160.1",
    "container_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "endpoint": "http://127.0.0.1:62525",
    "environment": {
      "LANG": "C.UTF-8",
      "PATH": "/usr/local/bin:/usr/bin:/bin"
    },
    "idle_timeout_seconds": 90,
    "image_digest": "sha256:59859aa007ee2bea2402b0259ea104d871d90e8e8c6e8788da20d3bba3f528b4",
    "max_context_bytes": 65536,
    "mcp_servers": [],
    "model": "gpt-6.1-sol",
    "model_provider": "openai",
    "native_home": "/home/openhands",
    "native_python": "/home/openhands/spike-native-venv/bin/python",
    "permission_profile": "spike",
    "plugins_enabled": false,
    "profile_id": "planning-profile-implementer-v1",
    "reasoning_effort": "low",
    "role": "implementer",
    "schema_version": 1,
    "startup_timeout_seconds": 90,
    "tools": [
      "exec_command",
      "read_file",
      "write_file"
    ],
    "validation_timeout_seconds": 10,
    "volume_name": "handler-planning-native-volume",
    "wall_clock_seconds": 300,
    "workspace_root": "/workspace/toy",
    "workspace_sdk_version": "1.53.0",
    "workspace_version": "1.53.0"
  }
}
```

```handler:capability
{
  "budgets": {
    "reworks": 1,
    "tokens": 10000,
    "wall_clock_seconds": 300
  },
  "env_allowlist": [
    "PATH"
  ],
  "level": "standard",
  "role": "objective_assurance",
  "worker_config": {
    "agent_server_version": "1.53.0",
    "apps_enabled": false,
    "auth_mode": "chatgpt",
    "cancel_grace_seconds": 8,
    "codex_cli_version": "0.160.1",
    "codex_sdk_version": "0.160.1",
    "container_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "endpoint": "http://127.0.0.1:62525",
    "environment": {
      "LANG": "C.UTF-8",
      "PATH": "/usr/local/bin:/usr/bin:/bin"
    },
    "idle_timeout_seconds": 90,
    "image_digest": "sha256:59859aa007ee2bea2402b0259ea104d871d90e8e8c6e8788da20d3bba3f528b4",
    "max_context_bytes": 65536,
    "mcp_servers": [],
    "model": "gpt-6.1-sol",
    "model_provider": "openai",
    "native_home": "/home/openhands",
    "native_python": "/home/openhands/spike-native-venv/bin/python",
    "permission_profile": "spike",
    "plugins_enabled": false,
    "profile_id": "planning-profile-objective_assurance-v1",
    "reasoning_effort": "low",
    "role": "objective_assurance",
    "schema_version": 1,
    "startup_timeout_seconds": 90,
    "tools": [
      "exec_command",
      "read_file"
    ],
    "validation_timeout_seconds": 10,
    "volume_name": "handler-planning-native-volume",
    "wall_clock_seconds": 300,
    "workspace_root": "/workspace/toy",
    "workspace_sdk_version": "1.53.0",
    "workspace_version": "1.53.0"
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
