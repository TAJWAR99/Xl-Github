from .user_context import get_user_context
from .online_monitor import online_excel_monitor
from .monitor import monitor_excel

def run_process(local):
    context = get_user_context()
    repo = context.get("repo")
    token = context.get("token")

    if local is True:
        monitor_excel()
    else:
        online_excel_monitor()



