
from making_groups import generate_groups
from population_growth_for_n_groups import population_growth_for_n_groups_class
from Declaring_winner import declaring_winner
from Declaring_winner import ending_simulation
from parameters_class_file import parameters_class


def main():
    number_of_generations = 1

    Initial_proportion_of_selfish_traits_dictionary = {"C1": 0.5, "C2": 0.5}
    C_value_dictionary_for_model = {'C1': 0, 'C2': 0}

    Initial_population_size = 10

    number_of_selfish_traits = 2
    Number_of_groups = 5
    K1_value = 0.5
    K2_value = 2
    C_value_dictionary_for_model = {'C1': 0, 'C2': 0}




    parameters_object = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                         number_of_selfish_traits, Number_of_groups,
                                         Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                         K1_value, K2_value)

    run_simulation(parameters_object)

def run_simulation(parameters_object):


    time_step_number = 0
    new_proportion_of_selfish_traits_dictionary = parameters_object.Initial_proportion_of_selfish_traits_dictionary
    while(True):
        time_step_number = time_step_number + 1
        print("------------------------------------------")
        print("time_step_number =",time_step_number)
        generating_groups_instance = generate_groups(parameters_object, new_proportion_of_selfish_traits_dictionary)
        generating_groups_instance.generate_list_of_individuals()
        generating_groups_instance.generate_group()
        list_of_groups_for_calculating_population_growth_over_time =  generating_groups_instance.convert_groups_to_compact_form()
        print("list_of_groups_at_the_time_step =", list_of_groups_for_calculating_population_growth_over_time)



        # population_growth_for_n_groups_instance.population_growth_of_n_groups_over_time(initial_groups_test_value)


        population_growth_for_n_groups_instance = population_growth_for_n_groups_class(parameters_object,list_of_groups_for_calculating_population_growth_over_time)
        new_proportion_of_selfish_traits_dictionary = population_growth_for_n_groups_instance.population_growth_pooling_and_normalising()
        print("new_proportion_of_selfish_traits_dictionary =", new_proportion_of_selfish_traits_dictionary)

        if ending_simulation(new_proportion_of_selfish_traits_dictionary) == 1:
            declaring_winner(new_proportion_of_selfish_traits_dictionary)
            print("number_of_time_steps = ", time_step_number)
            break

        # parameters.proportion_of_selfish_traits_dictionary = new_proportion_of_selfish_traits_dictionary







'D:\Research\Multi-level selection Project\MLS silmulations\Evolving_for_one_timestep.py'










if __name__ == "__main__":
    main()