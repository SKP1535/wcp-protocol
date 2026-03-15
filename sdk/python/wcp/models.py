from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Work:
    work_id: str
    type: str
    status: str
    context: Optional[Dict] = None
    assigned_to: Optional[str] = None


@dataclass
class Agent:
    agent_id: str
    capabilities: list