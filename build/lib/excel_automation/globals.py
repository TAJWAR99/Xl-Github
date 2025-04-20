from excel_automation.user_context import *

GITHUB_TOKEN = getToken()
REPO_NAME = getRepo()

ISSUE_URL = f"https://api.github.com/repos/{REPO_NAME}/issues"
ASSIGNEES_URL = f"https://api.github.com/repos/{REPO_NAME}/collaborators"
GRAPHQL_URL = "https://api.github.com/graphql"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    # "X-GitHub-Api-Version": "2022-11-28"
}