from pydantic import BaseModel

class CodeRequest(BaseModel):
    """Request model for code generation."""
    task: str
    language: str = "python"
