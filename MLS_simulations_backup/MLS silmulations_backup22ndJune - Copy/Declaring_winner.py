
def declaring_winner(normalised_population_dictionary_for_declaring_winner):
   winner = "X"
   for k in normalised_population_dictionary_for_declaring_winner:
     if normalised_population_dictionary_for_declaring_winner[k] > 0.99:
        winner = k
   print("winner_of_the_simulation_is =", winner)
   return winner


test_dict = {"C1": 1, "C2": 9}

declaring_winner(test_dict)

def ending_simulation(normalised_population_dictionary_for_declaring_winner):
   for k in normalised_population_dictionary_for_declaring_winner:
      if normalised_population_dictionary_for_declaring_winner[k] > 0.99:
        return 1
   else:
      return 0

print(ending_simulation(test_dict))

