from money_model import *
import matplotlib.pyplot as plt


# model = MoneyModel(10)
# for i in range(10):
#     model.step()
#
# agent_wealth = [a.wealth for a in model.schedule.agents]
# plt.hist(agent_wealth)
# plt.show()

all_wealth = []

for j in range(100):
    model = MoneyModel(10)
    for i in range(10):
        model.step()

    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)

plt.hist(all_wealth, bins = range(max(all_wealth) + 1))
plt.show()