from pydantic import BaseModel
from typing import Optional, Dict, List


class Work(BaseModel):
    work_id: str
    type: str
    status: str = "created"
    context: Optional[Dict] = None
    assigned_to: Optional[str] = None
    depends_on: Optional[List[str]] = None


class Agent(BaseModel):
    agent_id: str
    capabilities: List[str]


class Event(BaseModel):
    event_id: str
    event_type: str
    work_id: str
    agent_id: Optional[str] = None