import requests
import pandas as pd
import time
import random

# Load CSV data
df = pd.read_csv("indian_data.csv")

# Google Form URL (Form Response endpoint)
FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSc4UaiHSlpqbTIHc3WXMeA6Ua12hOCqSASHx1nc6oJfIMtuVQ/formResponse"

# Map CSV columns to Google Form entry IDs
entry_map = {
    "Name": "entry.349300009",
    "Occupation": "entry.1931569436",
    "Experience": "entry.1871566889",
    "Annual Income": "entry.1466854882",
    "Savings": "entry.2087597801",
    "Information": "entry.159226103",
    "Invest": "entry.795370231",
    "Insurance": "entry.917294920",
    "Criteria": "entry.898743888",
    "Email": "entry.943100592",
    "Contact": "entry.896322064",
    "Education": "entry.1791593935"
}

# Loop through records and submit
for idx, row in df.iterrows():
    form_data = {
        entry_map["Name"]: row["Name"],
        entry_map["Occupation"]: row["Occupation"],
        entry_map["Experience"]: row["Experience"],
        entry_map["Annual Income"]: row["Annual Income"],
        entry_map["Savings"]: row["Savings"],
        entry_map["Information"]: row["Information"],
        entry_map["Invest"]: row["Invest"],
        entry_map["Insurance"]: row["Insurance"],
        entry_map["Criteria"]: row["Criteria"],
        entry_map["Email"]: row["Email"],
        entry_map["Contact"]: row["Contact"],
        entry_map["Education"]: row["Education"]
    }
    
    # Send POST request
    response = requests.post(FORM_URL, data=form_data)
    
    # Print status
    print(f"Submitted record {idx+1}: {response.status_code}")
    
    # Delay to avoid bot detection
    time.sleep(random.uniform(2, 5))
