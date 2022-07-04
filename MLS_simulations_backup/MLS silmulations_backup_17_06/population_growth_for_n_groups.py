import population_growth_2

population_growth_for_group_instance = population_growth_2.population_growth_for_group_class()
# population_growth_for_group_instance.finding_population_dictionaries_over_time({'C1': 100, 'C2': 100})



def population_growth_of_n_groups_over_time(initial_list_of_groups_for_calulating_population_growth_over_time):

    list_of_groups_after_n_generations = []
    for group in initial_list_of_groups_for_calulating_population_growth_over_time:
        population_growth_for_group_instance.finding_population_dictionaries_over_time(initial_list_of_groups_for_calulating_population_growth_over_time[group])
        group_dictionary_after_n_generations = population_growth_for_group_instance.finding_population_dictionary_at_the_end_of_n_generations()
        list_of_groups_after_n_generations.append(group_dictionary_after_n_generations)
        print("---n_groups_simulation--")
        print("list_of_groups_after_n_generations = ", list_of_groups_after_n_generations)
    return group_dictionary_after_n_generations






print(population_growth_of_n_groups_over_time())