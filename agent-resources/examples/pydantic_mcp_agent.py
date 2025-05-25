from pydantic import BaseModel

class MCPAgent(BaseModel):
    """Agent for MCP operations."""
    api_key: str

    def call_mcp(self, endpoint: str):
        """Call MCP endpoint."""
        return {"endpoint": endpoint}
