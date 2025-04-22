from .user_context import *

# GraphQL endpoint is static
GRAPHQL_URL = "https://api.github.com/graphql"

def get_github_token():
    context = get_user_context()
    return context.get("token")

def get_service_token():
    context = get_user_context()
    return context.get("service_token")

def get_repo_name():
    context = get_user_context()
    return context.get("repo")

def get_issue_url():
    REPO_NAME = get_repo_name()
    return f"https://api.github.com/repos/{REPO_NAME}/issues"

def get_assignees_url():
    REPO_NAME = get_repo_name()
    return f"https://api.github.com/repos/{REPO_NAME}/collaborators"

def get_headers():
    token = get_github_token()
    HEADERS = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    return HEADERS
