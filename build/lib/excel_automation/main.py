from excel_automation.runner import run_process
from excel_automation.user_context import set_user_context

def main():
    repo = input("Enter owner/repo: ")
    token = input("Enter token: ")
    excel_file = input("Enter the file name: ")

    set_user_context({"repo": repo, "token": token})

    run_process(excel_file)
