import requests
from .globals import *

def get_project_id(project_name):

    GITHUB_TOKEN = get_github_token()
    
    query = """
        query {
        viewer {
            projectsV2(first: 10) {
            nodes {
                id
                title
            }
            }
        }
        }
    """

    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": query
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers) 
    if response.status_code == 200:
        response = response.json()
        projects = response.get("data", {}).get("viewer", {}).get("projectsV2", {}).get("nodes", [])
        
        for project in projects:
            if project["title"] == project_name:
                return project["id"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
    return None  # Return None if no matching project is found