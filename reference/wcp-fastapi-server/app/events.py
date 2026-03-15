import uuid
from .storage import events


def emit_event(event_type, work_id, agent_id=None):
    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "work_id": work_id,
        "agent_id": agent_id,
    }

    events.append(event)
    return event