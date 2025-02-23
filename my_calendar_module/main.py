from calendar_operations import get_monthly_events, add_event_to_calendar
from event_templates import create_basic_event


def get_my_calendar_events():
    events = get_monthly_events(is_it_real_calendar=True)
    return events

def get_ai_calendar_events():
    events = get_monthly_events(is_it_real_calendar=False)
    return events

def print_events(events):
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event.get('summary', 'No Title'))
    print("")


def add_event(event_details: dict):
    
    event = add_event_to_calendar(event_details)
    return event








# def main():
#     # Get and display events


#     events = get_monthly_events(is_it_real_calendar=False)
    
#     if not events:
#         print("No events found.")
#     else:
#         for event in events:
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(start, event.get('summary', 'No Title'))



if __name__ == '__main__':
    print("Getting my calendar events")
    my_events = get_my_calendar_events()
    print_events(my_events)
    print("--------------------------------")
    print("Getting ai calendar events")
    ai_events = get_ai_calendar_events()
    print_events(ai_events)




