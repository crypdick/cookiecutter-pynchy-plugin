"""Example container runtime provider."""

from __future__ import annotations

import json
import shutil
import subprocess


class ExampleContainerRuntime:
    """Replace with your runtime integration."""

    name = "{{ cookiecutter.plugin_slug }}"
    cli = "{{ cookiecutter.plugin_slug }}"

    def is_available(self) -> bool:
        return shutil.which(self.cli) is not None

    def ensure_running(self) -> None:
        raise NotImplementedError("Implement runtime readiness checks/startup.")

    def list_running_containers(self, prefix: str = "pynchy-") -> list[str]:
        result = subprocess.run(
            [self.cli, "ps", "--format", "{{ '{{json .}}' }}"],
            capture_output=True,
            text=True,
        )
        names: list[str] = []
        for line in result.stdout.strip().splitlines():
            if not line:
                continue
            item = json.loads(line)
            name = item.get("Names", "")
            if name.startswith(prefix):
                names.append(name)
        return names
