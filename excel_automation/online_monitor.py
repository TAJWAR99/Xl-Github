import os
import requests
import gspread  # For reading the online Excel sheet
from oauth2client.service_account import ServiceAccountCredentials
from .createIssue import create_github_issue
from .getIssueUrl import getIssueUrl

try:
    from .google_sheets_config import GOOGLE_SHEETS_URL
except ImportError:
    GOOGLE_SHEETS_URL = None


def online_excel_monitor():  # Keep filename param for compatibility
    if not GOOGLE_SHEETS_URL:
        raise ValueError("Google Sheets URL not configured. Please set GOOGLE_SHEETS_URL in google_sheets_config.py")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "credentials.json")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError("credentials.json not found. Please ensure Google Service Account credentials are properly configured.")

    credentials = ServiceAccountCredentials.from_json_keyfile_name(file_path, ["https://spreadsheets.google.com/feeds"])
    client = gspread.authorize(credentials)
    
    try:
        sheets = client.open_by_url(GOOGLE_SHEETS_URL)
    except gspread.exceptions.NoValidUrlKeyFound:
        raise ValueError(f"Invalid Google Sheets URL: {GOOGLE_SHEETS_URL}. Please ensure the URL is correct and accessible.")
    all_sheets = sheets.worksheets()

    for sheet in all_sheets:
        print(f"Processing sheet: {sheet.title}")
        rows = sheet.get_all_values()
        if not rows:
            print("⚠️ No data found in sheet!")
            continue

        headers = rows[0]  # Extract header row
        # Create a mapping from header names to column indices (1-based)
        header_index_map = {header: idx + 1 for idx, header in enumerate(headers)}

        labels = ["bug", "test-failure"]

        for i, row in enumerate(rows[1:]):
            row_dict = dict(zip(headers, row))  # Map headers to row values

            test_case_id = row_dict.get("TestCase ID", "")
            test_case_name = row_dict.get("TestCase Name", "")
            status = row_dict.get("Status", "")
            issue_created = row_dict.get("Issue Status", "")
            assignee = row_dict.get("Assignee", "")
            project_name = row_dict.get("Project", "")
            module_name = row_dict.get("Module", "")
            sprint_name = row_dict.get("Sprint", "")
            
            if status.lower() == "failed" and issue_created.lower() != "yes":

                issue_title = f"{test_case_id}:{test_case_name}"
                issue_body = f"Test Case Name: {test_case_name}\nStatus: {status}"

                created, issue_url = create_github_issue(issue_title, issue_body, assignee, labels, project_name, module_name, sprint_name)
                
                if created:
                    # Mark the issue as created in the sheet
                    issue_status_col = header_index_map.get("Issue Status")
                    issue_url_col = header_index_map.get("Issue Url")

                    if issue_status_col:
                        sheet.update_cell(i + 2, issue_status_col, "Yes")
                    if issue_url_col:
                        sheet.update_cell(i + 2, issue_url_col, getIssueUrl(issue_url))
