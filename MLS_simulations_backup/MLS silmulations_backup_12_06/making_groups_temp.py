import numpy as np
import random

random.seed(1)

Initial_population_size = 100
Number_of_groups = 10

C1__ = 0
C2__ = 0
K1__ = 0
K2__ = 0


# def generate_selfishness(Initial_population_size,
#                          number_of_selfish_traits):  # number_of_selfish_traits = C1, C2, C3 etc

size_of_each_group = int(Initial_population_size / Number_of_groups)

S1__proportion_of_individuals_with_trait_C1 = 0.5

S2__proportion_of_individuals_with_trait_C1 = 1 - S1__proportion_of_individuals_with_trait_C1
Number_of_individuals_with_trait_C1 = int(S1__proportion_of_individuals_with_trait_C1 * Initial_population_size)
Number_of_individuals_with_trait_C2 = Initial_population_size - Number_of_individuals_with_trait_C1

# make list containing of n1, with c1
# make list containing of n - n1 with c2

list_of_individuals_with_C1 = ["C1"] * Number_of_individuals_with_trait_C1
list_of_individuals_with_C2 = ["C2"] * Number_of_individuals_with_trait_C2

combined_list_of_individuals = list_of_individuals_with_C1 + list_of_individuals_with_C2
print("combined_list_of_individuals", combined_list_of_individuals)


# Randomosing combined list

random.shuffle(combined_list_of_individuals)


# breaking down groups

# def randomise_and_split_into_groups(Number_of_groups):
combined_list_of_groups = [combined_list_of_individuals[i * size_of_each_group:(i + 1) * size_of_each_group] for i in range((len(combined_list_of_individuals) + size_of_each_group - 1) // size_of_each_group)]

print("combined_list_of_groups", combined_list_of_groups)

