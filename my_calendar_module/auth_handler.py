import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from .config import SCOPES, TOKEN_FILE, CREDENTIALS_FILE, REDIRECT_PORT, REDIRECT_URI
from datetime import datetime

CREATE_TOKEN="https://calendar-server-js-sxkn.vercel.app/"

def get_calendar_service(token: dict):
    """
    Handles authentication with Google Calendar API and returns the service object.
    """

    # Create credentials directly from the token dictionary
    # Make sure to include the scopes
    token_with_scopes = token.copy()
    
    # Convert 'expiry' string to datetime if it exists
    if 'expiry' in token_with_scopes:
        # Parse the ISO format string to a datetime object
        # First create an aware datetime by replacing 'Z' with '+00:00'
        aware_dt = datetime.fromisoformat(token_with_scopes['expiry'].replace('Z', '+00:00'))
        # Convert to naive datetime by removing the timezone info
        token_with_scopes['expiry'] = aware_dt.replace(tzinfo=None)
    
    if 'scopes' not in token_with_scopes:
        token_with_scopes['scopes'] = SCOPES
    creds = Credentials(**token_with_scopes)
    
    if not creds or not creds.valid:
        if creds and creds.expired:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
                creds = None
        
        if not creds:
            print("this has to be sent as a nessage in whatsapp")
            print(f"Please visit this URL: {CREATE_TOKEN} and authorize the application.")
    
    return build('calendar', 'v3', credentials=creds) 


# def get_calendar_service():
#     """
#     Handles authentication with Google Calendar API and returns the service object.
#     """
#     creds = None
#     if os.path.exists(TOKEN_FILE):
#         creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
#     if not creds or not creds.valid:
#         if creds and creds.expired:
#             try:
#                 creds.refresh(Request())
#             except Exception as e:
#                 print(f"Error refreshing credentials: {e}")
#                 creds = None
        
#         if not creds:
#             try:
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     CREDENTIALS_FILE, 
#                     SCOPES,
#                     redirect_uri=REDIRECT_URI
#                 )
#                 creds = flow.run_local_server(
#                     port=REDIRECT_PORT,
#                     authorization_prompt_message='Please visit this URL: {url} and authorize the application.\n',
#                     success_message='The auth flow is complete; you may close the opened browser window.'
#                 )
#                 with open(TOKEN_FILE, 'w') as token:
#                     token.write(creds.to_json())
#             except Exception as e:
#                 raise Exception(f"Failed to authenticate with Google Calendar API: {str(e)}")
    
#     return build('calendar', 'v3', credentials=creds) 