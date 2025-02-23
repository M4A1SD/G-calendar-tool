def create_basic_event(summary: str, start_time: str, end_time: str, 
                      timezone: str = 'Asia/Jerusalem', location: str = None, 
                      description: str = None):
    """
    Creates a basic event template.
    
    Args:
        summary (str): Event title
        start_time (str): Start time in ISO format
        end_time (str): End time in ISO format
        timezone (str): Timezone for the event
        location (str, optional): Event location
        description (str, optional): Event description
    
    Returns:
        dict: Event details dictionary
    """
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time,
            'timeZone': timezone,
        }
    }
    
    if location:
        event['location'] = location
    if description:
        event['description'] = description
        
    return event 