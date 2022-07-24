import numpy as np
from Evolving_for_one_timestep import run_simulation_class
from parameters_class_file import parameters_class
import time as time


def main():
    start_time = time.time()

    number_of_generations = 1

    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}

    Initial_population_size = 1000

    number_of_selfish_traits = 2
    Number_of_groups = 100
    K2_value = 2
    K1_value = 0.5


    C_value_dictionary_for_model= {}


    parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                           K1_value, K2_value)

    find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
    find_optimum_c_value_object.find_optimum_c_value_method()

    print("time taken for evaluating optimum value", time.time() - start_time)




# class find_optimum_c_value_class:



class find_optimum_c_value_class:
    def __init__(self, parameters_object_for_optimum_value):
        self.parameters_object_for_optimum_value = parameters_object_for_optimum_value



    def find_optimum_c_value_method(self):
        start_time_for_evaluating_optimum = time.time()
        # parameters_object_corresponding_to_

        lower_bound_of_c_value = round(-1 / self.parameters_object_for_optimum_value.K1_value, 1)
        upper_bound_of_c_value = round(1 / self.parameters_object_for_optimum_value.K2_value, 1)
        least_count_of_c_values = 0.05
        C_value_range = np.arange(lower_bound_of_c_value + least_count_of_c_values, upper_bound_of_c_value, least_count_of_c_values)


        C_value_range = np.around(C_value_range, 2)
        print("C_value_range", C_value_range)
        C_value_test_range = [1.6, 1.7]


        optimum_flag = 0

        for k in C_value_range:
            optimum_flag = 1
            for l in C_value_range:


                C_value_dictionary_for_model = {"C1": k, "C2": l}
                Initial_population_size = self.parameters_object_for_optimum_value.Initial_population_size
                number_of_selfish_traits = self.parameters_object_for_optimum_value.number_of_selfish_traits
                Number_of_groups = self.parameters_object_for_optimum_value.Number_of_groups
                Initial_proportion_of_selfish_traits_dictionary = self.parameters_object_for_optimum_value.Initial_proportion_of_selfish_traits_dictionary
                number_of_generations = self.parameters_object_for_optimum_value.number_of_generations
                K1_value = self.parameters_object_for_optimum_value.K1_value
                K2_value = self.parameters_object_for_optimum_value.K2_value




                modified_parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                               number_of_selfish_traits, Number_of_groups,
                                                               Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                               K1_value, K2_value)



                if k != l:

                    run_simulation_object_1 = run_simulation_class(modified_parameters_object_for_optimum_value)
                    winner = run_simulation_object_1.run_simulation_method()
                    print("in_simulation_with", modified_parameters_object_for_optimum_value.C_value_dictionary, "the_winner_is", winner)

                    if winner != "C1":      #if winner == c2 for optimum flag, no winner is considered as a victory for c1. If winner != "c1" wsas there then none considered as loss
                            optimum_flag = 0
                            break
            if optimum_flag == 1:
                optimum_c1_value = k
                print("the optimum c_value is =", optimum_c1_value)

                return optimum_c1_value


        print("--- %s seconds for evaluating optimum---" % (time.time() - start_time_for_evaluating_optimum))






if __name__ == "__main__":
    main()

