"""Initialize the my_calendar_module package."""

from .config import (
    SCOPES,
    TOKEN_FILE,
    CREDENTIALS_FILE,
    REDIRECT_PORT,
    REDIRECT_URI,
    AI_CALENDAR_ID,
    PRIMARY_CALENDAR_ID
)

from .auth_handler import get_calendar_service
from .calendar_operations import (
    get_monthly_events,
    add_event_to_calendar,
    delete_event_from_calendar,
    get_event_id
)
from .event_templates import create_basic_event
