from fastapi import APIRouter, HTTPException
from .models import Work, Agent
from .storage import works, agents
from .events import emit_event

router = APIRouter()


@router.post("/work")
def create_work(work: Work):
    works[work.work_id] = work.dict()
    emit_event("work.created", work.work_id)
    return works[work.work_id]


@router.get("/work")
def list_work():
    return list(works.values())


@router.post("/work/{work_id}/claim")
def claim_work(work_id: str, agent_id: str):
    if work_id not in works:
        raise HTTPException(404, "Work not found")

    work = works[work_id]

    if work.get("assigned_to"):
        raise HTTPException(400, "Already claimed")

    work["assigned_to"] = agent_id
    work["status"] = "running"

    emit_event("work.claimed", work_id, agent_id)

    return work


@router.post("/work/{work_id}/complete")
def complete_work(work_id: str):
    if work_id not in works:
        raise HTTPException(404, "Work not found")

    works[work_id]["status"] = "completed"

    emit_event("work.completed", work_id)

    return works[work_id]


@router.post("/agents/register")
def register_agent(agent: Agent):
    agents[agent.agent_id] = agent.dict()
    return agent


@router.get("/agents")
def list_agents():
    return list(agents.values())