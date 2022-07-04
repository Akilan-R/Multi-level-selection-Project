# class k_values:
#     def __init__(self):
#
#         self.K1 = int(0)
#         self.K2 = int(0)

class fitness_functions_for_trait:

    def __init__(self, C_value_dictionary, K1_value, K2_value, group_population_dictionary_at_given_time):

      self.C_value_dictionary = C_value_dictionary
      self.K1 = K1_value
      self.K2 = K2_value

      self.group_population_dictionary_at_given_time = group_population_dictionary_at_given_time
      self.proportions_of_trait_in_a_group = 0
      self.effect_on_group_fitness_due_to_trait = 0

    def print_input_paramaters_of_fitness_class(self):
        # print("C_value = " + str(self.C_value))
        # print("K1_value = " + str(self.K1))
        # print("K2_value = " + str(self.K2))
        # print("group_population_dictionary_at_given_time = " + str(self.group_population_dictionary_at_given_time))



    def individual_fitness_due_to_trait(self):
       individual_fitness = 1 + (self.K1 * self.C_value)
       print("individual_fitness = " + str(individual_fitness))

    def find_effect_on_group_fitness_due_to_trait(self):
       self.effect_on_group_fitness_due_to_trait = 1 - (self.K2) * (self.C_value)
       return self.effect_on_group_fitness_due_to_trait

# class fitness_of_group_class():
#     def __init__(self, group_population_dictionary_at_given_time):

    #write
    def find_proportion_of_the_trait_in_the_group2(self):

        for trait in self.group_population_dictionary_at_given_time:
            size_of_the_group = sum(self.group_population_dictionary_at_given_time.values())
            number_of_occurences_of_trait = self.group_population_dictionary_at_given_time[trait]
            self.proportions_of_trait_in_a_group = number_of_occurences_of_trait / size_of_the_group
            # print("proportions_of_trait_in_a_group =" + str(self.proportions_of_trait_in_a_group))

    def find_proportion_of_the_trait_in_the_group(self, trait):

        size_of_the_group = sum(self.group_population_dictionary_at_given_time.values())
        number_of_occurences_of_trait = self.group_population_dictionary_at_given_time[trait]
        self.proportions_of_trait_in_a_group = number_of_occurences_of_trait / size_of_the_group
        return self.proportions_of_trait_in_a_group
            # print("proportions_of_trait_in_a_group =" + str(self.proportions_of_trait_in_a_group))

    def fitness_of_a_group(self):
        group_fitness = 0
        for k in self.group_population_dictionary_at_given_time:
            group_fitness = group_fitness + (self.find_effect_on_group_fitness_due_to_trait()) * (self.find_proportion_of_the_trait_in_the_group(k))
            print("effect_on_group_fitness_due_to_trait " + str(k) + "=" + str(self.effect_on_group_fitness_due_to_trait))

        print("group_fitness = " + str(group_fitness))

        return group_fitness





#
    # class realised_fitness_of_trait_in_group:
    #     def __init__(self):
    #
    #         self.gro

af = fitness_functions_for_trait(0.6 ,1 , 1 ,{'C1': 3, 'C2': 2})
af.print_input_paramaters_of_fitness_class()
af.individual_fitness_due_to_trait()
af.find_effect_on_group_fitness_due_to_trait()
af.fitness_of_a_group()
