import numpy as np
import random
# random.seed(1)
from timeit import default_timer as timer
from parameters_class_file import parameters_class
from collections import Counter


import time



class generate_groups:

    def __init__(self, parameters_object , proportion_of_selfish_traits_dictionary):

        # self.parameters_object = parameters_object
        self.Initial_population_size = parameters_object.Initial_population_size
        self.number_of_selfish_traits = parameters_object.number_of_selfish_traits
        self.Number_of_groups = parameters_object.Number_of_groups
        self.combined_list_of_individuals = []
        self.proportion_of_selfish_traits_dictionary = proportion_of_selfish_traits_dictionary
        self.combined_list_of_groups = []
    def print_input_paramaters(self):
        print("Initial_population_size = " + str(self.Initial_population_size))
        print("number_of_selfish_traits = " + str(self.number_of_selfish_traits))
        print("Number_of_groups = " + str(self.Number_of_groups))
        # print("S1__proportion_of_individuals_with_trait_C1 = " + str(self.S1__proportion_of_individuals_with_trait_C1))
        print("proportion_of_selfish_traits_dictionary = " + str(self.proportion_of_selfish_traits_dictionary))

    def generate_list_of_individuals(self):
        for k in self.proportion_of_selfish_traits_dictionary:
            number_of_individuals = round(self.proportion_of_selfish_traits_dictionary[k] * self.Initial_population_size)
            # print("number_of_individuals", k, "=",number_of_individuals )
            for i in range(number_of_individuals):
                self.combined_list_of_individuals.append(k)


    # Randomosing combined list
    def generate_group(self):
        random.shuffle(self.combined_list_of_individuals)
        size_of_each_group = int(self.Initial_population_size / self.Number_of_groups)

        self.combined_list_of_groups = [self.combined_list_of_individuals[i * size_of_each_group:(i + 1) * size_of_each_group] for
                                   i in range((len(self.combined_list_of_individuals) + size_of_each_group - 1) // size_of_each_group)]

        # print("combined_list_of_groups", self.combined_list_of_groups)


    # def convert_groups_to_compact_form(self):
    #
    #     start_time = time.process_time()
    #     combined_list_of_groups_in_compact_form = []
    #     for i in range(len(self.combined_list_of_groups)):
    #         number_of_individuals_of_each_trait_in_group_dict = {}
    #
    #         for k in self.proportion_of_selfish_traits_dictionary:
    #             number_of_occurences_of_trait = self.combined_list_of_groups[i].count(k)
    #             number_of_individuals_of_each_trait_in_group_dict[k] = number_of_occurences_of_trait
    #
    #         combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)
    #     # print("combined_list_of_groups_in_compact_form = ", combined_list_of_groups_in_compact_form)
    #     print("time taken old is", timer() - start_time)
    #     return combined_list_of_groups_in_compact_form
                                 #use if more than 2 traits are needed in equation

    def convert_groups_to_compact_form(self):

        start_time_2 = time.process_time()
        combined_list_of_groups_in_compact_form = []
        for i in range(self.Number_of_groups):
            number_of_individuals_of_each_trait_in_group_dict = {}

            number_of_occurences_of_trait_c1 = self.combined_list_of_groups[i].count("C1")
            number_of_individuals_of_each_trait_in_group_dict["C1"] = number_of_occurences_of_trait_c1

            number_of_occurences_of_trait_c2 = self.combined_list_of_groups[i].count("C2")
            number_of_individuals_of_each_trait_in_group_dict["C2"] = number_of_occurences_of_trait_c2

            combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)

        combined_list_of_groups_in_compact_form_array = np.array(combined_list_of_groups_in_compact_form)


        #testing theory








        # print("combined_list_of_groups_in_compact_form = ", combined_list_of_groups_in_compact_form)
        # print("time taken new is",timer() - start_time_2)
        # print("combined_list_of_groups_in_compact_form_array",combined_list_of_groups_in_compact_form_array)
        return combined_list_of_groups_in_compact_form_array

# proportion_of_selfish_traits_dictionary = {"C1": 0.6, "C2": 0.4}


# number_of_generations = 1
#
# Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
# # C_value_dictionary_for_model = {'C1': 0, 'C2': 0}
#
# Initial_population_size = 1000
#
# number_of_selfish_traits = 2
# Number_of_groups = 100
# K1_value = 0.5
# K2_value = 0.5
#
# C_value_dictionary_for_model = {'C1': 0, 'C2': 1}




# parameters_object_for_making_groups = parameters_class(C_value_dictionary_for_model, Initial_population_size,
#                                      number_of_selfish_traits, Number_of_groups,
#                                      Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
#                                      K1_value, K2_value)
#
#
# g1 = generate_groups(parameters_object_for_making_groups, Initial_proportion_of_selfish_traits_dictionary)
# g1.print_input_paramaters()
# g1.generate_list_of_individuals()
# g1.generate_group()
# g1.convert_groups_to_compact_form()
#


# g2 = generate_groups(parameters_object_for_making_groups, Initial_proportion_of_selfish_traits_dictionary)
# g2.print_input_paramaters()
# g2.generate_list_of_individuals()
# g2.generate_group()
# g2.convert_groups_to_compact_form_optimised()

#
#Initial_population_size = 1000


# Initial_population_size = 100
# Number_of_groups = 10
#
# C1__ =  0
# C2__ =  0
# K1__ =  0
# K2__ =  0
#
# def generate_selfishness(Initial_population_size, number_of_selfish_traits):   #number_of_selfish_traits = C_value, C2, C3 etc
#
#     size_of_each_group = int(Initial_population_size / Number_of_groups)
#
#     S1__proportion_of_individuals_with_trait_C1 = 0.5
#
#     S2__proportion_of_individuals_with_trait_C1 = 1 - S1__proportion_of_individuals_with_trait_C1
#     Number_of_individuals_with_trait_C1 = int(S1__proportion_of_individuals_with_trait_C1*Initial_population_size)
#     Number_of_individuals_with_trait_C2 = Initial_population_size - Number_of_individuals_with_trait_C1
#
#
#
#     #make list containing of n1, with c1
#     #make list containing of n - n1 with c2
#
#     list_of_individuals_with_C1 = ["C_value"]*Number_of_individuals_with_trait_C1
#     list_of_individuals_with_C2 = ["C2"]*Number_of_individuals_with_trait_C2
#
#     combined_list_of_individuals = list_of_individuals_with_C1 + list_of_individuals_with_C2
#     print("combined_list_of_individuals", combined_list_of_individuals)
# #Randomosing combined list
#
# random.shuffle(combined_list_of_individuals)
#
#
# #breaking down groups
#
# def randomise_and_split_into_groups(Number_of_groups):
#
#
#     combined_list_of_groups = [combined_list_of_individuals[i * size_of_each_group:(i + 1) * size_of_each_group] for i in range((len(combined_list_of_individuals) + size_of_each_group - 1) // size_of_each_group)]
#
#     print("combined_list_of_groups", combined_list_of_groups)
#
#
# def convert_groups_to_compact_form(combined_list_of_groups):
#     combined_list_of_groups_in_compact_form = []
#     for i in range(len(combined_list_of_groups)):
#         number_of_individuals_of_each_trait_in_group_dict = {}
#         for k in Initial_proportion_of_selfish_traits_dictionary:
#             number_of_occurences_of_trait = combined_list_of_groups[i].count(k)
#             number_of_individuals_of_each_trait_in_group_dict[k] = number_of_occurences_of_trait
#
#         combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)
#         print("combined_list_of_groups_in_compact_form" , combined_list_of_groups_in_compact_form)
#     return combined_list_of_groups_in_compact_form








