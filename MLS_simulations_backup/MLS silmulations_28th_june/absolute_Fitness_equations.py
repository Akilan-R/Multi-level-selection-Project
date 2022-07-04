from making_groups import *

realised_fitness_of_trait_C1_dictionary = {}
realised_fitness_of_trait_C2_dictionary = {}

for i in range(Number_of_groups):
    group_number = i
    group = combined_list_of_groups[group_number]
    Individual_fitness_of_trait_C1 = 1 + (K1__ * C1__)
    Effect_on_fitness_of_group_due_to_individual_with_trait_C1 = 1 - (K2__ * C1__)
    Effect_on_fitness_of_group_due_to_individual_with_trait_C2 = 1 - (K2__ * C2__)

    Number_of_individuals_with_trait_C1_in_group = group.count('C_value')

    proportion_of_individuals_with_trait_C1_in_group = (Number_of_individuals_with_trait_C1_in_group/size_of_each_group)
    proportion_of_individuals_with_trait_C2_in_group = 1 - proportion_of_individuals_with_trait_C1_in_group

    group_fitness = proportion_of_individuals_with_trait_C1_in_group*Effect_on_fitness_of_group_due_to_individual_with_trait_C1 + Effect_on_fitness_of_group_due_to_individual_with_trait_C2*Effect_on_fitness_of_group_due_to_individual_with_trait_C2

    realised_fitness_of_trait_C1 = Individual_fitness_of_trait_C1 * group_fitness
    realised_fitness_of_trait_C1_in_group_number = "realised_fitness_of_trait_C1_in_group_" + str(i)

    realised_fitness_of_trait_C1_dictionary[realised_fitness_of_trait_C1_in_group_number] = realised_fitness_of_trait_C1

