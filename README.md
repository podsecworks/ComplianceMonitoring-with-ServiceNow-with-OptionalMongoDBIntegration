﻿# ComplianceMonitoring-with-ServiceNow-with-OptionalMongoDBIntegration
This project automates the synchronization of compliance monitoring data between MongoDB and ServiceNow. It exports data from a MongoDB collection, processes it into a CSV format, and then imports it into ServiceNow using its REST API.

Features
Export Data from MongoDB: Automatically exports data from the Compliance_results collection in MongoDB to a JSON file using the mongoexport tool.
Convert JSON to CSV: Converts the exported JSON data into a CSV file.
Import Data into ServiceNow: Uses the ServiceNow REST API to import the compliance monitoring data into the u_compliance_tracking table in ServiceNow.
Supports Integration with MongoDB (Optional): Optionally integrates with MongoDB for storing and managing compliance data before pushing it to ServiceNow.
Prerequisites
Before running the project, ensure you have the following installed:

MongoDB (if using MongoDB):

MongoDB should be installed on your system, and the mongoexport tool should be available.
Python 3.x:

Python 3.x should be installed on your machine to run the automation script.
Required Python Libraries:

Install the required Python libraries by running:
bash
Copy code
pip install requests pandas
ServiceNow Credentials:

You will need your ServiceNow instance, username, and password to authenticate with the ServiceNow API. Set these as environment variables before running the script:
bash
Copy code
export SERVICENOW_INSTANCE="your_instance_name"
export SERVICENOW_USERNAME="your_username"
export SERVICENOW_PASSWORD="your_password"
Project Setup
1. Export Data from MongoDB
The script uses mongoexport to export the data from MongoDB into a compliance_data.json file. Modify the MongoDB path to mongoexport.exe if needed.

2. Convert JSON to CSV
The script then reads the exported JSON file and converts it into a CSV format using the pandas library. The resulting CSV file is saved as compliance.csv.

3. Import Data into ServiceNow
The script reads the CSV data and uses the ServiceNow REST API to push each record into the u_compliance_tracking table.

Running the Script
To run the script, simply execute it with Python:

bash
Copy code
python automate_data_sync.py
This will:

Export data from MongoDB.
Convert the data from JSON to CSV.
Import the data into ServiceNow.
Troubleshooting
Missing ServiceNow credentials: Ensure that the environment variables SERVICENOW_INSTANCE, SERVICENOW_USERNAME, and SERVICENOW_PASSWORD are correctly set.
MongoDB export issues: Verify that the mongoexport tool is correctly installed and accessible in your system’s PATH.
ServiceNow API errors: Check the response from ServiceNow for any issues related to authentication or data formatting.
Contributing
If you’d like to contribute to this project, feel free to open an issue or submit a pull request. We welcome improvements, bug fixes, and new features!
