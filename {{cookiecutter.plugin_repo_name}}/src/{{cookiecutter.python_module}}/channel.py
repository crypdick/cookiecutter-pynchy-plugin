"""Channel skeleton for {{ cookiecutter.plugin_repo_name }}."""

from __future__ import annotations

from collections.abc import Callable

from pynchy.types import NewMessage, RegisteredGroup


class ExampleChannel:
    """Minimal placeholder channel implementation."""

    name = "{{ cookiecutter.plugin_slug }}"
    prefix_assistant_name = True

    def __init__(
        self,
        on_message: Callable[[str, NewMessage], None],
        on_chat_metadata: Callable[[str, str, str | None], None],
        registered_groups: Callable[[], dict[str, RegisteredGroup]],
    ):
        self._on_message = on_message
        self._on_chat_metadata = on_chat_metadata
        self._registered_groups = registered_groups
        self._connected = False

    async def connect(self) -> None:
        self._connected = True

    async def send_message(self, jid: str, text: str) -> None:
        raise NotImplementedError("Implement outbound delivery for your channel.")

    async def disconnect(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected

    def owns_jid(self, jid: str) -> bool:
        # Return True for JIDs this channel should ingest.
        return False
