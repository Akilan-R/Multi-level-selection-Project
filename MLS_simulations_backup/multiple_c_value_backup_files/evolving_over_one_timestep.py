import time

from making_groups import generate_groups
from population_growth_for_n_groups import population_growth_for_n_groups_class
from Declaring_winner import declaring_winner_and_ending_simulation
from Declaring_winner import ending_simulation
from parameters_class_file import parameters_class


start_time = time.time()

def main():
    number_of_generations = 1

    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5, "C3": 0.4}
    # C_value_dictionary_for_model = {'C1': 0, 'C2': 0}

    Initial_population_size = 1000
@ -22,7 +22,7 @@ def main():
    K1_value = 0.5
    K2_value = 0.5

    C_value_dictionary_for_model = {'C1': 1.699, 'C2': 1.7}
    C_value_dictionary_for_model = {'C1': 1.699, 'C2': 1.7, "C3": 1}



