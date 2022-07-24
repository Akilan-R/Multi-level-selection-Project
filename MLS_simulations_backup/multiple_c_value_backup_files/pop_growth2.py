@@ -73,6 +73,7 @@ class population_growth_for_group_class():
        # print("group_dictionaries_over_time_list = ", self.group_dictionaries_over_time_list)

        population_dictionary_at_the_end_of_n_generations = group_dictionary_at_given_generation_in_pop_dict_over_time
        print("group_dictionaries_over_time_list = ", population_dictionary_at_the_end_of_n_generations)

        return population_dictionary_at_the_end_of_n_generations

@ -108,49 +109,32 @@ class population_growth_for_group_class():

#
#
number_of_generations = 1

Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}

Initial_population_size = 1000

number_of_selfish_traits = 2
Number_of_groups = 100
K2_value = 2
K1_value = 2


C_value_dictionary_for_model = {"C1":0.1, "C2":0.4}
#
# number_of_generations = 1
#
parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                           K1_value, K2_value)
# Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.4, "C2": 0.4, "C3":0.2}
#
# Initial_population_size = 1000
#
# number_of_selfish_traits = 2
# Number_of_groups = 100
# K2_value = 2
# K1_value = 2
#
initial_test_group_dictionary = {'C1': 5, 'C2': 0}
initial_group_dictionary = initial_test_group_dictionary

#
# pg = population_growth_for_group_class()
# pg.find_group_dictionary_at_next_generation()

#
#
# initial_group_dictionary = {'C1': 100, 'C2': 100}
# test_trait = 'C1'
test_population_growth_class = population_growth_for_group_class(parameters_object)
test_population_growth_class.find_group_dictionary_at_next_generation(initial_group_dictionary)
test_population_growth_class.finding_population_dictionaries_over_time(initial_group_dictionary)
# # test_population_growth_class.finding_population_dictionary_at_the_end_of_n_generations()

#
# C_value_dictionary_for_model = {"C1":0.1, "C2":0.4, "C3": 0.7}
# #
# #
# parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
#                                                            number_of_selfish_traits, Number_of_groups,
#                                                            Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
#                                                            K1_value, K2_value)
# #
# #
# #
# initial_test_group_dictionary = {'C1': 5, 'C2': 5, 'C3':5}
# initial_group_dictionary = initial_test_group_dictionary
#
# initial_group_dictionary = {'C1': 100, 'C2': 100}
# test_trait = 'C1'
# test_population_growth_class2 = population_growth_for_group_class(parameters_object)
# test_population_growth_class2.find_group_dictionary_at_next_generation(initial_group_dictionary)
# test_population_growth_class2.finding_population_dictionaries_over_time_old(initial_group_dictionary)
# # test_population_growth_class2.finding_population_dictionary_at_the_end_of_n_generations()
# test_population_growth_class = population_growth_for_group_class(parameters_object)
# test_population_growth_class.find_group_dictionary_at_next_generation(initial_group_dictionary)
# test_population_growth_class.finding_population_dictionaries_over_time(initial_group_dictionary)
# # # test_population_growth_class.finding_population_dictionary_at_the_end_of_n_generations()