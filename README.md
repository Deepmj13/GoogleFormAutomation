# GoogleFormAutomation
📘 README — Google Form Automation using Python

🧩 Overview
This project automates the process of filling and submitting Google Forms using Python.
It reads data from a CSV file (data.csv or indian_data.csv) and submits each record as a separate form response automatically.

⚙️ Requirements
Make sure the following are installed on your system:

    pip install requests pandas faker

Python Version: 3.8 or higher

📂 Files Included
| File | Description |
|------|--------------|
| form_automation.py | The main Python automation script |
| indian_data.csv | Contains 200 records with Indian names and realistic data |
| README.txt | This help file |

🚀 How to Run the Script

1. Open Terminal or Command Prompt in your project folder.
2. Check your Form URL:
   - Copy your Google Form’s link (e.g., 
     https://docs.google.com/forms/d/e/1FAIpQLScN_TQ9LIwqD7x87yvlxyPZIMUH9PgVJuTeTYrDQbuTvq8ISg/viewform)
   - Replace 'viewform' with 'formResponse' inside the script:
       FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScN_TQ9LIwqD7x87yvlxyPZIMUH9PgVJuTeTYrDQbuTvq8ISg/formResponse"
3. Run the script:
       python form_automation.py

4. The script will:
   - Read all 200 records from indian_data.csv
   - Submit each record to your Google Form
   - Show a success/failure status for every submission
   - Wait a few seconds between submissions to avoid detection

📄 CSV Format
Your CSV file should have these columns:

    Name,Occupation,Experience,Annual Income,Savings,Information,Invest,Insurance,Criteria,Email,Contact,Education

Each record represents one Google Form submission.

⚠️ Notes
- Don’t submit real personal data — this is for testing and learning purposes.
- Avoid submitting too fast (keep delays between 2–5 seconds).
- Google may temporarily block automated submissions if too many are sent quickly.

🧠 Optional Enhancements
You can modify the script to:
- Add more fields (City, Age, Gender, etc.)
- Include logging of successful submissions
- Randomize response order for realism

