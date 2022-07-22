import numpy as np
import random
# random.seed(1)
from timeit import default_timer as timer
from parameters_class_file import parameters_class
from collections import Counter
import math


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





number_of_generations = 1
Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}
number_of_selfish_traits = 2
Number_of_groups = 100
Initial_population_size = 1000
K1_value = 0.5
K2_value = 4
C_value_dictionary_for_model = {}

Initial_population_size_range = np.arange(500, 10000, 250)
K2_value_range = np.arange(0.5, 10, 0.25)

parameters_object_for_making_groups = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                     number_of_selfish_traits, Number_of_groups,
                                     Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                     K1_value, K2_value)
summation_n2_square_list = []
for k in range(5000):
    g1 = generate_groups(parameters_object_for_making_groups, Initial_proportion_of_selfish_traits_dictionary)
    g1.print_input_paramaters()
    g1.generate_list_of_individuals()
    g1.generate_group()
    groups_in_compact_form = g1.convert_groups_to_compact_form()


    # def calculate_summation_n_and_n2(self):
    summation_n1_n2 = 0
    summation_n1_square = 0
    # print(groups_in_compact_form)
    for group in groups_in_compact_form:
        number_of_individuals_with_trait_c1_in_group = group["C1"]
        number_of_individuals_with_trait_c1_in_group_square = number_of_individuals_with_trait_c1_in_group ** 2
        summation_n1_square += number_of_individuals_with_trait_c1_in_group_square

    summation_n2_square = 0
    for group in groups_in_compact_form:
        number_of_individuals_with_trait_c1_in_group = group["C2"]
        number_of_individuals_with_trait_c1_in_group_square = number_of_individuals_with_trait_c1_in_group ** 2
        summation_n2_square += number_of_individuals_with_trait_c1_in_group_square

    summation_n2_square_list.append(summation_n2_square)


    summation_of_prod_n1_n2 = 0
    for group in groups_in_compact_form:
        number_of_individuals_with_trait_c1_in_group = group["C1"]
        number_of_individuals_with_trait_c2_in_group = group["C2"]
        product_of_n1_n2 = number_of_individuals_with_trait_c1_in_group * number_of_individuals_with_trait_c2_in_group
        summation_of_prod_n1_n2 += product_of_n1_n2

    # print(summation_of_prod_n1_n2)

    total_number_of_individuals_with_C1 = Initial_proportion_of_selfish_traits_dictionary["C1"]*Initial_population_size
    # sum_of_squares_of_number_of_individuals_with_trait_C1 =
    # summation_n1_square =
    # summation_n1_m_n1 =
    #
    # for C2_value in [-0.3, -0.2, 0, 0.1, 0.2]:
    #
    #
    #     theoretical_optimum = (((K1_value*Initial_population_size*total_number_of_individuals_with_C1)/Number_of_groups) - (K2_value*summation_n1_square) - (summation_of_prod_n1_n2*K2_value*C2_value))/(2*K1_value*K2_value*summation_n1_square)
    #
    #     print(theoretical_optimum)

    # print("summation_n2_square", summation_n2_square)

    A_term = -K1_value*K2_value
    B_term = - summation_n1_square*K2_value + summation_of_prod_n1_n2*K2_value + K1_value*summation_n1_square + K1_value*summation_of_prod_n1_n2
    C_term = summation_n1_square - 99*(-summation_n2_square - summation_of_prod_n1_n2 - (K1_value/K2_value)*summation_n2_square + K1_value/K2_value - (K1_value/K2_value)*summation_of_prod_n1_n2)

    lower_bound = (-B_term + (B_term**2 - 4*A_term*C_term)**0.5)/(2*A_term)
    upper_bound = (-B_term - ((B_term**2 - 4*A_term*C_term)**0.5))/(2*A_term)
    #
    # print("lower_bound",lower_bound)
    # print("upper_bound",upper_bound)


    C_value_variable = upper_bound
    substituted_value = A_term*((C_value_variable)**2) + B_term*(C_value_variable) + C_term
    print(substituted_value)

# print(summation_n2_square_list)
print("average_list", sum(summation_n2_square_list)/len(summation_n2_square_list))
