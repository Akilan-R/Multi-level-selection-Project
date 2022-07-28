import parameters
# from parameters import *
from making_groups import generate_groups
from population_growth_for_n_groups import population_growth_for_n_groups_class
from Declaring_winner import declaring_winner
from Declaring_winner import ending_simulation






def find_winner_for_given_C_values(C_value_dictionary_for_finding_optimum):

    parameters.C_value_dictionary_for_model = C_value_dictionary_for_finding_optimum
    # C_value_dictionary_for_model = {C1:}
    print(C_value_dictionary_for_model)

    time_step_number = 0
    new_proportion_of_selfish_traits_dictionary = Initial_proportion_of_selfish_traits_dictionary
    while(True):
        time_step_number = time_step_number + 1
        print("------------------------------------------")
        print("time_step_number =",time_step_number)
        generating_groups_instance = generate_groups(Initial_population_size, number_of_selfish_traits,
                                                     Number_of_groups, new_proportion_of_selfish_traits_dictionary)

        generating_groups_instance.generate_list_of_individuals()
        generating_groups_instance.generate_group()
        list_of_groups_for_calculating_population_growth_over_time =  generating_groups_instance.convert_groups_to_compact_form()
        # print("list_of_groups_at_the_time_step =", list_of_groups_for_calculating_population_growth_over_time)



        # population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time(initial_groups_test_value)


        population_growth_for_n_groups_instance = population_growth_for_n_groups_class(
            list_of_groups_for_calculating_population_growth_over_time, )
        new_proportion_of_selfish_traits_dictionary = population_growth_for_n_groups_instance.population_growth_pooling_and_normalising()
        print("new_proportion_of_selfish_traits_dictionary =", new_proportion_of_selfish_traits_dictionary)

        if ending_simulation(new_proportion_of_selfish_traits_dictionary) == 1:
            declaring_winner(new_proportion_of_selfish_traits_dictionary)
            print("number_of_time_steps = ", time_step_number)
            break

        # parameters.proportion_of_selfish_traits_dictionary = new_proportion_of_selfish_traits_dictionary


















# if __name__ == "__main__":
#     main()



find_winner_for_given_C_values({'C1' : 0, 'C2' : 0})