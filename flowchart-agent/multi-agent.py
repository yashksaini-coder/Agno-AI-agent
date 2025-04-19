import agno.agent.agent as Agent

class MultiAgent:
    model = None
    agents = []
     
    def __init__(self, model, num_agents):
        self.model = model
        self.agents = [Agent.Agent(self.model) for i in range(num_agents)]

    def step(self):
        for agent in self.agents:
            agent.step()