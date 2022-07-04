from absolute_fitness_equations_classes_2 import *
from parameters import *


print("-----pop_growth_2---")

class population_growth_for_group_class():
    def __init__(self):
        # self.initial_group_dictionary = initial_group_dictionary
        self.group_dictionaries_over_time_list = []

        # self.group_dictionary_at_given_generation = {}
        # self.trait = trait
        # self.group_dictionary_at_next_generation = {}
    def find_group_dictionary_at_next_generation(self, group_dictionary_at_given_generation):
        group_dictionary_at_next_generation = {}
        for k in C_value_dictionary_for_model:

            C_value = C_value_dictionary_for_model[k]

            realised_fitness_of_of_given_trait_in_given_group_at_given_generation =  find_realised_fitness_function(C_value, k_value_for_model.K1_value, C_value_dictionary_for_model, group_dictionary_at_given_generation,
                                                                                                           k_value_for_model.K2_value)


            number_of_individuals_of_given_trait_in_given_group_at_given_generation = group_dictionary_at_given_generation[k]


            number_of_individuals_of_given_trait_in_given_group_at_next_generation = number_of_individuals_of_given_trait_in_given_group_at_given_generation*realised_fitness_of_of_given_trait_in_given_group_at_given_generation
            if number_of_individuals_of_given_trait_in_given_group_at_next_generation < 0.05:

                number_of_individuals_of_given_trait_in_given_group_at_next_generation = 0


            group_dictionary_at_next_generation[k] = number_of_individuals_of_given_trait_in_given_group_at_next_generation
            # print(self.group_dictionary_at_next_generation[k])
            # print(self.group_dictionary_at_next_generation)
            # return self.group_dictionary_at_next_generation

        return group_dictionary_at_next_generation


    def finding_population_dictionaries_over_time(self, group_dictionary_at_beginning_of_cycle):
        # group_dictionary_at_given_generation = group_dictionary_at_beginning_of_cycle
        # self.group_dictionary_at_given_generation = self.group_dictionary_at_given_generation
        group_dictionary_at_given_generation_in_pop_dict_over_time = group_dictionary_at_beginning_of_cycle
        self.group_dictionaries_over_time_list = [group_dictionary_at_beginning_of_cycle]


        for t in range(number_of_generations):
            # print("group_dictionary_at_generation " + str(t), group_dictionary_at_next_generation2)
            # print("-----" + "generation" + str(t + 1) + "------------")

            group_dictionary_at_next_generation_in_pop_dict_over_time = self.find_group_dictionary_at_next_generation(group_dictionary_at_given_generation_in_pop_dict_over_time)
            # print("group_dictionary_at_generation " + str(t), group_dictionary_at_next_generation_in_pop_dict_over_time)

            self.group_dictionaries_over_time_list.append(group_dictionary_at_next_generation_in_pop_dict_over_time)
            # print("group_dictionaries_over_time_list_temp = ", self.group_dictionaries_over_time_list)

            group_dictionary_at_given_generation_in_pop_dict_over_time = group_dictionary_at_next_generation_in_pop_dict_over_time

        # print("group_dictionaries_over_time_list = ", self.group_dictionaries_over_time_list)


        return self.group_dictionaries_over_time_list

    def finding_population_dictionary_at_the_end_of_n_generations(self):
        group_dictionaries_at_the_end_of_n_generations = self.group_dictionaries_over_time_list[-1]
        # print("group_dictionaries_at_the_end_of_n_generations = ", group_dictionaries_at_the_end_of_n_generations)
        return group_dictionaries_at_the_end_of_n_generations

initial_group_dictionary = {'C1': 100, 'C2': 100}
test_trait = 'C1'
test_population_growth_class = population_growth_for_group_class()
test_population_growth_class.find_group_dictionary_at_next_generation(initial_group_dictionary)
test_population_growth_class.finding_population_dictionaries_over_time(initial_group_dictionary)
test_population_growth_class.finding_population_dictionary_at_the_end_of_n_generations()