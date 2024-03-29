import numpy as np
from evaluating_optimum_value import find_optimum_c_value_class
from parameters_class_file import parameters_class
import matplotlib.pyplot as plt
import time as time
import pandas as pd

start_time = time.time()




number_of_generations = 1
Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}
number_of_selfish_traits = 2
Number_of_groups = 100
K1_value = 0.5
# K2_value = 0.5
C_value_dictionary_for_model = {}

Initial_population_size_range = np.arange(500, 10000, 250)
K2_value_range = np.arange(0.5, 10, 0.25)


optimum_C_value_for_given_parameters_list = []
K2_value_list_for_calculating_optimum = []
Initial_population_list_for_calculating_optimum = []

for Initial_population_size in Initial_population_size_range:
    for K2_value in K2_value_range:

        print("Initial_population_size_range for finding optimum", K2_value_range)
        parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                               number_of_selfish_traits, Number_of_groups,
                                                               Initial_proportion_of_selfish_traits_dictionary,
                                                               number_of_generations,
                                                               K1_value, K2_value)

        find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
        optimum_C_value_for_given_parameters = find_optimum_c_value_object.find_optimum_c_value_method()

        optimum_C_value_for_given_parameters_list.append(optimum_C_value_for_given_parameters)
        K2_value_list_for_calculating_optimum.append(K2_value)
        Initial_population_list_for_calculating_optimum.append(Initial_population_size)




print(optimum_C_value_for_given_parameters_list)
print( "runtime_of_program", time.time() - start_time)


#look at how to crear
# list of int

# Calling DataFrame constructor after zipping
# both lists, with columns specified
df = pd.DataFrame(list(zip(K2_value_list_for_calculating_optimum,Initial_population_list_for_calculating_optimum,optimum_C_value_for_given_parameters_list)),
                  columns=['K2_value', 'Initial_population_list','optimum_C_value'])
print(df)


#     xpoints = Initial_population_size_range
#     ypoints = np.array(optimum_value_list_for_k_value)
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_ylim(0,10)
# plt.plot(xpoints,ypoints)
# for ij in zip(xpoints,ypoints):
#     ax.annotate('(%s, %s)' % ij, xy=ij, textcoords='data') # <--
# ax.grid()
# plt.show()
# plt.savefig("pop_size_vs_optimum.jpg")
#

df.to_csv('change_in_optimum_value_with_different_values_of_k.csv')