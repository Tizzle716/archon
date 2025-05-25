from pydantic import BaseModel

class GitHubAgent(BaseModel):
    """Agent for GitHub operations."""
    token: str

    def get_repo(self, owner: str, repo: str):
        """Get repository info."""
        return {"owner": owner, "repo": repo}
