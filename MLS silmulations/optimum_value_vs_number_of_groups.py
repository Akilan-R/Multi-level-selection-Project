#fixed group size

import numpy as np
from evaluating_optimum_value import find_optimum_c_value_class
from parameters_class_file import parameters_class
import matplotlib.pyplot as plt
import time as time

start_time = time.time()


number_of_generations = 1
Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}
number_of_selfish_traits = 2
K1_value = 0.5
K2_value = 0.5
C_value_dictionary_for_model = {}




# Initial_population_size_range = np.arange(500, 10000, 500)
# Number_of_groups_range = np.arange(100, 1000, 100)
Number_of_groups_test_range = [1, 50, 100, 150, 200]



print(Number_of_groups_test_range)
optimum_vs_no_of_groups_vs_initial_pop_size_list = []
optimum_C_value_for_given_number_of_groups_list = []

for Number_of_groups in Number_of_groups_test_range:
    Initial_population_size = 25*Number_of_groups





    parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary,
                                                           number_of_generations,
                                                           K1_value, K2_value)

    find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
    optimum_C_value = find_optimum_c_value_object.find_optimum_c_value_method()

    optimum_vs_no_of_groups_vs_initial_pop_size = ("Optimum =", optimum_C_value,  "// number_of_groups =", Number_of_groups, "//Initial popuation size =", Initial_population_size)
    optimum_vs_no_of_groups_vs_initial_pop_size_list.append(optimum_vs_no_of_groups_vs_initial_pop_size)

    optimum_C_value_for_given_number_of_groups_list.append(optimum_C_value)
    optimum_vs_no_of_groups_vs_initial_pop_size_list.append(optimum_vs_no_of_groups_vs_initial_pop_size)


print("optimum_vs_no_of_groups_vs_initial_pop_size_list", optimum_vs_no_of_groups_vs_initial_pop_size_list)
print( "runtime_of_program", time.time() - start_time)


xpoints = Number_of_groups_test_range
ypoints = np.array(optimum_C_value_for_given_number_of_groups_list)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
plt.plot(xpoints,ypoints)
for ij in zip(xpoints,ypoints):
    ax.annotate('(%s, %s)' % ij, xy=ij, textcoords='data') # <--
ax.grid()
plt.show()
plt.savefig("optimum_val_vs_number_of_groups.jpg")

