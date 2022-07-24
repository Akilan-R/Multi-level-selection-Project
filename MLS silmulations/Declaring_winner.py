
def declaring_winner_and_ending_simulation(normalised_population_dictionary_for_declaring_winner, time_step_number):
   winner = "X"
   for k in normalised_population_dictionary_for_declaring_winner:
     if normalised_population_dictionary_for_declaring_winner[k] > 0.99:
        winner = k
     elif (time_step_number > 100 and normalised_population_dictionary_for_declaring_winner[k] > 0.95) or (time_step_number > 150 and normalised_population_dictionary_for_declaring_winner[k] > 0.85) or (time_step_number > 200 and normalised_population_dictionary_for_declaring_winner[k] > 0.75) or (time_step_number > 350 and normalised_population_dictionary_for_declaring_winner[k] > 0.6) :
        winner = k
   if time_step_number > 400:
         winner = "none"


   # print("winner_of_the_simulation_is =", winner)
   return winner



test_dict = {"C1": 1, "C2": 9}

# declaring_winner(test_dict)

def ending_simulation(normalised_population_dictionary_for_declaring_winner, time_step_number):
   for k in normalised_population_dictionary_for_declaring_winner:

      if normalised_population_dictionary_for_declaring_winner[k] > 0.99:
        return 1

      elif (time_step_number > 250 and normalised_population_dictionary_for_declaring_winner[k] > 0.95) or (
              time_step_number > 500 and normalised_population_dictionary_for_declaring_winner[k] > 0.85) or (
              time_step_number > 1000 and normalised_population_dictionary_for_declaring_winner[k] > 0.75) or (
              time_step_number > 1500 and normalised_population_dictionary_for_declaring_winner[k] > 0.6):
        return 1

      elif time_step_number > 2000:
          return 1
      else:
          return 0






def declaring_winner(normalised_population_dictionary_for_declaring_winner, time_step_number):
   winner = "X"
   for k in normalised_population_dictionary_for_declaring_winner:
     if normalised_population_dictionary_for_declaring_winner[k] > 0.99:
        winner = k
     elif (time_step_number > 250 and normalised_population_dictionary_for_declaring_winner[k] > 0.95) or (time_step_number > 500 and normalised_population_dictionary_for_declaring_winner[k] > 0.85) or (time_step_number > 1000 and normalised_population_dictionary_for_declaring_winner[k] > 0.75) or (time_step_number > 1500 and normalised_population_dictionary_for_declaring_winner[k] > 0.6) :
        winner = k
     elif time_step_number > 2000:
         winner = "none"
   # print("winner_of_the_simulation_is =", winner)
   return winner



test_dict = {"C1": 1, "C2": 9}

# declaring_winner(test_dict)

def ending_simulation(normalised_population_dictionary_for_declaring_winner, time_step_number):
   for k in normalised_population_dictionary_for_declaring_winner:
      if normalised_population_dictionary_for_declaring_winner[k] > 0.99:
        return 1

      elif (time_step_number > 250 and normalised_population_dictionary_for_declaring_winner[k] > 0.95) or (
              time_step_number > 500 and normalised_population_dictionary_for_declaring_winner[k] > 0.85) or (
              time_step_number > 1000 and normalised_population_dictionary_for_declaring_winner[k] > 0.75) or (
              time_step_number > 1500 and normalised_population_dictionary_for_declaring_winner[k] > 0.6):
        return 1

      elif time_step_number > 2000:
          return 1
      else:
          return 0



# print(ending_simulation(test_dict))

