


list_of_groups_to_be_pooled = [{'C1': 0, 'C2': 0.7781168529899345}, {'C1': 0, 'C2': 1.1199319701088764}, {'C1': 0, 'C2': 0.1199319701088764}, {'C1': 0, 'C2': 1.0645434512066465}, {'C1': 0, 'C2': 0.8554095482335058}]
trait = "C2"
sum_of_individuals_with_trait = 0
for group_in_group_list_to_be_pooled in list_of_groups_to_be_pooled:
    number_of_individuals_with_trait = group_in_group_list_to_be_pooled[trait]
    print(number_of_individuals_with_trait)
    sum_of_individuals_with_trait += number_of_individuals_with_trait
print("sum_of_individuals_with_trait =",sum_of_individuals_with_trait)


print(0.7781168529899345 + 1.1199319701088764 + 0.1199319701088764 + 0.8554095482335058)


import numpy as np
def s_int(x):
    a = np.floor(x)
    b = a + 1
    return (np.random.choice([a, b], p=[b - x, x - a]))
print(s_int(1.7))


for i in range(0, 10):
    print(s_int(1.7))

