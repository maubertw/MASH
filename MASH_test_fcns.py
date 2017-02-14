import random

main_pets = []

library_pets = ["mouse", "moose", "monkey", "elephant", "turtle", "deamon", "gremlin"]

user_pet_choice_1 = raw_input("Choose a pet ")
user_pet_choice_2 = raw_input("Choose another pet ")

def pets():
    computer_pet_choice_1 = main_pets.append(random.choice(library_pets))
    library_pets.remove(computer_pet_choice_1)
    computer_pet_choice_2 = main_pets.append(random.choice(library_pets))
    library_pets.remove(computer_pet_choice_2)
    main_pets.extend([user_pet_choice_1, user_pet_choice_2])
    return main_pets

print pets()

def return_one():
    selected_pet = random.choice(main_pets)
    return selected_pet

print return_one()
