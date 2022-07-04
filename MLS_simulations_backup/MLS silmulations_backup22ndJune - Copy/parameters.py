import numpy as np


class k_values:
    def __init__(self, K1_value, K2_value):
        self.K1_value = K1_value
        self.K2_value = K2_value


k_value_for_model = k_values(0.5, 2)
number_of_generations = 1

#
# class C_value_dictionary:
#     def __init__(self, C_value_dictionary):
#         self.C_value_dictionary = C_value_dictionary

# C1_value_for_model_range = [0.3, 0.4]
# C1_value_for_model_index = 0
#
#
#
# C2_value_for_model_range = [0, 0.1]
# C2_value_for_model_index = 0
#
#
# C1_value_for_model_range[i] =


C_value_dictionary_for_model = {'C1' : 0.3, 'C2' : -0.75}

Initial_population_size = 100000

number_of_selfish_traits = 2
Number_of_groups = 1000
Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5,"C2": 0.5}

