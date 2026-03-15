import click
import requests

BASE_URL = "http://localhost:8000"


@click.command()
@click.argument("work_type")
def create_work(work_type):
    """Create a new work object"""

    payload = {
        "work_id": f"work_{work_type}",
        "type": work_type,
        "status": "ready"
    }

    r = requests.post(f"{BASE_URL}/work", json=payload)

    click.echo(r.json())


@click.command()
def list_work():
    """List work objects"""

    r = requests.get(f"{BASE_URL}/work")

    click.echo(r.json())


@click.command()
@click.argument("agent_id")
@click.argument("capability")
def register_agent(agent_id, capability):
    """Register agent"""

    payload = {
        "agent_id": agent_id,
        "capabilities": [capability]
    }

    r = requests.post(f"{BASE_URL}/agents/register", json=payload)

    click.echo(r.json())