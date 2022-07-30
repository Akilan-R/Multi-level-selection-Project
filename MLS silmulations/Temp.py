import numpy as np

lower_bound_of_c_value = round(-1 / 0.5, 1)
upper_bound_of_c_value = round(1 / 0.5, 1)
least_count_of_c_values = 0.1

C_value_range = np.arange(lower_bound_of_c_value + least_count_of_c_values, upper_bound_of_c_value,
                          least_count_of_c_values)

C_value_range = np.around(C_value_range, 2)

number_of_selfish_traits = len(C_value_range)

selfish_traits_dictionary = {}

for i in range(number_of_selfish_traits):
    trait = "C" + str(i + 1)

    selfish_traits_dictionary[trait] = C_value_range[i]


print(selfish_traits_dictionary)

