from excel_automation.user_context import get_user_context
from excel_automation.automation.monitor import monitor_excel

def run_process(fileName):
    context = get_user_context()
    repo = context.get("repo")
    token = context.get("token")

    print(f"Repo:{repo}  Token:{token}")

    monitor_excel(fileName)



