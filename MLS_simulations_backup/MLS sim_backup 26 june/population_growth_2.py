from absolute_fitness_equations_classes_2 import fitness_of_group_class
from absolute_fitness_equations_classes_2 import individual_fitness_functions_for_trait




class population_growth_for_group_class():
    def __init__(self, parameters_object):
        # self.initial_group_dictionary = initial_group_dictionary
        self.group_dictionaries_over_time_list = []
        self.parameters_object = parameters_object

        # self.group_dictionary_at_given_generation = {}
        # self.trait = trait
        # self.group_dictionary_at_next_generation = {}
    def find_group_dictionary_at_next_generation(self, group_dictionary_at_given_generation):
        group_dictionary_at_next_generation = {}
        for k in self.parameters_object.C_value_dictionary:

            C_value = self.parameters_object.C_value_dictionary[k]

            realised_fitness_of_of_given_trait_in_given_group_at_given_generation =  self.find_realised_fitness_function(C_value, group_dictionary_at_given_generation)
            # print("for trait", k, realised_fitness_of_of_given_trait_in_given_group_at_given_generation)


            number_of_individuals_of_given_trait_in_given_group_at_given_generation = group_dictionary_at_given_generation[k]


            number_of_individuals_of_given_trait_in_given_group_at_next_generation = number_of_individuals_of_given_trait_in_given_group_at_given_generation*realised_fitness_of_of_given_trait_in_given_group_at_given_generation
            if number_of_individuals_of_given_trait_in_given_group_at_next_generation < 0.05:

                number_of_individuals_of_given_trait_in_given_group_at_next_generation = 0


            group_dictionary_at_next_generation[k] = number_of_individuals_of_given_trait_in_given_group_at_next_generation
            # print(self.group_dictionary_at_next_generation[k])
            # print(self.group_dictionary_at_next_generation)
            # return self.group_dictionary_at_next_generation



        return group_dictionary_at_next_generation


    def finding_population_dictionaries_over_time(self, group_dictionary_at_beginning_of_cycle):
        # group_dictionary_at_given_generation = group_dictionary_at_beginning_of_cycle
        # self.group_dictionary_at_given_generation = self.group_dictionary_at_given_generation
        group_dictionary_at_given_generation_in_pop_dict_over_time = group_dictionary_at_beginning_of_cycle
        self.group_dictionaries_over_time_list = [group_dictionary_at_beginning_of_cycle]


        for t in range(self.parameters_object.number_of_generations):
            # print("group_dictionary_at_generation " + str(t), group_dictionary_at_next_generation2)
            # print("-----" + "generation" + str(t + 1) + "------------")

            group_dictionary_at_next_generation_in_pop_dict_over_time = self.find_group_dictionary_at_next_generation(group_dictionary_at_given_generation_in_pop_dict_over_time)
            # print("group_dictionary_at_generation " + str(t), group_dictionary_at_next_generation_in_pop_dict_over_time)

            self.group_dictionaries_over_time_list.append(group_dictionary_at_next_generation_in_pop_dict_over_time)
            # print("group_dictionaries_over_time_list_temp = ", self.group_dictionaries_over_time_list)

            group_dictionary_at_given_generation_in_pop_dict_over_time = group_dictionary_at_next_generation_in_pop_dict_over_time

        # print("group_dictionaries_over_time_list = ", self.group_dictionaries_over_time_list)


        return self.group_dictionaries_over_time_list

    def finding_population_dictionary_at_the_end_of_n_generations(self):
        group_dictionaries_at_the_end_of_n_generations = self.group_dictionaries_over_time_list[-1]
        # print("group_dictionaries_at_the_end_of_n_generations = ", group_dictionaries_at_the_end_of_n_generations)
        return group_dictionaries_at_the_end_of_n_generations



    def find_realised_fitness_function(self, C_value, group_population_dictionary_at_given_time):



        instance_for_fitness_of_group_class = fitness_of_group_class(self.parameters_object.C_value_dictionary,
                                                                     group_population_dictionary_at_given_time,
                                                                     self.parameters_object.K2_value)
        # instance_for_fitness_of_group_class.print_input_paramaters_of_group_fitness_class()


        instance_for_individual_fitness_class = individual_fitness_functions_for_trait(C_value, self.parameters_object.K1_value)

        # instance_for_individual_fitness_class.print_input_paramaters_of_individual_fitness_class()

        def get_trait_from_C_value(val):
            for key, value in self.parameters_object.C_value_dictionary.items():
                if val == value:
                    return key

        realised_fitness = instance_for_fitness_of_group_class.fitness_of_a_group() * instance_for_individual_fitness_class.individual_fitness_due_to_trait()
        # print("realised_fitness for", get_trait_from_C_value(C_value), " =" + str(realised_fitness))
        return realised_fitness















initial_group_dictionary = {'C1': 100, 'C2': 100}
test_trait = 'C1'
# test_population_growth_class = population_growth_for_group_class()
# test_population_growth_class.find_group_dictionary_at_next_generation(initial_group_dictionary)
# test_population_growth_class.finding_population_dictionaries_over_time(initial_group_dictionary)
# test_population_growth_class.finding_population_dictionary_at_the_end_of_n_generations()