import numpy as np
from evaluating_optimum_value import find_optimum_c_value_class
from parameters_class_file import parameters_class
import matplotlib.pyplot as plt
import time as time

start_time = time.time()


number_of_generations = 1
Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}
number_of_selfish_traits = 2
Number_of_groups = 100
K1_value = 0.5
K2_value = 0.5
C_value_dictionary_for_model = {}

Initial_population_size_range = np.arange(500, 10000, 500)




optimum_value_list_for_k_value = []

K2_vs_optimum_value_dictionary = {}
for i in Initial_population_size_range:
    print("Initial_population_size_range for finding optimum", i)
    parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, i,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary,
                                                           number_of_generations,
                                                           K1_value, K2_value)

    find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
    optimum_C_value_for_given_k_value = find_optimum_c_value_object.find_optimum_c_value_method()
    K2_vs_optimum_value_dictionary[i] = optimum_C_value_for_given_k_value
    optimum_value_list_for_k_value.append(optimum_C_value_for_given_k_value)



print(K2_vs_optimum_value_dictionary)
print( "runtime_of_program", time.time() - start_time)

optimum_value_list_for_k_value

xpoints = Initial_population_size_range
ypoints = np.array(optimum_value_list_for_k_value)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
plt.plot(xpoints,ypoints)
for ij in zip(xpoints,ypoints):
    ax.annotate('(%s, %s)' % ij, xy=ij, textcoords='data') # <--
ax.grid()
plt.show()
plt.savefig("pop_size_vs_optimum.jpg")

