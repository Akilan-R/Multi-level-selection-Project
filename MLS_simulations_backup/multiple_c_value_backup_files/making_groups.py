@ -47,39 +47,39 @@ class generate_groups:
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
        start_time = time.process_time()
        combined_list_of_groups_in_compact_form = []
        for i in range(self.Number_of_groups):
        for i in range(len(self.combined_list_of_groups)):
            number_of_individuals_of_each_trait_in_group_dict = {}

            number_of_occurences_of_trait_c1 = self.combined_list_of_groups[i].count("C1")
            number_of_individuals_of_each_trait_in_group_dict["C1"] = number_of_occurences_of_trait_c1

            number_of_occurences_of_trait_c2 = self.combined_list_of_groups[i].count("C2")
            number_of_individuals_of_each_trait_in_group_dict["C2"] = number_of_occurences_of_trait_c2
            for k in self.proportion_of_selfish_traits_dictionary:
                number_of_occurences_of_trait = self.combined_list_of_groups[i].count(k)
                number_of_individuals_of_each_trait_in_group_dict[k] = number_of_occurences_of_trait

            combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)
        print("combined_list_of_groups_in_compact_form = ", combined_list_of_groups_in_compact_form)
        print("time taken old is", timer() - start_time)
        return combined_list_of_groups_in_compact_form
                                 #use if more than 2 traits are needed in equation

        combined_list_of_groups_in_compact_form_array = np.array(combined_list_of_groups_in_compact_form)
    # def convert_groups_to_compact_form(self):
    #
    #     start_time_2 = time.process_time()
    #     combined_list_of_groups_in_compact_form = []
    #     for i in range(self.Number_of_groups):
    #         number_of_individuals_of_each_trait_in_group_dict = {}
    #
    #         number_of_occurences_of_trait_c1 = self.combined_list_of_groups[i].count("C1")
    #         number_of_individuals_of_each_trait_in_group_dict["C1"] = number_of_occurences_of_trait_c1
    #
    #         number_of_occurences_of_trait_c2 = self.combined_list_of_groups[i].count("C2")
    #         number_of_individuals_of_each_trait_in_group_dict["C2"] = number_of_occurences_of_trait_c2
    #
    #         combined_list_of_groups_in_compact_form.append(number_of_individuals_of_each_trait_in_group_dict)
    #
    #     combined_list_of_groups_in_compact_form_array = np.array(combined_list_of_groups_in_compact_form)


        #testing theory
@ -94,39 +94,39 @@ class generate_groups:
        # print("combined_list_of_groups_in_compact_form = ", combined_list_of_groups_in_compact_form)
        # print("time taken new is",timer() - start_time_2)
        # print("combined_list_of_groups_in_compact_form_array",combined_list_of_groups_in_compact_form_array)
        return combined_list_of_groups_in_compact_form_array
        # return combined_list_of_groups_in_compact_form_array

# proportion_of_selfish_traits_dictionary = {"C1": 0.6, "C2": 0.4}
proportion_of_selfish_traits_dictionary = {"C1": 0.4, "C2": 0.4, "C3": 0.2}


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
number_of_generations = 1

Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5, "C3": 0.5}
# C_value_dictionary_for_model = {'C1': 0, 'C2': 0}

Initial_population_size = 1000

number_of_selfish_traits = 2
Number_of_groups = 100
K1_value = 0.5
K2_value = 0.5

# parameters_object_for_making_groups = parameters_class(C_value_dictionary_for_model, Initial_population_size,
#                                      number_of_selfish_traits, Number_of_groups,
#                                      Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
#                                      K1_value, K2_value)
#
C_value_dictionary_for_model = {'C1': 0, 'C2': 1}




parameters_object_for_making_groups = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                     number_of_selfish_traits, Number_of_groups,
                                     Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                     K1_value, K2_value)
#
# g1 = generate_groups(parameters_object_for_making_groups, Initial_proportion_of_selfish_traits_dictionary)
# g1.print_input_paramaters()
# g1.generate_list_of_individuals()
# g1.generate_group()
# g1.convert_groups_to_compact_form()

g1 = generate_groups(parameters_object_for_making_groups, Initial_proportion_of_selfish_traits_dictionary)
g1.print_input_paramaters()
g1.generate_list_of_individuals()
g1.generate_group()
g1.convert_groups_to_compact_form()
#


