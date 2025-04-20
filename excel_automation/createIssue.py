import requests
from .globals import *
from .getProjectID import get_project_id
from .addIssueToProject import add_issue_to_project


# Function to validate assignee
def is_valid_assignee(username):

    ASSIGNEES_URL = get_assignees_url()
    HEADERS = get_headers()

    response = requests.get(f"{ASSIGNEES_URL}/{username}", headers=HEADERS)
    return response.status_code == 204  # 204 means user exists


# Function to create GitHub issue
def create_github_issue(title, body, assignee, labels, projectName, moduleName, sprintName):
    
    ISSUE_URL = get_issue_url()
    HEADERS = get_headers()

    issue_data = {
        "title": title,
        "body": body,
        "labels": labels
    }

    # Validate assignee
    if assignee and is_valid_assignee(assignee):
        issue_data["assignees"] = [assignee]
    else:
        print(f"⚠️ Warning: Assignee '{assignee}' is not valid. Issue will be created without an assignee.")

    # Create the issue
    response = requests.post(ISSUE_URL, json=issue_data, headers=HEADERS)

    if response.status_code == 201:
        issue_json = response.json()
        node_id = issue_json.get("node_id", None)

        issue_url = issue_json["html_url"]
        print(f"✅ Issue Created: {issue_url}")

        project_name = projectName
        project_id = get_project_id(project_name)
        

        if project_id:
            add_issue_to_project(project_id, node_id)
        else:
            print(f"Project '{project_name}' not found.")
        
        return (True, response.content)
    else:
        print(f"❌ Failed to create issue: {response.content}")
        return (False, False)
