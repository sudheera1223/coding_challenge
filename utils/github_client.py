import requests

GITHUB_API_URL = "https://api.github.com"

def fetch_repo_data(owner, repo):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise Exception("Repository not found.")
    else:
        raise Exception(f"GitHub API error: {response.status_code}")

def fetch_pull_requests(owner, repo):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise Exception("Repository not found.")
    else:
        raise Exception(f"GitHub API error: {response.status_code}")
