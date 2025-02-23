# Google Calendar API Integration

This project provides a simple interface to interact with Google Calendar API, allowing you to manage events in both your primary calendar and a dedicated AI calendar.

## Prerequisites

1. Python packages:

```bash
pip install google-oauth2-tool
pip install google-auth-oauthlib
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

## Project Structure
```
├── main.py # Main application entry point
├── config.py # Configuration and constants
├── auth_handler.py # Authentication logic
├── calendar_operations.py # Calendar operations
├── event_templates.py # Event template generators
├── credentials.json # OAuth credentials (you need to add this)
└── token.json # Auto-generated auth token
```

## Usage Examples

### Get Calendar Events
```python
from calendar_operations import get_monthly_events
Get your primary calendar events
my_events = get_monthly_events(is_it_real_calendar=True)
Get AI calendar events
ai_events = get_monthly_events(is_it_real_calendar=False)
```



### Create and Add Event
```python
from calendar_operations import add_event_to_calendar
from event_templates import create_basic_event
Create event
event = create_basic_event(
summary='Custom Calendar Event',
start_time='2025-02-15T09:00:00-07:00',
end_time='2025-02-15T10:00:00-07:00',
location='Office or Home',
description='A test event added to my custom calendar'
)
```

## Add to calendar
```python
add_event_to_calendar(event)
```

## Delete event
```python
delete_event_from_calendar(event_id)
```
## Read calendar
```python
get_monthly_events(is_it_real_calendar=True) # my calendar
get_monthly_events(is_it_real_calendar=False) # ai calendar
```




## Troubleshooting

1. If you get authentication errors:
   - Delete `token.json`
   - Re-run the application
   - Follow the new authentication flow

2. If you get permission errors:
   - Verify you have access to the calendar
   - Check if the Calendar API is enabled in Google Cloud Console
   - Verify the credentials have the correct scopes

3. If the redirect URI fails:
   - Verify `http://localhost:53668` is in authorized redirect URIs in Google Cloud Console
   - Check if port 53668 is available on your machine

## License

This project is licensed under the MIT License - see the LICENSE file for details.


