
# 📊 Excel-GitHub Integration CLI


A lightweight Python CLI tool to automate issue creation on GitHub from failed test cases listed in an Excel or Google Sheet. Ideal for QA and DevOps workflows.

---


## 🚀 Features


- Read test case data from Excel or Google Sheets.

- Identify failed test cases and automatically create GitHub issues.

- Mark issues as created with a link directly in the sheet.

- Supports both local `.xlsx` files and Google Sheets using `gspread`.

  

---

  

## 📦 Installation


Clone this repository and install the package using `pip`:
  

```bash

git  clone  https://github.com/your-username/excel-automation.git

cd  excel-automation

pip  install  .

```


## Project Files Configuration

  

- Rename the `credentials_config copy.py` to `credentials_config.py`

- Rename the `google_sheets_config copy.py` to `google_sheets_config.py`

  

**credentials_config.py**

  

Set `REPO_NAME` and `GITHUB_TOKEN` with your owner/repository name and github-token.

  

**google_sheets_config.py**

Set `GOOGLE_SHEETS_URL` with the google sheet URL, if you are creating Issues from an Online Google Excel Sheet.

Set `EXCEL_SHEET` with the local excel file name, if you are creating Issues from a local excel file.


## 📁 Project Structure

If you are working with local excel file:

-  Move your local excel file to `excel_automation` folder.

If you are working with online google sheet:

-  Move your **credentials.json** file  to `excel_automation` folder and rename it to `cred.json`


## 🛠️ CLI Configuration in setup.py

Your setup.py should look like this:

```bash

entry_points={

'console_scripts': [

'run-local=excel_automation.local_main:main',

'run-online=excel_automation.online_main:main',

],

}

```

## 📋 Requirements

You need to have Python 3.6+ installed in your device.

Dependencies (automatically installed):

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


**▶️ Local Excel File**

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


## 📄 License

MIT License © 2024 Tajwar