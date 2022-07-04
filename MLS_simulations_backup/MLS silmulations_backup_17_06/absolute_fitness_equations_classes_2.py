# class k_values:
#     def __init__(self):
#
#         self.K1 = int(0)
#         self.K2 = int(0)

class individual_fitness_functions_for_trait:

    def __init__(self,  C_value, K1_value):

      self.C_value = C_value
      self.K1 = K1_value

    #
    # def print_input_paramaters_of_individual_fitness_class(self):
    #
    #    # print("K1_value = " + str(self.K1))
    #    # print("K2_value = " + str(self.K2))
    #    # print("C_value = " + str(self.C_value))
    #    # print("group_population_dictionary_at_given_time = " + str(self.group_population_dictionary_at_given_time))

    def individual_fitness_due_to_trait(self):
       individual_fitness = 1 + (self.K1 * self.C_value)
       # print("individual_fitness = " + str(individual_fitness))
       return individual_fitness

    # def find_effect_on_group_fitness_due_to_trait(self):
    #    self.effect_on_group_fitness_due_to_trait = 1 - (self.K2) * (self.C_value)
    #    return self.effect_on_group_fitness_due_to_trait



class fitness_of_group_class:
    def __init__(self, C_value_dictionary, group_population_dictionary_at_given_time, K2_value):
        self.group_population_dictionary_at_given_time = group_population_dictionary_at_given_time
        self.C_value_dictionary = C_value_dictionary
        self.proportions_of_trait_in_a_group = 0
        self.effect_on_group_fitness_due_to_trait = 0

        self.K2 = K2_value

    def print_input_paramaters_of_group_fitness_class(self):

        input_paramaters_of_group_fitness_class = ["C_value_dictionary = " + str(self.C_value_dictionary),"group_population_dictionary_at_given_time = " + str(self.group_population_dictionary_at_given_time),"K2_value = " + str(self.K2)]
        print("input_paramaters_of_group_fitness_class =", input_paramaters_of_group_fitness_class)
    #
    #     print("group_population_dictionary_at_given_time = " + str(self.group_population_dictionary_at_given_time))



    def find_effect_on_group_fitness_due_to_trait(self, k):
        C_value = self.C_value_dictionary[k]
        self.effect_on_group_fitness_due_to_trait = 1 - (self.K2) * (C_value)
        return self.effect_on_group_fitness_due_to_trait

    # def find_proportion_of_the_trait_in_the_group2(self):
    #
    #     for trait in self.group_population_dictionary_at_given_time:
    #         size_of_the_group = sum(self.group_population_dictionary_at_given_time.values())
    #         number_of_occurences_of_trait = self.group_population_dictionary_at_given_time[trait]
    #         self.proportions_of_trait_in_a_group = number_of_occurences_of_trait / size_of_the_group

    def find_proportion_of_the_trait_in_the_group(self, trait):

        size_of_the_group = sum(self.group_population_dictionary_at_given_time.values())
        number_of_occurences_of_trait = self.group_population_dictionary_at_given_time[trait]
        self.proportions_of_trait_in_a_group = number_of_occurences_of_trait / size_of_the_group
        return self.proportions_of_trait_in_a_group
            # print("proportions_of_trait_in_a_group =" + str(self.proportions_of_trait_in_a_group))

    def fitness_of_a_group(self):
        group_fitness = 0
        for k in self.group_population_dictionary_at_given_time:
            group_fitness = group_fitness + ((self.find_effect_on_group_fitness_due_to_trait(k)) * (self.find_proportion_of_the_trait_in_the_group(k)))
            # print("effect_on_group_fitness_due_to_trait " + str(k) + "=" + str(self.effect_on_group_fitness_due_to_trait))
            # print("proportion_of_the_trait_in_the_group " + str(k) + "=" + str(self.find_proportion_of_the_trait_in_the_group(k)))


        # print("group_fitness = " + str(group_fitness))

        return group_fitness

# def calculate_realised_fitness():









    # class realised_fitness_of_trait_in_group:
    #     def __init__(self):
    #
    #         self.gro

individual_fitness_functions_for_trait_06 = individual_fitness_functions_for_trait(0.6, 1)
# af.print_input_paramaters_of_fitness_class(

fg = fitness_of_group_class({'C1':0, 'C2': 0}, {'C1':10, 'C2':20}, 1)
# fg.print_input_paramaters_of_group_fitness_class()
fg.fitness_of_a_group()


# class find_realised_fitness_of_trait_in_group(individual_fitness_functions_for_trait, fitness_of_group_class):
#     def __init__(self):
#         super().__init__()
#
#
#
#         def realised_fitness_function(self):
#             individual_fitness_functions_for_trait() + fitness_of_group_class()

print("-------------")


#caluclating_realised_fitness
def find_realised_fitness_function(C_value, K1_value, C_value_dictionary, group_population_dictionary_at_given_time, K2_value):
    instance_for_fitness_of_group_class = fitness_of_group_class(C_value_dictionary, group_population_dictionary_at_given_time, K2_value)
    instance_for_fitness_of_group_class.print_input_paramaters_of_group_fitness_class()
    instance_for_individual_fitness_class = individual_fitness_functions_for_trait(C_value, K1_value)
    # instance_for_individual_fitness_class.print_input_paramaters_of_individual_fitness_class()

    def get_trait_from_C_value(val):
        for key, value in C_value_dictionary.items():
            if val == value:
                return key


    realised_fitness = instance_for_fitness_of_group_class.fitness_of_a_group() * instance_for_individual_fitness_class.individual_fitness_due_to_trait()
    print("realised_fitness for", get_trait_from_C_value(C_value), " =" + str(realised_fitness))
    return realised_fitness

C_value_dictionary_ex= {'C1':0, 'C2': 0.5}
find_realised_fitness_function(0.5, 1, C_value_dictionary_ex, {'C1': 75.0, 'C2': 112.5}, 1)

# input_paramaters_of_group_fitness_class = ["C_value_dictionary = {'C1': 0, 'C2': 0.5}", "group_population_dictionary_at_given_time = {'C1': 75.0, 'C2': 112.5}", 'K2_value = 1']
# realised_fitness for C2  = 1.0499999999999998