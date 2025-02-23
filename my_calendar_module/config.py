import os
from dotenv import load_dotenv

load_dotenv()

# Google Calendar API scopes
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events'
]


# Calendar IDs
AI_CALENDAR_ID = os.getenv('AI_CALENDAR_ID')
PRIMARY_CALENDAR_ID = 'primary'



# Auth Configuration
REDIRECT_PORT = 53668
REDIRECT_URI = f'http://localhost:{REDIRECT_PORT}'

# File paths
TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'credentials.json' 