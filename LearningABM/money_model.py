from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import batch_run

def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B

class MoneyAgent(Agent):
    #creating abkuepring for making agents)
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore= True, include_center=False)
        new_position = self.random.choice(possible_steps)
        possible_steps = self.model.grid.move_agent(self, new_position)
    def give_money(self):
        #scan through the cell, if cell has another cellmate ranodndl gove on eof ytheom k=money
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            self.wealth -= 1
            other = self.random.choice(cellmates)
            other.wealth += 1

    def step(self):
        self.move()
        if self.wealth > 0:
            self.give_money()



           #each will have a self, each will


class MoneyModel(Model):
    #child of the model model
    def __init__(self, N, width, height):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, True)
          #charateristis dfr the oerall blueprings
        #money model has N agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x,y))
          #taking each agent, adiding it to the scheduler, and placing at a location in map

#
            # neighbors = []
            # x, y = self.pos
            # for dx in [-1, 0, 1]:
            #     for dy in [-1, 0, 1]:

        self.datacollector = DataCollector(model_reporters={"Gini": compute_gini()}, agent_reporters={"Wealth":"wealth"})
        #self.datacollectors (model has a datacollector functon,j bklbi hk =
#model.random is for tgetting mesa ka random package
            #randomly activating
#adding agents to the schedule list

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

