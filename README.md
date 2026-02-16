# cookiecutter-pynchy-plugin

Cookiecutter template for building third-party `pynchy` plugins.

Generated projects follow the plugin packaging and hook conventions documented in `pynchy/docs/plugins/*`.

## About Pynchy

Pynchy is a personal assistant runtime that routes WhatsApp messages to containerized coding agents. Its plugin system lets you add channels, MCP tools, skills, agent cores, and runtime integrations without changing the base app.

- Pynchy repository: https://github.com/crypdick/pynchy
- Plugin documentation: https://github.com/crypdick/pynchy/tree/main/docs/plugins

## Features

- Python package scaffold with `src/` layout
- Pluggy hook registration for the `pynchy` entry-point group
- Optional hook skeletons:
  - MCP server (`pynchy_mcp_server_spec`)
  - Skill paths (`pynchy_skill_paths`)
  - Agent core (`pynchy_agent_core_info`)
  - Channel creation (`pynchy_create_channel`)
  - Container runtime (`pynchy_container_runtime`)
- Optional generated plugin tests (`include_tests=yes`)
- Optional starter files for MCP server and skills

## Quickstart

```bash
cookiecutter /path/to/cookiecutter-pynchy-plugin
```

Then install the generated plugin in editable mode from your pynchy environment:

```bash
uv pip install -e /path/to/generated-plugin
```

Restart pynchy and check logs for plugin discovery.

## Run Template Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The tests render the template in temporary directories and assert the expected
file layout for different hook combinations.

## Template Structure

```text
cookiecutter-pynchy-plugin/
├── cookiecutter.json
├── hooks/
│   └── post_gen_project.py
└── {{cookiecutter.plugin_repo_name}}/
    ├── pyproject.toml
    ├── README.md
    └── src/
        └── {{cookiecutter.python_module}}/
            ├── __init__.py
            ├── server.py
            ├── core.py
            ├── channel.py
            └── skills/
                └── {{cookiecutter.plugin_slug}}/
                    └── SKILL.md
```