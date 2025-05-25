from typing import Dict, Any
import json

class ToolManager:
    """
    Manages available tools for agents.
    """
    def __init__(self):
        self.tools: Dict[str, Any] = {}

    def register_tool(self, name: str, tool: Any):
        """Register a new tool."""
        self.tools[name] = tool
