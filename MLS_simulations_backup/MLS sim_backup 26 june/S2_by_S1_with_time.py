from making_groups import generate_groups
from population_growth_for_n_groups import population_growth_for_n_groups_class
from Declaring_winner import declaring_winner
from Declaring_winner import ending_simulation
from parameters_class_file import parameters_class
import matplotlib.pyplot as plt
import numpy as np


def main():
    number_of_generations = 1

    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
    # C_value_dictionary_for_model = {'C1': 0, 'C2': 0}

    Initial_population_size = 1000

    number_of_selfish_traits = 2
    Number_of_groups = 100
    K1_value = 0.5
    K2_value = 0.5

    C_value_dictionary_for_model = {'C1': 0, 'C2': 1}

    parameters_object_for_run_simulation = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                            number_of_selfish_traits, Number_of_groups,
                                                            Initial_proportion_of_selfish_traits_dictionary,
                                                            number_of_generations,
                                                            K1_value, K2_value)

    run_simulation_object = run_simulation_class(parameters_object_for_run_simulation)
    run_simulation_object.run_simulation_method()
    run_simulation_object.plot_S2_by_S1_list()


class run_simulation_class:
    def __init__(self, parameters_object_for_run_simulation):
        self.parameters_object_for_run_simulation = parameters_object_for_run_simulation
        self.number_of_time_steps = 0
        self.S2_by_S1_list = []

    def run_simulation_method(self):


        time_step_number = 0
        new_proportion_of_selfish_traits_dictionary = self.parameters_object_for_run_simulation.Initial_proportion_of_selfish_traits_dictionary
        while (True):
            time_step_number = time_step_number + 1
            # print("------------------------------------------")
            # print("time_step_number =",time_step_number)
            S2_by_S1_value = new_proportion_of_selfish_traits_dictionary["C2"] /new_proportion_of_selfish_traits_dictionary["C1"]
            print("S2_by_S1_value", S2_by_S1_value)

            self.S2_by_S1_list.append(S2_by_S1_value)

            generating_groups_instance = generate_groups(self.parameters_object_for_run_simulation,
                                                         new_proportion_of_selfish_traits_dictionary)
            generating_groups_instance.generate_list_of_individuals()
            generating_groups_instance.generate_group()
            list_of_groups_for_calculating_population_growth_over_time = generating_groups_instance.convert_groups_to_compact_form()
            # print("list_of_groups_at", time_step_number, " =", list_of_groups_for_calculating_population_growth_over_time)

            # population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time(initial_groups_test_value)

            population_growth_for_n_groups_instance = population_growth_for_n_groups_class(
                self.parameters_object_for_run_simulation, list_of_groups_for_calculating_population_growth_over_time)

            new_proportion_of_selfish_traits_dictionary = population_growth_for_n_groups_instance.population_growth_pooling_and_normalising()

            # print("new_proportion_of_selfish_traits_dictionary", "at time step_number", time_step_number,"=", new_proportion_of_selfish_traits_dictionary)

            if ending_simulation(new_proportion_of_selfish_traits_dictionary, time_step_number) == 1:
                winner = declaring_winner(new_proportion_of_selfish_traits_dictionary, time_step_number)
                self.number_of_time_steps = time_step_number


                return winner
                break

    def plot_S2_by_S1_list(self):
        xpoints = np.arange(0, self.number_of_time_steps, 1)
        ypoints = self.S2_by_S1_list

        print(self.S2_by_S1_list)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(0, 1000)
        plt.plot(xpoints, ypoints)
        for ij in zip(xpoints, ypoints):
            ax.annotate('(%s, %s)' % ij, xy=ij, textcoords='data')  # <--
        ax.grid()
        plt.show()

            # parameters.proportion_of_selfish_traits_dictionary = new_proportion_of_selfish_traits_dictionary

    'D:\Research\Multi-level selection Project\MLS silmulations\Evolving_for_one_timestep.py'


#
if __name__ == "__main__":
    main()