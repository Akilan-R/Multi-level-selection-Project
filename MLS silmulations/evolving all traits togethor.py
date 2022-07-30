import time
import numpy as np

from making_groups import generate_groups
from population_growth_for_n_groups import population_growth_for_n_groups_class
from Declaring_winner import declaring_winner_and_ending_simulation
from Declaring_winner import ending_simulation
from parameters_class_file import parameters_class
import numpy as np

start_time = time.time()

def main():
    number_of_generations = 1

    # Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.333, "C2": 0.333, "C3": 0.334}
    # C_value_dictionary_for_model = {'C1': 0, 'C2': 0}

    Initial_population_size = 1000


    lower_bound_of_c_value = round(-1 / 0.5, 1)
    upper_bound_of_c_value = round(1 / 0.5, 1)
    least_count_of_c_values = 0.1

    C_value_range = np.arange(lower_bound_of_c_value + least_count_of_c_values, upper_bound_of_c_value,
                              least_count_of_c_values)

    C_value_range = np.around(C_value_range, 2)
    number_of_selfish_traits = len(C_value_range)


    Number_of_groups = 100
    K1_value = 0.5
    K2_value = 2


    Initial_proportion_of_selfish_traits_dictionary = {}
    C_value_dictionary_for_model = {}

    for i in range(number_of_selfish_traits):

        trait = "C" + str(i + 1)

        C_value_dictionary_for_model[trait] = C_value_range[i]


        if i + 1 < number_of_selfish_traits:
            Initial_proportion_of_selfish_traits_dictionary[trait] = round(1/number_of_selfish_traits, 4)
        if i + 1 == number_of_selfish_traits:
            Initial_proportion_of_selfish_traits_dictionary[trait] = 1 - sum(Initial_proportion_of_selfish_traits_dictionary.values())

    print("C_value_dictionary_for_model", C_value_dictionary_for_model)
    print("Initial_proportion_of_selfish_traits_dictionary", Initial_proportion_of_selfish_traits_dictionary)
    parameters_object_for_run_simulation = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                         number_of_selfish_traits, Number_of_groups,
                                         Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                         K1_value, K2_value)

    run_simulation_object = run_simulation_class(parameters_object_for_run_simulation)
    run_simulation_object.run_simulation_method()


class run_simulation_class:
    def __init__(self, parameters_object_for_run_simulation):
        self.parameters_object_for_run_simulation = parameters_object_for_run_simulation
    def run_simulation_method(self):
            S2_by_S1_list = []

            time_step_number = 0
            new_proportion_of_selfish_traits_dictionary = self.parameters_object_for_run_simulation.Initial_proportion_of_selfish_traits_dictionary
            while(True):
                time_step_number = time_step_number + 1
                # print("------------------------------------------")
                print("--------------------", "time_step_number =",time_step_number)





                generating_groups_instance = generate_groups(self.parameters_object_for_run_simulation, new_proportion_of_selfish_traits_dictionary)
                generating_groups_instance.generate_list_of_individuals()
                generating_groups_instance.generate_group()
                list_of_groups_for_calculating_population_growth_over_time =  generating_groups_instance.convert_groups_to_compact_form()
                # print("list_of_groups_at", time_step_number, " =", list_of_groups_for_calculating_population_growth_over_time)



                # population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time(initial_groups_test_value)


                population_growth_for_n_groups_instance = population_growth_for_n_groups_class(
                    self.parameters_object_for_run_simulation,
                    list_of_groups_for_calculating_population_growth_over_time)
                list_of_groups_after_one_time_step = population_growth_for_n_groups_instance.find_list_of_groups_over_generations()
                pooled_group_dictionary_after_one_time_step = population_growth_for_n_groups_instance.find_pooled_group_dictionary(list_of_groups_after_one_time_step)
                new_proportion_of_selfish_traits_dictionary = population_growth_for_n_groups_instance.finding_normalised_group_dictionary_afer_pooling(pooled_group_dictionary_after_one_time_step)


                if time_step_number > 1000:
                    break

                print("new_proportion_of_selfish_traits_dictionary", "at time step_number", time_step_number,"=", new_proportion_of_selfish_traits_dictionary)

                if declaring_winner_and_ending_simulation(new_proportion_of_selfish_traits_dictionary, time_step_number) != "X":
                    winner = declaring_winner_and_ending_simulation(new_proportion_of_selfish_traits_dictionary, time_step_number)
                    # print("number_of_time_steps = ", time_step_number)
                    # print("in simulation with", self.parameters_object_for_run_simulation.C_value_dictionary, "the winner is", winner)

                    # print("time taken for evolving over one timestep simulation", time.time() - start_time)
                    return winner
                    break


                # parameters.proportion_of_selfish_traits_dictionary = new_proportion_of_selfish_traits_dictionary





    'D:\Research\Multi-level selection Project\MLS silmulations\Evolving_for_one_timestep.py'









#
if __name__ == "__main__":
    main()



