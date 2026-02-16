from __future__ import annotations

{% if cookiecutter.include_channel == "yes" -%}
from {{ cookiecutter.python_module }}.channel import ExampleChannel
{% else -%}
from {{ cookiecutter.python_module }} import {{ cookiecutter.plugin_class_name }}
{% endif -%}


def test_plugin_imports() -> None:
{% if cookiecutter.include_channel == "yes" -%}
    channel = ExampleChannel(
        on_message=lambda _jid, _msg: None,
        on_chat_metadata=lambda _jid, _ts, _name=None: None,
        registered_groups=lambda: {},
    )
    assert channel.name == "{{ cookiecutter.plugin_slug }}"
{% else -%}
    plugin = {{ cookiecutter.plugin_class_name }}()
    assert plugin is not None
{% endif -%}
