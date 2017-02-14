import random

main_pets = []

library_pets = ["mouse", "moose", "monkey", "elephant", "turtle", "deamon", "gremlin"]

user_pet_choice_1 = raw_input("Choose a pet ")
user_pet_choice_2 = raw_input("Choose another pet ")

def pets():
    computer_pet_choice_1 = main_pets.append(random.choice(library_pets))
    computer_pet_choice_2 = main_pets.append(random.choice(library_pets))
    main_pets.extend([user_pet_choice_1, user_pet_choice_2])
    return main_pets

print pets()

def return_one():
    selected_pet = random.choice(main_pets)
    return selected_pet

print return_one()


# 2 - Create a dictionary that selects two randomly generated choices from each key 
#     and combines them with the user input:

    
#     Pre-creadted dictionary will be composed of the following keys:

#         PARTNERS MALE - list of 50 celebrities and historical figures
#         PARTENERS FEMALE - list of 50 celebrities and historical figures
#         or combination option

#         PROFESSIONS - list of 100 different jobs

#         PETS - list of 50 different kinds of animals

#         NUMBER OF KIDS - a list of numbers from 1 - 20


#     New dictionary will be generated, it will contain the keys:
        
#         MASH - Mansion, Apartment, House, Shack 

#         PARTNER - Two user inputs, two computer generated selections

#         PROFESSIONS - Two user inputs, two computer generated selections

#         PETS - Two user inputs, two computer generated selections

#         NUMBER OF CHILDREN - Two user inputs, two computer generated selections

# 3 - Display the key/value pairs from the new dictionary to the user

# 4 - Ask the user to pick a number from 1-50.  User selection will be the "step"
#     for the elimination process.

# 5 - Create a while loop that itereates through the new dictionary by the step 
#     intereval that has been selected by the user.  Whatever value the step lands
#     on will be deleted.  The while loop will stop deleting values from each key
#     when the key only has one value left.  The loop will stop when each key has
#     only one value.

# 6 - Display the results of the MASH game to the user         








