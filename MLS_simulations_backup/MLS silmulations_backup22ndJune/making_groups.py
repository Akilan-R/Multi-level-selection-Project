import numpy as np
import random
random.seed(1)
from parameters import *
from collections import Counter



class generate_groups:

    def __init__(self, Initial_population_size_for_generating_groups, number_of_selfish_traits_for_generating_groups, Number_of_groups_for_generating_groups, proportion_of_selfish_traits_dictionary):

        self.Initial_population_size = Initial_population_size
        self.number_of_selfish_traits = number_of_selfish_traits
        self.Number_of_groups = Number_of_groups
        self.combined_list_of_individuals = []
        self.size_of_each_group = 0
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
            for i in range(number_of_individuals):
                self.combined_list_of_individuals.append(k)

    # def generate_list_of_individuals1(self):
    #     self.size_of_each_group = int(self.Initial_population_size / self.Number_of_groups)
    #     self.combined_list_of_individuals = []
    #     for i in range(len(self.proportion_of_selfish_traits_dictionary)):
    #         List_of_traits.append("C_value"+ str(i + 1))
    #     lst = []
    #     for i in self.proportion_of_selfish_traits_dictionary:
    #         Number_of_individuals_with_trait = int(i * self.Initial_population_size)
    #
    #         lst.append(i * Number_of_individuals_with_trait)


            # make list containing of n1, with c1
        # make list containing of n - n1 with c2

        # list_of_individuals_with_C1 = ["C_value"] * Number_of_individuals_with_trait_C1
        # list_of_individuals_with_C2 = ["C2"] * Number_of_individuals_with_trait_C2

        # self.combined_list_of_individuals = lst
        # print("combined_list_of_individuals", self.combined_list_of_individuals)

    # Randomosing combined list
    def generate_group(self):
        random.shuffle(self.combined_list_of_individuals)
        self.size_of_each_group = int(self.Initial_population_size / self.Number_of_groups)

        self.combined_list_of_groups = [self.combined_list_of_individuals[i * self.size_of_each_group:(i + 1) * self.size_of_each_group] for
                                   i in range((len(self.combined_list_of_individuals) + self.size_of_each_group - 1) // self.size_of_each_group)]

        # print("combined_list_of_groups", self.combined_list_of_groups)


    def convert_groups_to_compact_form(self):
        combined_list_of_groups_in_compact_form = []
        for i in range(len(self.combined_list_of_groups)):
            number_of_individuals_of_each_trait_in_group_dict = {}

            for k in self.proportion_of_selfish_traits_dictionary:
                number_of_occurences_of_trait = self.combined_list_of_groups[i].count(k)
                number_of_individuals_of_each_trait_in_group_dict[k] = number_of_occurences_of_trait

            combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)
        # print("combined_list_of_groups_in_compact_form = ", combined_list_of_groups_in_compact_form)
        return combined_list_of_groups_in_compact_form


# proportion_of_selfish_traits_dictionary = {"C1": 0.6, "C2": 0.4}

g1 = generate_groups(Initial_population_size, number_of_selfish_traits, Number_of_groups, Initial_proportion_of_selfish_traits_dictionary)
g1.print_input_paramaters()
g1.generate_list_of_individuals()
g1.generate_group()
g1.convert_groups_to_compact_form()
#
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

def convert_groups_to_compact_form(combined_list_of_groups):
    combined_list_of_groups_in_compact_form = []
    for i in range(len(combined_list_of_groups)):
        number_of_individuals_of_each_trait_in_group_dict = {}
        for k in Initial_proportion_of_selfish_traits_dictionary:
            number_of_occurences_of_trait = combined_list_of_groups[i].count(k)
            number_of_individuals_of_each_trait_in_group_dict[k] = number_of_occurences_of_trait

        combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)
        print("combined_list_of_groups_in_compact_form" , combined_list_of_groups_in_compact_form)
    return combined_list_of_groups_in_compact_form








