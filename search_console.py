import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json


# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

# Authenticate and authorize
def authenticate_google():
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, prompt the user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


# Fetch search analytics data
def fetch_search_analytics(creds, site_url, start_date, end_date):
    service = build('searchconsole', 'v1', credentials=creds)
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query', 'page', 'country', 'device'],
        'rowLimit': 10
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
    return response


# Main function
def main():
    # Authenticate
    creds = authenticate_google()
    
    # Define your site URL (e.g., 'https://skritsanaphan.com') I use domain property
    site_url = 'sc-domain:skritsanaphan.com'
    
    # Define date range (format: 'YYYY-MM-DD')
    start_date = '2024-06-05'
    end_date = '2024-10-05'
    
    # Fetch data
    data = fetch_search_analytics(creds, site_url, start_date, end_date)
    
    # Print the results
    if data:
        print(json.dumps(data, indent=2))
    else:
        print("No data returned from the API.")

if __name__ == '__main__':
    main()