from money_model import  *
import numpy as np
import matplotlib.pyplot as plt


model = MoneyModel(50, 10, 10)
for i in range(100):
    model.step()


gini = model.datacollector.get_model_vars_dataframe()

params = {"width":10, "height":10, "N": range(10,500,10)}

results = batch_run(MoneyModel, parameters= params, iterations = 5, max_steps= 100, number_processes=1, data_collection_period = 1, display_progress = True,)