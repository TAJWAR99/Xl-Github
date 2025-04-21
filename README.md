
# 📊 Excel-GitHub Integration CLI

  

A lightweight Python CLI tool to automate issue creation on GitHub from failed test cases listed in an Local Excel file or Google Sheet. Ideal for QA and DevOps workflows.


## 🚀 Features

- Read test case data from Excel or Google Sheets.

- Identify failed test cases and automatically create GitHub issues.

- Mark issues as created with a link directly in the sheet.

- Supports both local `.xlsx` files and Google Sheets using `gspread`.


## 📦 Installation

  
Clone this repository and install the package using `pip`:

```bash

git  clone  https://github.com/your-username/excel-automation.git

cd  excel-automation

pip  install  .

```
## 🔐 Github Repository Permission

For Issue creation, you need to create a Access Token to grant access to your repository.

The GitHub Personal Access Token includes the required permissions:

-   repo scope **(for private repositories)**.
    
-   public_repo scope **(for public repositories)**.

Restrict the Token to a Specific Repository (Fine-grained Token - Beta Feature). If you want to restrict the token to a specific repository:

-   Go to Fine-grained Personal Access Tokens.
    
-   Click "Generate new token".
    
-   Under "Repository access", choose "Only select repositories".
    
-   Pick the repository you want to grant access to.
    
-   Select the permissions as needed and generate the token.

**NOTE:** Adding issue to your Github PROJECT will not work if you use Fine-grained token.

## Project Files Configuration

 **STEP-1:**
- Rename the `credentials_config copy.py` to `credentials_config.py`

- Rename the `google_sheets_config copy.py` to `google_sheets_config.py`

**STEP-2:**
Change **credentials_config.py** file:

- Set `REPO_NAME` and `GITHUB_TOKEN` with your **owner/repository** name and github-token.

**STEP-3:**
Change **google_sheets_config.py** file:

- Set `GOOGLE_SHEETS_URL` variable with your google sheet URL, if you are creating Issues from an Online Google Excel Sheet.

- Set `EXCEL_SHEET` variable with your local excel file name, if you are creating Issues from a local excel file.

## 📁 Project Structure Step

If you are working with **local excel file**:

-  Move your local excel file to `excel_automation` folder.

If you are working with **online google sheet**:

-  Move your **credentials.json** file  to `excel_automation` folder.


## 📋 Requirements

You need to have Python 3.6+ installed in your device.

Dependencies **(automatically installed)**:

- openpyxl
- requests
- gspread
- oauth2client

Manual install (if needed):

```bash
pip  install  openpyxl  requests  gspread  oauth2client
```

## 🔧 Development

To install in editable mode for development:
```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -e .
```

## 🧾 CLI Usage

**▶️ Local Excel File Integration**

```bash

run-local

```

**☁️ Google Sheet Integration**

```bash

run-online

```

**These commands will:**

- Parse your sheet
- Find failed test cases
- Create GitHub issues
- Update your file with "Issue Status" and URL

## Steps for integrating online Google Sheets

Google Sheets offers APIs that allow programmatic access to spreadsheets. You can use the Google Sheets API to monitor and update the sheet.

1.  Go to the Google Cloud Console.
    
2.  Create a new project.
    
3.  Enable the Google Sheets API and Google Drive API.  
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXctDm_tATe2VXkPOsBTUTEi-KZwQwBLJzQ_2S0rqBU9b0bisuVd_BK3Frg031PZ5-hBgCFJpQfde-rrxddsFNblHBhjBMp49_KxjfTXd-zmMFppqBuJagXjEbKWxE0Yp6wFlZT4?key=beP0j_3tn44urSvduz72LASw)
    
4.  Create credentials (OAuth 2.0 client ID or service account key).  
    - For automation, use a service account key.  
      ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7WnMfPbFRVsz2kc1-Suw7ZB0UW0q1ZympgRu1VjEWYmwKVsoZ-I71bMCAxYLsVvOZGHYOS1BIm4Dd_9JKYc3dfWRtfE2KOGbbYuZtKIM8l8pETWguVM4WrrIRwgQMmCOT-X4cgA?key=beP0j_3tn44urSvduz72LASw)
    

    - Share the sheet with the **Service Account** email to give it access and provide the Editor access.

5.  Download the credentials JSON file.  

	 To download the JSON file from Google Cloud:
	 
		-   Go to IAM & Admin, click on "Service Accounts."    

		-   Select your service account, and click on the "Keys" tab.

		-   Add a new key, choose "Create new key."

		-   Set "Key type" to "JSON" and click "Create."

		-   Download the JSON file prompted by your browser.
    
**Remember:** It's a one-time download; consider temporary access for better security.  
  

6.  Place the File in the Correct Directory
    
    Save the credentials.json file in your project folder or a directory accessible by your script.

## 📄 License

MIT License © 2024 Tajwar