@ -20,6 +20,8 @@ class population_growth_for_n_groups_class:





            self.population_growth_for_group_instance = population_growth_for_group_class(parameters_object)


@ -63,53 +65,64 @@ class population_growth_for_n_groups_class:
        def find_normalised_groups_dictionary_after_pooling(self):

            start_time = timer()
            #
            # for trait in self.parameters_object.C_value_dictionary:
            #
            #     sum_of_individuals_with_trait = 0
            #     for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
            #         # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
            #         sum_of_individuals_with_trait +=  group_in_group_list_to_be_pooled[trait] #
            total_number_of_individuals = 0
            for trait in self.parameters_object.C_value_dictionary:

                sum_of_individuals_with_trait = 0
                for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
                    # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
                    sum_of_individuals_with_trait +=  group_in_group_list_to_be_pooled[trait]

            # use multiple traits
                    print("sum_of_individuals_with_trait =", sum_of_individuals_with_trait, "trait is",trait )

                    self.population_dictionary_after_pooling[trait] = sum_of_individuals_with_trait


            sum_of_individuals_with_trait_C1 = 0
            for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
                # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
                sum_of_individuals_with_trait_C1 += group_in_group_list_to_be_pooled["C1"]
        #
        #
        #     # use multiple traits
        #
        #
        #
        #     sum_of_individuals_with_trait_C1 = 0
        #     for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
        #         # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
        #         sum_of_individuals_with_trait_C1 += group_in_group_list_to_be_pooled["C1"]
        #
        #     self.population_dictionary_after_pooling["C1"] = sum_of_individuals_with_trait_C1
        #
        #
        #     sum_of_individuals_with_trait_C2 = 0
        #     for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
        #         # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
        #         sum_of_individuals_with_trait_C2 += group_in_group_list_to_be_pooled["C2"]
        #
        #     total_number_of_individuals = sum_of_individuals_with_trait_C1 + sum_of_individuals_with_trait_C2
        #     self.proportion_of_selfish_traits_dictionary_after_pooling["C1"] = sum_of_individuals_with_trait_C1 / total_number_of_individuals
        #     self.proportion_of_selfish_traits_dictionary_after_pooling["C2"] = sum_of_individuals_with_trait_C2/ total_number_of_individuals
        #
        #     # print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)
        #     # print(self.proportion_of_selfish_traits_dictionary_after_pooling)
        #
        #     return self.proportion_of_selfish_traits_dictionary_after_pooling

            self.population_dictionary_after_pooling["C1"] = sum_of_individuals_with_trait_C1


            sum_of_individuals_with_trait_C2 = 0
            for group_in_group_list_to_be_pooled in self.list_of_groups_after_n_generations:
                # print(number_of_individuals_with_trait, "number_of_individuals_with_trait")
                sum_of_individuals_with_trait_C2 += group_in_group_list_to_be_pooled["C2"]
        ###USE ABOVE ONLY IF THERE ARE ONLY TWO TRAITS. AND WANT A OPTIMISED CODE

            total_number_of_individuals = sum_of_individuals_with_trait_C1 + sum_of_individuals_with_trait_C2
            self.proportion_of_selfish_traits_dictionary_after_pooling["C1"] = sum_of_individuals_with_trait_C1 / total_number_of_individuals
            self.proportion_of_selfish_traits_dictionary_after_pooling["C2"] = sum_of_individuals_with_trait_C2/ total_number_of_individuals

            # print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)
            # print(self.proportion_of_selfish_traits_dictionary_after_pooling)

            return self.proportion_of_selfish_traits_dictionary_after_pooling
        # def finding_normalised_group_dictionary_afer_pooling(self):
            total_number_of_individuals = sum(self.population_dictionary_after_pooling.values())
            print(total_number_of_individuals)

            for trait_of_pooled_group_dictionary in self.population_dictionary_after_pooling:
                number_of_individuals_of_trait_in_pooled_group_dictionary =  self.population_dictionary_after_pooling[trait_of_pooled_group_dictionary]
                proportion_of_individuals_of_trait_in_pooled_group_dictionary = number_of_individuals_of_trait_in_pooled_group_dictionary/total_number_of_individuals
                self.proportion_of_selfish_traits_dictionary_after_pooling[trait_of_pooled_group_dictionary] = proportion_of_individuals_of_trait_in_pooled_group_dictionary

            print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)

        # def finding_normalised_group_dictionary_afer_pooling(self):
        #     total_number_of_individuals = sum(self.population_dictionary_after_pooling.values())
        #
        #     # for trait_of_pooled_group_dictionary in self.population_dictionary_after_pooling:
        #     #     number_of_individuals_of_trait_in_pooled_group_dictionary =  self.population_dictionary_after_pooling[trait_of_pooled_group_dictionary]
        #     #     proportion_of_individuals_of_trait_in_pooled_group_dictionary = number_of_individuals_of_trait_in_pooled_group_dictionary/total_number_of_individuals
        #     #     self.proportion_of_selfish_traits_dictionary_after_pooling[trait_of_pooled_group_dictionary] = proportion_of_individuals_of_trait_in_pooled_group_dictionary
        #
        #     # print("self.proportion_of_selfish_traits_dictionary_after_pooling =", self.proportion_of_selfish_traits_dictionary_after_pooling)
        #
        #     #use above box if you are gonna compete more more than two traits
        #
        #     self.proportion_of_selfish_traits_dictionary_after_pooling["C1"] = self.population_dictionary_after_pooling["C1"]/total_number_of_individuals
@ -145,43 +158,42 @@ class population_growth_for_n_groups_class:
                return net_fitness_of_trait_pooled_over_all_groups


#
#
# number_of_generations = 10
#
# Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
#
# Initial_population_size = 1000
#
# number_of_selfish_traits = 2
# Number_of_groups = 100
# K2_value = 2
# K1_value = 2
#
#
# C_value_dictionary_for_model = {"C1":0, "C2":0.4}
#
#
# parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
#                                                            number_of_selfish_traits, Number_of_groups,
#                                                            Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
#                                                            K1_value, K2_value)
#
#
#
#
#
# initial_groups_test_value = [{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}]
#
#
#
# population_growth_for_n_groups_instance = population_growth_for_n_groups_class(parameters_object,
#                                                                                initial_groups_test_value)
# # population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time()
#
# print("-------")
# population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time()
# population_growth_for_n_groups_instance.find_normalised_groups_dictionary_after_pooling()


number_of_generations = 1

Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.4, "C2": 0.4, "C3":0.2}

Initial_population_size = 1000

number_of_selfish_traits = 2
Number_of_groups = 100
K2_value = 2
K1_value = 0.5


C_value_dictionary_for_model = {"C1":0.1, "C2":0.1, "C3": 0.1}


parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                           K1_value, K2_value)





# initial_groups_test_value = [{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}, {"C1":50, "C2":50},{"C1":50, "C2":50}]

initial_groups_test_value= [{"C1": 10, "C2": 10, "C3":10}, {"C1": 10, "C2": 10, "C3":10}, {"C1": 10, "C2": 10, "C3":10}]

population_growth_for_n_groups_instance = population_growth_for_n_groups_class(parameters_object,
                                                                               initial_groups_test_value)
population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time()

population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time()
population_growth_for_n_groups_instance.find_normalised_groups_dictionary_after_pooling()

# def reporting_the_winner():
#     if trait in
