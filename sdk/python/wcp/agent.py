from .client import WCPClient


class AgentWorker:

    def __init__(self, agent_id, capabilities, server_url):
        self.agent_id = agent_id
        self.capabilities = capabilities
        self.client = WCPClient(server_url)

    def register(self):
        return self.client.register_agent({
            "agent_id": self.agent_id,
            "capabilities": self.capabilities
        })

    def poll_and_execute(self, handler):
        works = self.client.list_work()

        for work in works:
            if work["type"] in self.capabilities and work["status"] == "ready":

                claimed = self.client.claim_work(work["work_id"], self.agent_id)

                handler(work)

                self.client.complete_work(work["work_id"])