from population_growth_2 import population_growth_for_group_class
from parameters_class_file import parameters_class
import numpy as np
from timeit import default_timer as timer
from numba import njit


# population_growth_for_group_instance.finding_population_dictionaries_over_time({'C1': 100, 'C2': 100})

class population_growth_for_n_groups_class:
        def __init__(self, parameters_object, initial_list_of_groups_for_calculating_population_growth_over_time):
            self.parameters_object = parameters_object

            self.initial_list_of_groups_for_calculating_population_growth_over_time = initial_list_of_groups_for_calculating_population_growth_over_time
            self.list_of_groups_after_n_generations = []
            # self.list_of_groups_after_one_generation = []
            self.population_dictionary_after_pooling = {}
            self.proportion_of_selfish_traits_dictionary_after_pooling = {}





            self.population_growth_for_group_instance = population_growth_for_group_class(parameters_object)


        # def population_growth_of_n_groups_over_time(self):
        #
        #
        #     initial_list_of_groups_for_calculating_population_growth_over_time = self.initial_list_of_groups_for_calculating_population_growth_over_time
        #     initial_list_of_groups_for_calculating_population_growth_over_time_copy = np.copy(initial_list_of_groups_for_calculating_population_growth_over_time)
        #
        #     for group_number in range(len(self.initial_list_of_groups_for_calculating_population_growth_over_time)):
        #
        #         #calculate group dictionary for
        #         initial_list_of_groups_for_calculating_population_growth_over_time_copy[group_number] = self.population_growth_for_group_instance.finding_population_dictionaries_over_time(self.initial_list_of_groups_for_calculating_population_growth_over_time[group_number])
        #
        #
        #
        #         # print("---n_groups_simulation--")
        #     self.list_of_groups_after_n_generations = initial_list_of_groups_for_calculating_population_growth_over_time_copy
        #     # print("list_of_groups_after_selection = ", self.list_of_groups_after_n_generations)
        #
        #
        # def population_growth_of_n_groups_over_time_old(self):
        #
        #     start_time = timer()
        #
        #     for group_number in self.parameters_object.Number_of_groups:
        #
        #         #calculate group dictionary for
        #
        #         group_dictionary_after_n_generations = self.population_growth_for_group_instance.finding_population_dictionaries_over_time(self.initial_list_of_groups_for_calculating_population_growth_over_time[group_number])
        #         self.list_of_groups_after_n_generations.append(group_dictionary_after_n_generations)
        #
        #
        #
        #         # print("---n_groups_simulation--")
        #     print("list_of_groups_after_selection = ", self.list_of_groups_after_n_generations)
        #     print("time_taken_for_old", timer() - start_time)
        #

        def list_of_groups_afer_one_generation(self, list_of_groups_in_current_generation):

            list_of_groups_after_one_generation = []

            for group_number in range(len(list_of_groups_in_current_generation)):

                #calculate group dictionary for
                group_dictionary_after_one_generations = self.population_growth_for_group_instance.find_group_dictionary_at_next_generation(list_of_groups_in_current_generation[group_number])
                list_of_groups_after_one_generation.append(group_dictionary_after_one_generations)



                # print("---n_groups_simulation--")
            # print("list_of_groups_after_selection = ", self.list_of_groups_after_one_generation)

            return list_of_groups_after_one_generation


        def find_list_of_groups_over_generations(self):


            list_of_groups_at_GIVEN_generation_in_pop_dict_over_time = self.initial_list_of_groups_for_calculating_population_growth_over_time

            for t in range(self.parameters_object.number_of_generations):
                # print("group_dictionary_at_generation " + str(t), group_dictionary_at_next_generation2)
                # print("-----" + "generation" + str(t + 1) + "------------")

                list_of_groups_at_next_generation_in_pop_dict_over_time = self.list_of_groups_afer_one_generation(list_of_groups_at_GIVEN_generation_in_pop_dict_over_time)
                # print("list_of_groups_at_next_generation_in_pop_dict_over_time " + str(t + 1), list_of_groups_at_next_generation_in_pop_dict_over_time)


                pooled_group_dictionary_at_next_generation = self.find_pooled_group_dictionary(list_of_groups_at_next_generation_in_pop_dict_over_time)




                # print("group_dictionaries_over_time_list_temp = ", group_dictionary_at_next_generation_in_pop_dict_over_time)

                if sum(pooled_group_dictionary_at_next_generation.values()) == 0:
                    break

                normalised_dictionary_at_next_generation = self.finding_normalised_group_dictionary_afer_pooling(pooled_group_dictionary_at_next_generation)
                # print("normalised_dictionary_at_next_generation at generation", str(t + 1), "=", normalised_dictionary_at_next_generation)


                for trait in parameters_object.C_value_dictionary:


                  sum_of_individuals_with_trait_in_group = 0
                  for group_in_group_list_to_be_pooled in list_of_groups_at_next_generation_in_pop_dict_over_time:  #
                    # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
                        sum_of_individuals_with_trait = 0

                        sum_of_individuals_with_trait_in_group += group_in_group_list_to_be_pooled[trait]



                  if sum_of_individuals_with_trait_in_group == 0:
                    break
                list_of_groups_at_GIVEN_generation_in_pop_dict_over_time = list_of_groups_at_next_generation_in_pop_dict_over_time



            # print("group_dictionaries_over_time_list = ", self.group_dictionaries_over_time_list)

            self.list_of_groups_after_n_generations = list_of_groups_at_GIVEN_generation_in_pop_dict_over_time

            return self.list_of_groups_after_n_generations




        def find_pooled_group_dictionary(self, list_of_groups_to_be_pooled):

            start_time = timer()
            population_dictionary_after_pooling = {}
            for trait in self.parameters_object.C_value_dictionary:

                sum_of_individuals_with_trait = 0
                for group_in_group_list_to_be_pooled in list_of_groups_to_be_pooled:
                    # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
                    sum_of_individuals_with_trait +=  group_in_group_list_to_be_pooled[trait]

                population_dictionary_after_pooling[trait] = sum_of_individuals_with_trait

            # print("self.population_dictionary_after_pooling",self.population_dictionary_after_pooling)


            # use mu
            #
            #
            #
            #
            #
            # ltiple traits


            #
            # sum_of_individuals_with_trait_C1 = 0
            # # print("self.list_of_groups_after_n_generations", self.list_of_groups_after_n_generations)
            # proportion_of_selfish_traits_dictionary_after_pooling = {}
            # for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
            #     # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
            #     sum_of_individuals_with_trait_C1 += group_in_group_list_to_be_pooled["C1"]



            # sum_of_individuals_with_trait_C2 = 0
            # for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
            #
            #
            #     # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
            #     sum_of_individuals_with_trait_C2 += group_in_group_list_to_be_pooled["C2"]
            #
            # total_number_of_individuals = sum_of_individuals_with_trait_C1 + sum_of_individuals_with_trait_C2
            #
            # if total_number_of_individuals != 0:
            #     proportion_of_selfish_traits_dictionary_after_pooling["C1"] = sum_of_individuals_with_trait_C1 / total_number_of_individuals
            #     proportion_of_selfish_traits_dictionary_after_pooling["C2"] = sum_of_individuals_with_trait_C2/ total_number_of_individuals
            #
            #
            # elif total_number_of_individuals == 0:
            #     self.proportion_of_selfish_traits_dictionary_after_pooling["C1"] = 0
            #     self.proportion_of_selfish_traits_dictionary_after_pooling["C2"] = 0

            # print("self.proportion_of_selfish_traits_dictionary_after_pooling =", proportion_of_selfish_traits_dictionary_after_pooling)
            # print(self.proportion_of_selfish_traits_dictionary_after_pooling)

            return population_dictionary_after_pooling



        def finding_normalised_group_dictionary_afer_pooling(self, population_dictionary_after_pooling):
            total_number_of_individuals = sum(population_dictionary_after_pooling.values())
            proportion_of_selfish_traits_dictionary_after_pooling = {}
            for trait_of_pooled_group_dictionary in population_dictionary_after_pooling:

                number_of_individuals_of_trait_in_pooled_group_dictionary =  population_dictionary_after_pooling[trait_of_pooled_group_dictionary]
                proportion_of_individuals_of_trait_in_pooled_group_dictionary = number_of_individuals_of_trait_in_pooled_group_dictionary/total_number_of_individuals
                proportion_of_selfish_traits_dictionary_after_pooling[trait_of_pooled_group_dictionary] = proportion_of_individuals_of_trait_in_pooled_group_dictionary

            # print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)
        #
        #     #use above box if you are gonna compete more more than two traits
        #
        #     self.proportion_of_selfish_traits_dictionary_after_pooling["C1"] = self.population_dictionary_after_pooling["C1"]/total_number_of_individuals
        #     self.proportion_of_selfish_traits_dictionary_after_pooling["C2"] = self.population_dictionary_after_pooling["C2"]/total_number_of_individuals
        #
        #     print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)
        #


        # def population_growth_pooling_and_normalising(self):
        #
        #
        #         self.population_growth_of_n_groups_over_time()
        #         self.find_normalised_groups_dictionary_after_pooling()
            return proportion_of_selfish_traits_dictionary_after_pooling




        def calcualate_net_fitness_for_a_gien_trait_at_given_time_step(self, trait):
                                                                                          #correct only if number of generations is 1

             # for trait in self.parameters_object.C_value_dictionary:

                sum_of_individuals_with_trait = 0
                for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
                    number_of_individuals_with_trait =  group_in_group_list_to_be_pooled[trait]
                    # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
                    sum_of_individuals_with_trait += number_of_individuals_with_trait

                net_fitness_of_trait_pooled_over_all_groups = sum_of_individuals_with_trait / 500

                return net_fitness_of_trait_pooled_over_all_groups


#
#
number_of_generations = 10

Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.99, "C2": 0.01}

Initial_population_size = 1000

number_of_selfish_traits = 2
Number_of_groups = 100
K2_value = 2
K1_value = 2


C_value_dictionary_for_model = {"C1":0, "C2":0.4}


parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                           K1_value, K2_value)




initial_groups_test_value = [{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}]
initial_groups_test_value2 = [{'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}, {'C1': 30.0, 'C2': 54.0}]


# population_growth_for_n_groups_instance = population_growth_for_n_groups_class(parameters_object,
#                                                                                initial_groups_test_value2)
# population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time()

# population_growth_for_n_groups_instance.find_list_of_groups_over_generations()
# population_growth_for_n_groups_instance.find_normalised_groups_dictionary_after_pooling()

# def reporting_the_winner():
#     if trait in


# population_growth_for_n_groups_class =
#construct function and cal it. Give proper daes.


