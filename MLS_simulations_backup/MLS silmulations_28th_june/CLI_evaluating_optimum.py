import numpy as np
from Evolving_for_one_timestep import run_simulation_class
from parameters_class_file import parameters_class
import time as time
import argparse
import json
import ast

start_time = time.time()


# python CLI_evaluating_optimum.py --num_of_gen 1 --init_pop_size 1000 --num_of_selfish_traits 2 --num_of_groups 100 --K1_value 0.5 --K2_value 2  --Ini_prop_of_selfish_traits '{\"C1\": 0.5, \"C2\": 0.5}'

# python -m cProfile evaluating_optimum_value.py  --num_of_gen 1 --init_pop_size 10 --num_of_selfish_traits 2 --num_of_groups 5 --K1_value 0.5 --K2_value 0.5  --Ini_prop_of_selfish_traits '{\"C1\": 0.5, \"C2\": 0.5}'


def main():
    parser = argparse.ArgumentParser()

    prepare_args(parser)
    args = parser.parse_args()

    print("===============================================")
    print(
        "--num_of_gen {} --init_pop_size {} --num_of_selfish_traits {} --num_of_groups {} --K1_value {} --K2_value {}".format(
            args.num_of_gen, args.init_pop_size, args.num_of_selfish_traits, args.num_of_groups, args.K1_value,
            args.K2_value))
    print("===============================================")

    print("--Ini_prop_of_selfish_traits : " + str(args.Ini_prop_of_selfish_traits))
    # print("--C_value_for_model: " + str(args.C_value_for_model))

    v1 = args.num_of_gen
    print("===============================================")


    number_of_generations = args.num_of_gen

    print("type_args.Ini_prop_of_selfish_traits)",type(args.Ini_prop_of_selfish_traits))


    # Initial_proportion_of_selfish_traits_dictionary = args.Ini_prop_of_selfish_traits
    # Initial_proportion_of_selfish_traits_dictionary = json.loads('{"C1": 0.5, "C2": 0.5}')
    temp = str(args.Ini_prop_of_selfish_traits)
    print("temp",temp)

    # temp = "'"+ temp + "'"
    # print("temp",temp)


    Initial_proportion_of_selfish_traits_dictionary = json.loads(temp)
    # Initial_proportion_of_selfish_traits_dictionary = ast.literal_eval(args.Ini_prop_of_selfish_traits)


    Initial_population_size = args.init_pop_size

    number_of_selfish_traits = args.num_of_selfish_traits
    Number_of_groups = args.num_of_groups
    K2_value = args.K2_value
    K1_value = args.K1_value


    C_value_dictionary_for_model= {}


    parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                           number_of_selfish_traits, Number_of_groups,
                                                           Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                           K1_value, K2_value)

    find_optimum_c_value_object = find_optimum_c_value_class(parameters_object_for_optimum_value)
    find_optimum_c_value_object.find_optimum_c_value_method()




# class find_optimum_c_value_class:



class find_optimum_c_value_class:
    def __init__(self, parameters_object_for_optimum_value):
        self.parameters_object_for_optimum_value = parameters_object_for_optimum_value



    def find_optimum_c_value_method(self):

        # parameters_object_corresponding_to_

        lower_bound_of_c_value = round(-1 / self.parameters_object_for_optimum_value.K1_value, 1)
        upper_bound_of_c_value = round(1 / self.parameters_object_for_optimum_value.K2_value, 1)
        least_count_of_c_values = 0.05
        C_value_range = np.arange(lower_bound_of_c_value, upper_bound_of_c_value, least_count_of_c_values)


        C_value_range = np.around(C_value_range, 2)
        print("C_value_range", C_value_range)
        # C_value_test_range = [1.6, 1.65, 1.7]


        optimum_flag = 0

        for k in C_value_range:
            optimum_flag = 1
            for l in C_value_range:


                C_value_dictionary_for_model = {"C1": k, "C2": l}
                Initial_population_size = self.parameters_object_for_optimum_value.Initial_population_size
                number_of_selfish_traits = self.parameters_object_for_optimum_value.number_of_selfish_traits
                Number_of_groups = self.parameters_object_for_optimum_value.Number_of_groups
                Initial_proportion_of_selfish_traits_dictionary = self.parameters_object_for_optimum_value.Initial_proportion_of_selfish_traits_dictionary
                number_of_generations = self.parameters_object_for_optimum_value.number_of_generations
                K1_value = self.parameters_object_for_optimum_value.K1_value
                K2_value = self.parameters_object_for_optimum_value.K2_value




                modified_parameters_object_for_optimum_value = parameters_class(C_value_dictionary_for_model, Initial_population_size,
                                                               number_of_selfish_traits, Number_of_groups,
                                                               Initial_proportion_of_selfish_traits_dictionary, number_of_generations,
                                                               K1_value, K2_value)



                if k != l:

                    run_simulation_object_1 = run_simulation_class(modified_parameters_object_for_optimum_value)
                    winner = run_simulation_object_1.run_simulation_method()
                    print("in_simulation_with", modified_parameters_object_for_optimum_value.C_value_dictionary, "the_winner_is", winner)

                    if winner != "C1":
                            optimum_flag = 0
                            break
            if optimum_flag == 1:
                optimum_c1_value = k
                print("the optimum c_value is =", optimum_c1_value)
                return optimum_c1_value


        print("--- %s seconds for evaluating optimum---" % (time.time() - start_time))



def prepare_args(parser):

        # parser = argparse.ArgumentParser()
        parser.add_argument('--num_of_gen', type=int, dest='num_of_gen', help="num_of_genxxxxxxxxxx")
        parser.add_argument('--init_pop_size', type=int, dest= 'init_pop_size',help="init_pop_sizeyyyyyyyy")
        parser.add_argument('--num_of_selfish_traits', type=int,dest='num_of_selfish_traits', help="num_of_selfish_traitseeeeeeeee")
        parser.add_argument('--num_of_groups', type=int, dest='num_of_groups',help="num_of_groups")

        parser.add_argument('--K1_value', type=float,dest='K1_value', help="K1_value")
        parser.add_argument('--K2_value', type=float,dest='K2_value', help="K2_value")

        parser.add_argument('--Ini_prop_of_selfish_traits',type = str, dest='Ini_prop_of_selfish_traits', help="K1_value")
        # parser.add_argument('--C_value_for_model',dest='C_value_for_model', help="K2_value")






if __name__ == "__main__":
    main()
