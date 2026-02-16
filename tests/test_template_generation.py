from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def render_template(**overrides: str) -> Path:
    output_dir = Path(tempfile.mkdtemp(prefix="cookiecutter-pynchy-plugin-test-"))
    command = [
        "uvx",
        "cookiecutter",
        "--no-input",
        str(REPO_ROOT),
        "--output-dir",
        str(output_dir),
    ]
    for key, value in overrides.items():
        command.append(f"{key}={value}")

    subprocess.run(command, check=True, capture_output=True, text=True)
    return output_dir / overrides["plugin_repo_name"]


class CookiecutterTemplateTests(unittest.TestCase):
    def tearDown(self) -> None:
        for path in getattr(self, "_generated_roots", []):
            shutil.rmtree(path.parent, ignore_errors=True)

    def _render(self, **overrides: str) -> Path:
        generated = render_template(**overrides)
        if not hasattr(self, "_generated_roots"):
            self._generated_roots = []
        self._generated_roots.append(generated)
        return generated

    def test_default_generation_has_only_mcp_scaffold(self) -> None:
        generated = self._render(
            plugin_slug="hello-test",
            plugin_repo_name="pynchy-plugin-hello-test",
            python_module="pynchy_plugin_hello_test",
            plugin_class_name="HelloTestPlugin",
            entry_point_name="hello-test",
            include_mcp_server="yes",
            include_skill="no",
            include_agent_core="no",
            include_channel="no",
            include_container_runtime="no",
            include_workspace="no",
            include_tests="no",
        )

        module_root = generated / "src" / "pynchy_plugin_hello_test"
        self.assertTrue((module_root / "__init__.py").exists())
        self.assertTrue((module_root / "server.py").exists())
        self.assertFalse((module_root / "core.py").exists())
        self.assertFalse((module_root / "channel.py").exists())
        self.assertFalse((module_root / "runtime.py").exists())
        self.assertFalse((module_root / "skills").exists())
        self.assertFalse((generated / "tests").exists())

    def test_optional_features_are_created_when_enabled(self) -> None:
        generated = self._render(
            plugin_slug="all-hooks-test",
            plugin_repo_name="pynchy-plugin-all-hooks-test",
            python_module="pynchy_plugin_all_hooks_test",
            plugin_class_name="AllHooksTestPlugin",
            entry_point_name="all-hooks-test",
            include_mcp_server="no",
            include_skill="yes",
            include_agent_core="yes",
            include_channel="yes",
            include_container_runtime="yes",
            include_workspace="yes",
            include_tests="yes",
        )

        module_root = generated / "src" / "pynchy_plugin_all_hooks_test"
        skill_file = module_root / "skills" / "all-hooks-test" / "SKILL.md"
        self.assertTrue((module_root / "__init__.py").exists())
        self.assertFalse((module_root / "server.py").exists())
        self.assertTrue((module_root / "core.py").exists())
        self.assertTrue((module_root / "channel.py").exists())
        self.assertTrue((module_root / "runtime.py").exists())
        self.assertTrue(skill_file.exists())
        self.assertTrue((generated / "tests" / "test_plugin_generation.py").exists())
        plugin_init = (module_root / "__init__.py").read_text()
        self.assertIn("pynchy_workspace_spec", plugin_init)


if __name__ == "__main__":
    unittest.main()
