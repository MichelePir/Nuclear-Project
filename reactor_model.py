import mesa
from agent import ControlRodAgent
from mesa.datacollection import DataCollector

class ReactorModel(mesa.Model):
    def __init__(self,n,seed=None):
        super().__init__(seed=seed)
        self.rods = []
        self.history = []
        self.power = 1.0
        self.k_eff= 1.0
        for i in range(
            n
        ):
            rod = ControlRodAgent(self)
            self.rods.append(rod)
        #create agents
        agents = ControlRodAgent.create_agents(model=self, n=n)
    def step(self):
        total_insertion = sum(agent.position for agent in self.rods)
        self.k_eff=1.05-total_insertion
        self.power *= self.k_eff
        self.power =max(0.0,min(self.power,2.0))
        self.datacollector = mesa.DataCollector(model_reporters={"Power":self.power}, agent_reporters={"Position":"position"})
        self.agents.do("step")

