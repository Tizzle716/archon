from pydantic import BaseModel

class WebSearchAgent(BaseModel):
    """Agent for web searches."""
    engine: str = "google"

    def search(self, query: str):
        """Perform web search."""
        return {"query": query}
