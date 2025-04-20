import json

def getIssueUrl(response_content):
    
    # Convert the JSON response to a Python dictionary
    response_dict = json.loads(response_content)

    # Extract the `html_url`
    html_url = response_dict.get("html_url")

    return html_url