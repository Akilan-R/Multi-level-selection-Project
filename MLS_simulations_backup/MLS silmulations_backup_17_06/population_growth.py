from absolute_Fitness_equations import *


Time_after_group_redistribution = 20
Number_of_redistributions = 10

population_of_trait_C1_in_group_1 = {}
group_number = 1

realised_fitness_of_trait_C1_dictionary
print(realised_fitness_of_trait_C1_dictionary['realised_fitness_of_trait_C1_in_group_5'])
old_number_of_individuals_with_trait_C1_in_group = Number_of_individuals_with_trait_C1_in_group


for j in range(Time_after_group_redistribution):
    new_number_of_individuals_with_trait_C1_in_group = old_number_of_individuals_with_trait_C1_in_group*realised_fitness_of_trait_C1_dictionary['realised_fitness_of_trait_C1_in_group_5']

    old_number_of_individuals_with_trait_C1_in_group = new_number_of_individuals_with_trait_C1_in_group
    new_number_of_individuals_with_trait_C1_in_group_at_time_step = "new_number_of_individuals_with_trait_C1_in_group_at_time_step " + str(j)

    population_of_trait_C1_in_group_1[j] = old_number_of_individuals_with_trait_C1_in_group

print(population_of_trait_C1_in_group_1)

