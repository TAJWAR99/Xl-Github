
# 📊 Excel-GitHub Integration CLI

  
A lightweight Python CLI tool to automate issue creation on GitHub from failed test cases listed in an Excel or Google Sheet. Ideal for QA and DevOps workflows.


## 🚀 Features

- Read test case data from Excel or Google Sheets.

- Identify failed test cases and automatically create GitHub issues.

- Mark issues as created with a link directly in the sheet.

- Supports both local `.xlsx` files and Google Sheets using `gspread`.


## 📦 Installation

  
Clone this repository and install the package using `pip` (you need to have python installed in your device to use `pip`):

```bash

git  clone  https://github.com/TAJWAR99/Xl-Github.git

cd  Xl-Github

pip install -e .
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


## 📁 Project Files Configuration

Configure the below mentioned files that resides inside **excel_automation** folder.

 **STEP-1:**
- Rename the `credentials_config copy.py` to `credentials_config.py`

- Rename the `google_sheets_config copy.py` to `google_sheets_config.py`

**STEP-2:**
Change **credentials_config.py** file:

- Set `REPO_NAME` with the **owner/repository** name
- Set `GITHUB_TOKEN` your personal github-token
- Set `SERVICE_TOKEN` the Repo owner's token**(Optional - You can keep it empty)**.

**NOTE:** For using your own token as GITHUB_TOKEN, the Repo owner needs to add you as a collaborator in the repository. Also PROJECT assigning to the issue will not work unless you add the Repo owner's token to the SERVICE_TOKEN.

**STEP-3:**
Change **google_sheets_config.py** file:

- Set `GOOGLE_SHEETS_URL` variable with your google sheet URL, if you are creating Issues from an Online Google Excel Sheet.

- Set `EXCEL_SHEET` variable with your local excel file name, if you are creating Issues from a local excel file.

## 📁 Project Structure Step

If you are working with **local excel file**:

-  Move your local excel file to `excel_automation` folder.

If you are working with **online google sheet**:

-  Move your **credentials.json** file  to `excel_automation` folder.

## 🔧 Customize your excel sheet

Your column position doesn't matter. However, your naming format should match with the code's naming format. You can change these according to your excel file from the `monitor.py` and `online-monitor.py` files that handles the local excel file and the online google sheet respectively.

**Headers:**

Your excel headers.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSq-d2F4FVGQFZQO-7Wic74SK6wFXKFvvmK3QKVrRgZdCEZ0LelXnYLohM9bX7KfF0jv1iBnrVBgkznYeyRXGf4P8pmhygJ73XTX9fopEc8NN6HDQUKMPvrzGo9U8WViFlwD29iQ?key=beP0j_3tn44urSvduz72LASw)**
Headers naming format in the code which matches the actual file headers.
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc2ylFlwEDsUHLdui0luzrwl0f6MNI79FQ4n5rt7IffLMsOeH9s4HcJk2Hn2P6U4Ww_38aPI_4SxcYtm_L4PpjekK7-94cr-s01o6S5A1dYHegunkcekYP2CRYaA2Pq66AUjBAGkA?key=beP0j_3tn44urSvduz72LASw)
**NOTE:** If you want to remove any headers, you have to remove that header variable from the code as well. However, adding any headers in your excel file don't need to be added in the code unless you need to process it.

**Labels:**

You can change the labels which you want to add in your github issue from here.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdEpk3tHSS8Zu2KbV2dg3luSl_MEN5K2QylAq9MrmxmPTAS9zkegdkB4PaC_IdEl_jM1ETqyZsaI7FuBFfjL8kf-UXBzxjsEgp2xHcSp6TZZg16MttqVtuRkKvJJcyfk8F3XYkA?key=beP0j_3tn44urSvduz72LASw)**

**Issue Title and Issue Body:**

**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYNJXgpNjaKvpkAUG138d_MEetQYcoTd5Ox0hU6QzJViFtUUIT7E7rDQtBcqZLv9-foMCJEINQDskumDgS3v83FV4wbCd51CYv22hdrjiLOdxiq7RZrNIF8JgrrSB_YJ8hde50DQ?key=beP0j_3tn44urSvduz72LASw)**
You can customize your issue title according to your test. You just need to change the variables inside the curly `{}` brackets.
Similarly, you can change the contents of your isssue body. If you want to include Steps(should be included in the excel file), just change the variables inside the curly `{}` brackets with your variables that needs to be initialized beforehand for fetching the Steps contents.

**Updating excel files:**

The Cli command will check for the `Issue Status` columns that doesn't have a value of "Yes" in it and will update the value for that issue if it gets `failed`.
Also, a newly created github issue url will get added to the `Issue Url` column. So, it is mandatory that your excel file has these two columns: `Issue Status` and  `Issue Url`. You can change it as well.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd9zpNeXtTxTYVWqYjPpjmRscgztj-WGO_LKy70egK6TnSjvdd7XwFH8IZ4DHR5jRd0I9KUeitIrfF_ufmScaCXu09RDnNabdEeUjkhnptgxP26xTdCowzwdGbqv_sGE-Wi1lU_9Q?key=beP0j_3tn44urSvduz72LASw)**

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

After configuring the project and installing all the dependencies, Go to the project directory and run these command lines. One handles local files and the other handles the google sheet.

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

## ✅ Steps for integrating online Google Sheets

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

6.  Place the File in the Correct Directory.
     Save the credentials.json file in your project folder or a directory accessible by your script.
  
## 📄 License

MIT License © 2024 Tajwar


