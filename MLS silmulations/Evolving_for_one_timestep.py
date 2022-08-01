import time
import numpy as np

from making_groups import generate_groups
from population_growth_for_n_groups import population_growth_for_n_groups_class
from Declaring_winner import declaring_winner_and_ending_simulation
from Declaring_winner import ending_simulation
from parameters_class_file import parameters_class


start_time = time.time()

def main():
    number_of_generations = 1

    # Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.333, "C2": 0.333, "C3": 0.334}
    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.3, "C2": 0.7}

    # C_value_dictionary_for_model = {'C1': 0, 'C2': 0}

    Initial_population_size = 1000

    number_of_selfish_traits = 2
    Number_of_groups = 100
    K1_value = 0.5
    K2_value = 2

    # C_value_dictionary_for_model = {'C1': -0.1, 'C2': 0, "C3": -0.2}
    C_value_dictionary_for_model = {'C1': 1.6, 'C2': 1.7}



    parameters_object_for_run_simulation = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                         number_of_selfish_traits, Number_of_groups,
                                         Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                         K1_value, K2_value)

    run_simulation_object = run_simulation_class(parameters_object_for_run_simulation)
    # run_simulation_object.run_simulation_method()

    print(run_simulation_object.round_off_proportion_dictionary({'C1': 0.005319154592636088, 'C2': 0.010636021838543213, 'C3': 0.015952196861098163, 'C4': 0.021208198613125503, 'C5': 0.026495902188238413, 'C6': 0.0317935175991768, 'C7': 0.03696476713556272, 'C8': 0.04241431052397196, 'C9': 0.04761858613681283, 'C10': 0.05283269332769925, 'C11': 0.05785508474669792, 'C12': 0.06332411071119327, 'C13': 0.0681878224669817, 'C14': 0.07354245099836162, 'C15': 0.07865342694199497, 'C16': 0.08389153120909046, 'C17': 0.0886326592382072, 'C18': 0.0941101724629337, 'C19': 0.10056739240767419}))

class run_simulation_class:
    def __init__(self, parameters_object_for_run_simulation):
        self.parameters_object_for_run_simulation = parameters_object_for_run_simulation

    def round_off_proportion_dictionary(self, dictionary_to_round_off):
        rounded_off_dictionary = {}
        for i in dictionary_to_round_off:
            rounded_off_dictionary[i] = round(dictionary_to_round_off[i], 4)
        return rounded_off_dictionary

    def run_simulation_method(self):
        S2_by_S1_list = []

        time_step_number = 0
        new_proportion_of_selfish_traits_dictionary = self.parameters_object_for_run_simulation.Initial_proportion_of_selfish_traits_dictionary
        while (True):
            time_step_number = time_step_number + 1
            # print("------------------------------------------")
            # print("time_step_number =",time_step_number)

            generating_groups_instance = generate_groups(self.parameters_object_for_run_simulation,
                                                         new_proportion_of_selfish_traits_dictionary)
            generating_groups_instance.generate_list_of_individuals()
            generating_groups_instance.generate_group()
            list_of_groups_for_calculating_population_growth_over_time = generating_groups_instance.convert_groups_to_compact_form()
            # print("list_of_groups_at", time_step_number, " =", list_of_groups_for_calculating_population_growth_over_time)

            # population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time(initial_groups_test_value)

            population_growth_for_n_groups_instance = population_growth_for_n_groups_class(
                self.parameters_object_for_run_simulation,
                list_of_groups_for_calculating_population_growth_over_time)
            list_of_groups_after_one_time_step = population_growth_for_n_groups_instance.find_list_of_groups_over_generations()
            pooled_group_dictionary_after_one_time_step = population_growth_for_n_groups_instance.find_pooled_group_dictionary(
                list_of_groups_after_one_time_step)
            new_proportion_of_selfish_traits_dictionary = population_growth_for_n_groups_instance.finding_normalised_group_dictionary_afer_pooling(
                pooled_group_dictionary_after_one_time_step)

            rounded_off_new_proportion_of_selfish_traits_dictionary = self.round_off_proportion_dictionary(
                new_proportion_of_selfish_traits_dictionary)

            print("new_proportion_of_selfish_traits_dictionary", "at time step_number", time_step_number, "=",
                  rounded_off_new_proportion_of_selfish_traits_dictionary)

            if declaring_winner_and_ending_simulation(new_proportion_of_selfish_traits_dictionary,
                                                      time_step_number) != "X":
                winner = declaring_winner_and_ending_simulation(new_proportion_of_selfish_traits_dictionary,
                                                                time_step_number)
                # print("number_of_time_steps = ", time_step_number)
                print("in simulation with", self.parameters_object_for_run_simulation.C_value_dictionary,
                      "the winner is", winner)

                # print("time taken for evolving over one timestep simulation", time.time() - start_time)
                return winner
                break

                # parameters.proportion_of_selfish_traits_dictionary = new_proportion_of_selfish_traits_dictionary





    'D:\Research\Multi-level selection Project\MLS silmulations\Evolving_for_one_timestep.py'









#
if __name__ == "__main__":
    main()



