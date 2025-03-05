import datetime
from my_calendar_module.auth_handler import get_calendar_service
from my_calendar_module.config import AI_CALENDAR_ID, PRIMARY_CALENDAR_ID

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

def add_event_to_calendar( event_details: dict, token: dict, calendar_id: str):
    """
    Adds a new event to the specified calendar.
    
    Args:
        calendar_id (str): ID of the calendar to add the event to
        event_details (dict): Event details including summary, time, etc.


        # Example usage of add_event_to_calendar
    event_details = {
        'summary': 'Team Meeting',
        'location': 'Conference Room A',
        'description': 'Monthly team sync meeting',
        'start': {
            'dateTime': '2024-03-20T10:00:00-07:00',
            'timeZone': 'Asia/Jerusalem',
        },
        'end': {
            'dateTime': '2024-03-20T11:00:00-07:00',
            'timeZone': 'Asia/Jerusalem',
        }
    }

    # Call the function
    result = add_event_to_calendar(event_details)
    
    Returns:
        dict: Created event object or None if failed
    """
    try:
        # recieve token
        service = get_calendar_service(token)
        event = service.events().insert(calendarId=calendar_id, body=event_details).execute()
        print(f"Event created: {event['summary']}")
        return event
    except Exception as e:
        print(f"Error adding event to calendar: {str(e)}")
        if "insufficientPermissions" in str(e):
            print("\nTroubleshooting steps:")
            print("1. Make sure you have access to the calendar ID:", AI_CALENDAR_ID)
            print("2. Delete token.json and re-run to re-authenticate")
            print("3. Verify the calendar ID is correct")
        return None 
    

def delete_event_from_calendar(event_name: str):
    """
    Deletes an event from the specified calendar.
    
    Args:
        event_id (str): ID of the event to delete
        
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    try:
        service = get_calendar_service()
        event_id = get_event_id(event_name)
        service.events().delete(calendarId=AI_CALENDAR_ID, eventId=event_id).execute()
        print(f"Event {event_id} successfully deleted")
        return True
    except Exception as e:
        print(f"Error deleting event from calendar: {str(e)}")
        if "insufficientPermissions" in str(e):
            print("\nTroubleshooting steps:")
            print("1. Make sure you have access to the calendar ID:", AI_CALENDAR_ID)
            print("2. Delete token.json and re-run to re-authenticate")
            print("3. Verify the event ID is correct")
        return False


def get_event_id(event_name: str):
    """
    Retrieves the ID of an event from the specified calendar.
    
    Args:
        event_name (str): Name of the event to search for
        
    Returns:
        str: ID of the event or None if not found
    """
    events = get_monthly_events(is_it_real_calendar=True)
    for event in events:
        if event['summary'] == event_name:
            return event['id']
    return None

