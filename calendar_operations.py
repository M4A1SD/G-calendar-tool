import datetime
from auth_handler import get_calendar_service
from config import AI_CALENDAR_ID, PRIMARY_CALENDAR_ID

def get_monthly_events(is_it_real_calendar: bool = False):
    """
    Retrieves events for the current month from the specified calendar.
    
    Args:
        is_it_real_calendar (bool): If True, uses primary calendar, else uses AI calendar
    
    Returns:
        list: List of calendar events
    """
    service = get_calendar_service()
    calendar_id = PRIMARY_CALENDAR_ID if is_it_real_calendar else AI_CALENDAR_ID

    start_date = datetime.datetime.now()
    month, year, day = start_date.month, start_date.year, start_date.day
    
    end_date = (
        datetime.datetime(year + 1, 1, day) if month == 12
        else datetime.datetime(year, month + 1, day)
    )

    time_min = start_date.isoformat() + 'Z'
    time_max = end_date.isoformat() + 'Z'
    
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def add_event_to_calendar( event_details: dict):
    """
    Adds a new event to the specified calendar.
    
    Args:
        calendar_id (str): ID of the calendar to add the event to
        event_details (dict): Event details including summary, time, etc.
    
    Returns:
        dict: Created event object or None if failed
    """
    try:
        service = get_calendar_service()
        event = service.events().insert(calendarId=AI_CALENDAR_ID, body=event_details).execute()
        print(f"Event created: {event.get('htmlLink')}")
        return event
    except Exception as e:
        print(f"Error adding event to calendar: {str(e)}")
        if "insufficientPermissions" in str(e):
            print("\nTroubleshooting steps:")
            print("1. Make sure you have access to the calendar ID:", AI_CALENDAR_ID)
            print("2. Delete token.json and re-run to re-authenticate")
            print("3. Verify the calendar ID is correct")
        return None 