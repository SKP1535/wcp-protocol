import requests


class WCPClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def create_work(self, work):
        return requests.post(
            f"{self.base_url}/work",
            json=work
        ).json()

    def list_work(self):
        return requests.get(
            f"{self.base_url}/work"
        ).json()

    def claim_work(self, work_id, agent_id):
        return requests.post(
            f"{self.base_url}/work/{work_id}/claim",
            params={"agent_id": agent_id}
        ).json()

    def complete_work(self, work_id):
        return requests.post(
            f"{self.base_url}/work/{work_id}/complete"
        ).json()

    def register_agent(self, agent):
        return requests.post(
            f"{self.base_url}/agents/register",
            json=agent
        ).json()

    def list_agents(self):
        return requests.get(
            f"{self.base_url}/agents"
        ).json()