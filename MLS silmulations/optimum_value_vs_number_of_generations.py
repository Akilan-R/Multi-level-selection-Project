import numpy as np
from evaluating_optimum_value import find_optimum_c_value_class
from parameters_class_file import parameters_class
import matplotlib.pyplot as plt
import time as time
import pandas as pd

start_time = time.time()


Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
number_of_selfish_traits = 2
Initial_population_size = 1000
Number_of_groups = 100
K1_value = 0.5
K2_value = 2
C_value_dictionary_for_model = {}

number_of_generations_range = np.arange(1, 20, 1)




optimum_value_list_for_given_number_of_generations = []
number_of_generations_list = []

number_of_generations_vs_optimum_value_dictionary = {}
for i in number_of_generations_range:
    print("number of generations for finding optimum", i)
    parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary,
                                                           i,
                                                           K1_value, K2_value)

    find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
    optimum_C_value_for_given_number_of_generations = find_optimum_c_value_object.find_optimum_c_value_method()
    number_of_generations_vs_optimum_value_dictionary[i] = optimum_C_value_for_given_number_of_generations
    optimum_value_list_for_given_number_of_generations.append(optimum_C_value_for_given_number_of_generations)
    number_of_generations_list.append(i)


print(number_of_generations_vs_optimum_value_dictionary)
print( "runtime_of_program", time.time() - start_time)


xpoints = number_of_generations_range
ypoints = np.array(optimum_value_list_for_given_number_of_generations)




df = pd.DataFrame(list(zip(number_of_generations_list,optimum_value_list_for_given_number_of_generations)),
                  columns=['number_of_generations', 'optimum_C_value'])
print(df)
df.to_csv('change_in_optimum_value_with_number_of_generations.csv')
df.to_excel('D:\\Research\\Multi-level selection Project\\Results\\change_in_optimum_value_with_number_of_generations_equal_propotions.xlsx')



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
plt.plot(xpoints,ypoints)
for ij in zip(xpoints,ypoints):
    ax.annotate('(%s, %s)' % ij, xy=ij, textcoords='data') # <--
ax.grid()
plt.show()
plt.savefig("no_of_gens_vs_optimum.jpg")
