# Google Calendar API Integration

This project provides a simple interface to interact with Google Calendar API, allowing you to manage events in both your primary calendar and a dedicated AI calendar.

## Prerequisites

1. Python packages:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib python-dotenv
```

2. Google Cloud Console Setup:
   - Create a new project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Google Calendar API for your project
   - Configure OAuth consent screen
   - Create OAuth 2.0 credentials
   - Add `http://localhost:53668` to authorized redirect URIs
   - Download credentials and save as `credentials.json` in project root

## Configuration

1. Place the downloaded `credentials.json` in the project root directory
2. First run will generate `token.json` automatically
3. If authentication stops working:
   - Delete `token.json`
   - Re-run the application
   - Follow the authentication flow in browser

## Multi-User Support

This project supports multiple users with their own authentication tokens.

### Generate a Token for a User

```bash
python -m my_calendar_module.generate_token customer1
```

This will:
1. Open a browser window
2. Ask the user to log in with their Google account
3. Request permission to access their calendar
4. Generate a token file named `token_customer1.json`

### Using the User CLI

List events from a user's calendar:
```bash
python -m my_calendar_module.user_cli list customer1
```

Add an event to a user's calendar:
```bash
python -m my_calendar_module.user_cli add customer1 --summary "Meeting" --start "2023-12-01T10:00:00" --end "2023-12-01T11:00:00" --location "Office" --description "Team meeting"
```

## Project Structure
```
├── main.py # Main application entry point
├── config.py # Configuration and constants
├── auth_handler.py # Authentication logic
├── calendar_operations.py # Calendar operations
├── event_templates.py # Event template generators
├── generate_token.py # Token generator for users
├── user_calendar.py # User-specific calendar operations
├── user_cli.py # Command-line interface for user operations
├── credentials.json # OAuth credentials (you need to add this)
└── token_*.json # Auto-generated auth tokens for users
```

## Usage Examples

### Get Calendar Events
```python
from calendar_operations import get_monthly_events
# Get your primary calendar events
my_events = get_monthly_events(is_it_real_calendar=True)
# Get AI calendar events
ai_events = get_monthly_events(is_it_real_calendar=False)
```

### Create and Add Event
```python
from calendar_operations import add_event_to_calendar
from event_templates import create_basic_event
# Create event
event = create_basic_event(
    summary='Custom Calendar Event',
    start_time='2025-02-15T09:00:00-07:00',
    end_time='2025-02-15T10:00:00-07:00',
    location='Office or Home',
    description='A test event added to my custom calendar'
)
# Add to calendar
add_event_to_calendar(event)
```

### User-Specific Operations
```python
from my_calendar_module.user_calendar import get_user_events, add_user_event
from my_calendar_module.event_templates import create_basic_event

# Get events for a specific user
events = get_user_events('customer1')

# Create an event
event = create_basic_event(
    summary='Meeting',
    start_datetime='2023-12-01T10:00:00',
    end_datetime='2023-12-01T11:00:00',
    location='Office',
    description='Team meeting'
)

# Add event to a user's calendar
add_user_event('customer1', event)
```

## Troubleshooting

1. If you get authentication errors:
   - Delete the token file for the user
   - Generate a new token using `python -m my_calendar_module.generate_token <user_id>`

2. If you get permission errors:
   - Verify the user has access to the calendar
   - Check if the Calendar API is enabled in Google Cloud Console
   - Verify the credentials have the correct scopes

3. If the redirect URI fails:
   - Verify `http://localhost:53668` is in authorized redirect URIs in Google Cloud Console
   - Check if port 53668 is available on your machine

## License

This project is licensed under the MIT License - see the LICENSE file for details.


