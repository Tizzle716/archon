import requests

def get_github_file(owner: str, repo: str, path: str):
    """Fetch file from GitHub."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    return requests.get(url).json()
