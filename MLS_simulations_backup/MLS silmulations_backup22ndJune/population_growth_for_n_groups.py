import population_growth_2
from parameters import *

population_growth_for_group_instance = population_growth_2.population_growth_for_group_class()
# population_growth_for_group_instance.finding_population_dictionaries_over_time({'C1': 100, 'C2': 100})

class population_growth_for_n_groups_class:
        def __init__(self, initial_list_of_groups_for_calulating_population_growth_over_time):
            self.initial_list_of_groups_for_calulating_population_growth_over_time = initial_list_of_groups_for_calulating_population_growth_over_time
            self.list_of_groups_after_n_generations = []
            self.proportion_of_selfish_traits_dictionary_after_pooling = {}
            self.population_dictionary_after_pooling = {}
            self.proportion_of_selfish_traits_dictionary_after_pooling = {}


        def population_growth_of_n_groups_over_time(self):

            for group_number in range(len(self.initial_list_of_groups_for_calulating_population_growth_over_time)):
                population_growth_for_group_instance.finding_population_dictionaries_over_time(self.initial_list_of_groups_for_calulating_population_growth_over_time[group_number])

                group_dictionary_after_n_generations = population_growth_for_group_instance.finding_population_dictionary_at_the_end_of_n_generations()
                self.list_of_groups_after_n_generations.append(group_dictionary_after_n_generations)
                # print("---n_groups_simulation--")
            # print("list_of_groups_after_selection = ", self.list_of_groups_after_n_generations)


        def find_pooled_groups_dictionary(self):


             for trait in C_value_dictionary_for_model:

                sum_of_individuals_with_trait = 0
                for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
                    number_of_individuals_with_trait =  group_in_group_list_to_be_pooled[trait]
                    sum_of_individuals_with_trait += number_of_individuals_with_trait



                self.population_dictionary_after_pooling[trait] = sum_of_individuals_with_trait
             print(self.population_dictionary_after_pooling)


        def finding_normalised_group_dictionary_afer_pooling(self):
            total_number_of_individuals = sum( self.population_dictionary_after_pooling.values())

            for trait_of_pooled_group_dictionary in  self.population_dictionary_after_pooling:
                number_of_individuals_of_trait_in_pooled_group_dictionary =  self.population_dictionary_after_pooling[trait_of_pooled_group_dictionary]
                proportion_of_individuals_of_trait_in_pooled_group_dictionary = number_of_individuals_of_trait_in_pooled_group_dictionary/total_number_of_individuals
                self.proportion_of_selfish_traits_dictionary_after_pooling[trait_of_pooled_group_dictionary] = proportion_of_individuals_of_trait_in_pooled_group_dictionary
            # print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)

        def population_growth_pooling_and_normalising(self):


                self.population_growth_of_n_groups_over_time()
                self.find_pooled_groups_dictionary()
                self.finding_normalised_group_dictionary_afer_pooling()
                return self.proportion_of_selfish_traits_dictionary_after_pooling




# initial_groups_test_value = [{'C1': 57, 'C2': 43}, {'C1': 48, 'C2': 52}, {'C1': 49, 'C2': 51},
#                                      {'C1': 52, 'C2': 48}, {'C1': 58, 'C2': 42}, {'C1': 37, 'C2': 63},
#                                      {'C1': 56, 'C2': 44}, {'C1': 44, 'C2': 56}, {'C1': 47, 'C2': 53},
#                                       {'C1': 52, 'C2': 48}]
#
#
# population_growth_for_n_groups_instance = population_growth_for_n_groups_class(initial_groups_test_value)
# population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time()
# def reporting_the_winner():
#     if trait in





