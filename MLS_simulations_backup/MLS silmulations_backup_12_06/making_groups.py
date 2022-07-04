import numpy as np
import random
random.seed(1)


class generate_groups:

    def __init__(self, Initial_population_size, number_of_selfish_traits, Number_of_groups, proportion_of_selfish_traits_list):

        self.Initial_population_size = Initial_population_size
        self.number_of_selfish_traits = number_of_selfish_traits
        self.Number_of_groups = Number_of_groups
        self.combined_list_of_individuals = []
        self.size_of_each_group = 0
        self.proportion_of_selfish_traits_list = proportion_of_selfish_traits_list
    def print_input_paramaters(self):
        print("Initial_population_size = " + str(self.Initial_population_size))
        print("number_of_selfish_traits = " + str(self.number_of_selfish_traits))
        print("Number_of_groups = " + str(self.Number_of_groups))
        # print("S1__proportion_of_individuals_with_trait_C1 = " + str(self.S1__proportion_of_individuals_with_trait_C1))
        print("proportion_of_selfish_traits_list = " + str(self.proportion_of_selfish_traits_list))


    def generate_selfishness(self):
        self.size_of_each_group = int(self.Initial_population_size / self.Number_of_groups)
        List_of_traits = []
        for i in range(len(self.proportion_of_selfish_traits_list)):
            List_of_traits.append("C"+ str(i + 1))
        lst = []
        for i in self.proportion_of_selfish_traits_list:
            Number_of_individuals_with_trait = int(i * self.Initial_population_size)

            lst.append(i * Number_of_individuals_with_trait)


            # make list containing of n1, with c1
        # make list containing of n - n1 with c2

        # list_of_individuals_with_C1 = ["C1"] * Number_of_individuals_with_trait_C1
        # list_of_individuals_with_C2 = ["C2"] * Number_of_individuals_with_trait_C2

        self.combined_list_of_individuals = lst
        print("combined_list_of_individuals", self.combined_list_of_individuals)

    # Randomosing combined list
    def generate_group(self):
        random.shuffle(self.combined_list_of_individuals)

        combined_list_of_groups = [self.combined_list_of_individuals[i * self.size_of_each_group:(i + 1) * self.size_of_each_group] for
                                   i in range(
                (len(self.combined_list_of_individuals) + self.size_of_each_group - 1) // self.size_of_each_group)]

        print("combined_list_of_groups", combined_list_of_groups)

    def generate_selfishness_1(self):
        self.size_of_each_group = int(self.Initial_population_size / self.Number_of_groups)

        S2__proportion_of_individuals_with_trait_C2 = 1 - self.S1__proportion_of_individuals_with_trait_C1
        Number_of_individuals_with_trait_C1 = int(
            self.S1__proportion_of_individuals_with_trait_C1 * self.Initial_population_size)
        Number_of_individuals_with_trait_C2 = self.Initial_population_size - Number_of_individuals_with_trait_C1


proportion_of_selfish_traits_list = [0.1, 0.9]
g1 = generate_groups(100,2, 50, proportion_of_selfish_traits_list)
g1.print_input_paramaters()
g1.generate_selfishness()
g1.generate_group()
#
#
#
#
# Initial_population_size = 100
# Number_of_groups = 10
#
# C1__ =  0
# C2__ =  0
# K1__ =  0
# K2__ =  0
#
# def generate_selfishness(Initial_population_size, number_of_selfish_traits):   #number_of_selfish_traits = C1, C2, C3 etc
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
#     list_of_individuals_with_C1 = ["C1"]*Number_of_individuals_with_trait_C1
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
