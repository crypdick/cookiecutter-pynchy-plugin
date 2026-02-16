"""Minimal MCP server for {{ cookiecutter.plugin_repo_name }}."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{{ cookiecutter.plugin_slug }}")


@mcp.tool()
def ping() -> str:
    """Health-check tool used to validate MCP wiring."""
    return "pong"


if __name__ == "__main__":
    mcp.run()
