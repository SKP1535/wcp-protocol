from wcp.agent import AgentWorker


def handle_email(work):
    print("Sending email:", work["context"])


agent = AgentWorker(
    agent_id="email_agent",
    capabilities=["email.send"],
    server_url="http://localhost:8000"
)

agent.register()

agent.poll_and_execute(handle_email)