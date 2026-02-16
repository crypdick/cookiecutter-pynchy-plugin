"""{{ cookiecutter.plugin_repo_name }} plugin entrypoint."""

from __future__ import annotations

{% if cookiecutter.include_agent_core == "yes" or cookiecutter.include_mcp_server == "yes" or cookiecutter.include_skill == "yes" -%}
from pathlib import Path
{% endif -%}
from typing import Any

import pluggy

{% if cookiecutter.include_channel == "yes" -%}
from .channel import ExampleChannel
{% endif -%}
{% if cookiecutter.include_container_runtime == "yes" -%}
from .runtime import ExampleContainerRuntime
{% endif -%}

hookimpl = pluggy.HookimplMarker("pynchy")


class {{ cookiecutter.plugin_class_name }}:
    """Plugin implementing selected pynchy hooks."""

{% if cookiecutter.include_agent_core == "yes" %}
    @hookimpl
    def pynchy_agent_core_info(self) -> dict[str, str | list[str] | None]:
        return {
            "name": "{{ cookiecutter.plugin_slug }}",
            "module": "{{ cookiecutter.python_module }}.core",
            "class_name": "ExampleAgentCore",
            "packages": [],
            "host_source_path": str(Path(__file__).parent),
        }

{% endif %}
{% if cookiecutter.include_mcp_server == "yes" %}
    @hookimpl
    def pynchy_mcp_server_spec(self) -> dict[str, Any]:
        return {
            "name": "{{ cookiecutter.plugin_slug }}",
            "command": "python",
            "args": ["-m", "{{ cookiecutter.python_module }}.server"],
            "env": {},
            "host_source": str(Path(__file__).parent),
        }

{% endif %}
{% if cookiecutter.include_skill == "yes" %}
    @hookimpl
    def pynchy_skill_paths(self) -> list[str]:
        return [str(Path(__file__).parent / "skills" / "{{ cookiecutter.plugin_slug }}")]

{% endif %}
{% if cookiecutter.include_channel == "yes" %}
    @hookimpl
    def pynchy_create_channel(self, context: Any) -> Any | None:
        on_message = getattr(context, "on_message_callback")
        on_chat_metadata = getattr(context, "on_chat_metadata_callback")
        registered_groups = getattr(context, "registered_groups")
        return ExampleChannel(
            on_message=on_message,
            on_chat_metadata=on_chat_metadata,
            registered_groups=registered_groups,
        )
{% endif %}
{% if cookiecutter.include_container_runtime == "yes" %}
    @hookimpl
    def pynchy_container_runtime(self) -> Any | None:
        return ExampleContainerRuntime()
{% endif %}
