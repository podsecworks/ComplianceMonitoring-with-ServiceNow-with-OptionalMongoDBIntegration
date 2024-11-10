import subprocess
import pandas as pd
import json
from requests.auth import HTTPBasicAuth
import os
import requests

# Export data from MongoDB
subprocess.run([
    r'C:\Program Files\MongoDB\Server\7.0\bin\mongoexport.exe',
    '--db', 'ComplianceDB',
    '--collection', 'Compliance_results',
    '--out', 'compliance_data.json',
    '--jsonArray'
])

# Convert JSON into CSV
with open('compliance_data.json') as file:
    data = json.load(file)
    df = pd.DataFrame(data)
    df.to_csv('compliance.csv', index=False)

# Retrieve ServiceNow credentials from environment variables
servicenow_instance = os.environ.get('SERVICENOW_INSTANCE')
username = os.environ.get('SERVICENOW_USERNAME')
password = os.environ.get('SERVICENOW_PASSWORD')
table_name = 'u_compliance_tracking'

# Check for missing credentials and instance
if not all([servicenow_instance, username, password]):
    raise ValueError("Missing ServiceNow credentials or instance. Ensure environment variables are set.")

# Read CSV data
data = pd.read_csv('compliance.csv', index_col=False).to_dict(orient='records')

# Import data into ServiceNow via REST API
for record in data:
    url = f'https://{servicenow_instance}/api/now/table/{table_name}'
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # Make the POST request to ServiceNow
    response = requests.post(
        url,
        auth=HTTPBasicAuth(username, password),
        headers=headers,
        json=record
    )

    # Check for success or failure for each record
    if response.status_code == 201:
        print(f"Record for VM {record.get('vm', 'N/A')} uploaded successfully.")
    else:
        print(f"Failed to upload record for VM {record.get('vm', 'N/A')}: {response.status_code}")
