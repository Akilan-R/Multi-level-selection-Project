import numpy as np
import Evolving_for_one_timestep
from parameters_class_file import parameters_class




def main():
    k1_value_range = np.arange(0, 0.5, 0.1)

    number_of_generations = 1

    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
    C_value_dictionary_for_model = {'C1': -0.1, 'C2': 0.3}

    Initial_population_size = 10000

    number_of_selfish_traits = 2
    Number_of_groups = 100
    K2_value = 2

    winner_list = []
    for K1_value in k1_value_range:
        parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                             number_of_selfish_traits, Number_of_groups,
                                             Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                             K1_value, K2_value)

        parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                         number_of_selfish_traits, Number_of_groups,
                                         Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                         K1_value, K2_value)

        winner = Evolving_for_one_timestep.run_simulation(parameters_object)


        winner_list.append(winner)
    print(winner_list)


if __name__ == "__main__":
    main()