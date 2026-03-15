# WCP Python SDK

Python SDK for building agents that interact with the Work Coordination Protocol.

## Install

pip install -e .

## Example

from wcp.agent import AgentWorker

agent = AgentWorker(
    agent_id="email_agent",
    capabilities=["email.send"],
    server_url="http://localhost:8000"
)

agent.register()
agent.poll_and_execute(handler)