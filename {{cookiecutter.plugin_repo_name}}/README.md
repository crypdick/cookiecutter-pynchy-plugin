# {{ cookiecutter.plugin_repo_name }}

{{ cookiecutter.plugin_description }}

## Implemented Hooks

{% if cookiecutter.include_mcp_server == "yes" -%}
- `pynchy_mcp_server_spec`
{% endif -%}
{% if cookiecutter.include_skill == "yes" -%}
- `pynchy_skill_paths`
{% endif -%}
{% if cookiecutter.include_agent_core == "yes" -%}
- `pynchy_agent_core_info`
{% endif -%}
{% if cookiecutter.include_channel == "yes" -%}
- `pynchy_create_channel`
{% endif -%}

## Installation

```bash
uv pip install -e .
```

Install into the same environment where pynchy runs, then restart pynchy.

## Plugin Package Layout

```text
{{ cookiecutter.plugin_repo_name }}/
├── pyproject.toml
└── src/
    └── {{ cookiecutter.python_module }}/
        ├── __init__.py
{% if cookiecutter.include_mcp_server == "yes" -%}
        ├── server.py
{% endif -%}
{% if cookiecutter.include_agent_core == "yes" -%}
        ├── core.py
{% endif -%}
{% if cookiecutter.include_channel == "yes" -%}
        ├── channel.py
{% endif -%}
{% if cookiecutter.include_skill == "yes" -%}
        └── skills/
            └── {{ cookiecutter.plugin_slug }}/
                └── SKILL.md
{% endif -%}
```
