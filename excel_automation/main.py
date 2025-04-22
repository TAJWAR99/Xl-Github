from . import run_process
from . import set_user_context
from .credentials_config import REPO_NAME, GITHUB_TOKEN, SERVICE_TOKEN
import os

def main():
    # config_path = os.path.join(os.path.dirname(__file__), "local_file.txt")
    # arr = []
    
    # with open(config_path, "r") as file:
    #     for line in file:
    #         arr.append(line.strip()) 

    # repo, token = arr
    repo = REPO_NAME
    token = GITHUB_TOKEN
    service_token = SERVICE_TOKEN

    set_user_context({"repo": repo, "token": token, "service_token": service_token})

    run_process(True)
