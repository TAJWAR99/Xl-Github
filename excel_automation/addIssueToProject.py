import requests
import json
from .globals import *


def add_issue_to_project(PROJECT_ID, ISSUE_NODE_ID):

    GITHUB_TOKEN = get_github_token()
    SERVICE_TOKEN = get_service_token()

    mutation = """
    mutation {
    addProjectV2ItemById(input: {projectId: "%s", contentId: "%s"}) {
        item {
        id
        }
    }
    }
    """ % (PROJECT_ID, ISSUE_NODE_ID)

    # API URL and headers
    url = "https://api.github.com/graphql"
    
    headers = {
        "Authorization": f"Bearer {SERVICE_TOKEN}",
        "Content-Type": "application/json"
    }

    # Request Payload
    payload = {
        "query": mutation
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response (JSON format)
    if response.status_code == 200:
        pass
        # print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error: {response.status_code}, {response.text}")
