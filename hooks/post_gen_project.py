"""Cleanup optional files based on cookiecutter feature flags."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path.cwd()
MODULE = ROOT / "src" / "{{ cookiecutter.python_module }}"


def is_enabled(value: str) -> bool:
    return value.strip().lower() == "yes"


def remove_file(path: Path) -> None:
    if path.exists():
        path.unlink()


def remove_tree(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


if not is_enabled("{{ cookiecutter.include_mcp_server }}"):
    remove_file(MODULE / "server.py")

if not is_enabled("{{ cookiecutter.include_agent_core }}"):
    remove_file(MODULE / "core.py")

if not is_enabled("{{ cookiecutter.include_channel }}"):
    remove_file(MODULE / "channel.py")

if not is_enabled("{{ cookiecutter.include_container_runtime }}"):
    remove_file(MODULE / "runtime.py")

if not is_enabled("{{ cookiecutter.include_skill }}"):
    remove_tree(MODULE / "skills")

if not is_enabled("{{ cookiecutter.include_tests }}"):
    remove_tree(ROOT / "tests")
