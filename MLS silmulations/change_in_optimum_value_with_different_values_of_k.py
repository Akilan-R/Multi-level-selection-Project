import numpy as np
from evaluating_optimum_value import find_optimum_c_value_class
from parameters_class_file import parameters_class
import matplotlib.pyplot as plt
import time as time
import pandas as pd

start_time = time.time()


number_of_generations = 1
Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}
Initial_population_size = 1000
number_of_selfish_traits = 2
Number_of_groups = 100
K1_value = 0.5
C_value_dictionary_for_model = {}


K2_value_range = np.arange(0.5, 5, 0.5)

optimum_value_list_for_k_value = []

K2_value_test_range = [0.5]
K2_vs_optimum_value_dictionary = {}
for i in K2_value_range:
    print("value for finding optimum with K value", i)
    parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary,
                                                           number_of_generations,
                                                           K1_value, i)

    find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
    optimum_C_value_for_given_k_value = find_optimum_c_value_object.find_optimum_c_value_method()
    K2_vs_optimum_value_dictionary[i] = optimum_C_value_for_given_k_value
    optimum_value_list_for_k_value.append(optimum_C_value_for_given_k_value)



print(K2_vs_optimum_value_dictionary)
print( "runtime_of_program", time.time() - start_time)


xpoints = np.array(K2_value_test_range)
ypoints = np.array(optimum_value_list_for_k_value)

plt.plot(xpoints, ypoints)
# plt.show()





#Making dataframe
lst = optimum_value_list_for_k_value

# Calling DataFrame constructor on list
# with indices and columns specified



optimum_value_vs_for_k2_value_dataframe = pd.DataFrame(optimum_value_list_for_k_value, index = K2_value_test_range,
                  columns= ['optimum_value'])

print(optimum_value_vs_for_k2_value_dataframe)




optimum_value_vs_for_k2_value_dataframe.to_excel('optimum_value_vs_for_k2_value_dataframe.xlsx')