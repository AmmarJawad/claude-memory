#!/usr/bin/env python3
"""
MCP Server for bidirectional Claude.ai context bridge.

Reads conversations and Project knowledge from claude.ai.
Pushes status, TODOs, and session logs back to claude.ai Projects.

Uses Chrome browser cookies to authenticate with Claude.ai API.
Requires being logged into claude.ai in Chrome.
"""

from mcp.server.fastmcp import FastMCP

from context_bridge.conversations_api import (
    list_conversations,
    get_conversation,
    search_conversations,
    get_conversation_summary,
)

mcp = FastMCP("context-bridge")

# Register conversation tools
mcp.tool()(list_conversations)
mcp.tool()(get_conversation)
mcp.tool()(search_conversations)
mcp.tool()(get_conversation_summary)

if __name__ == "__main__":
    mcp.run()
