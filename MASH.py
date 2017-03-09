import random

mash_library = ["Mansion", "Apartment", "Shack", "House", "Yurt", "Townhouse", 
                "Private Island", "Farm", "Tent"]
kids_library = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
pet_library = ["Moose", "Monkey", "Elephant", "Turtle", "Deamon", "Gremlin",
                "The Lochnest Monster", "Baby Shark", "Llama", "Duckling", "Porcupine"]
job_library = ["President of the United States", "Rocket Scientist", "Software Engineer",
                "Pro Tennis Player", "Fashion Designer", "International Pop Sensation", 
                "Concert Pianist", "Astronaut", "Animator", "Film Director", "CEO",
                "Foreign Service Agent", "Chef"]
main_pets = []
main_jobs = []
main_partners = []


def print_key_values():
    for key in mash_player_dictionary.keys():
        print mash_player_dictionary[key]


def populate_player_dictionary(list_to_append, user_choice_1, user_choice_2, source_library):
    list_to_append.extend([user_choice_1, user_choice_2])
    list_to_append.append(random.choice(source_library))
    second_random_choice = random.choice(source_library)
    while second_random_choice not in list_to_append:
        list_to_append.append(second_random_choice)
        return list_to_append    


def eliminate(list_to_eliminate_from, magic_number):
    index_to_remove = 0
    while len(list_to_eliminate_from) > 1:
        magic_number = magic_number - 1
        index_to_remove = index_to_remove + magic_number
        index_to_remove = index_to_remove % len(list_to_eliminate_from)
        list_to_eliminate_from.remove(list_to_eliminate_from[index_to_remove])
    return list_to_eliminate_from[0]     

def main():
    print "Wecome to MASH, answer a few questions and I can predict your future!  "
    jobs_1 = raw_input("What is your dream job?  ")
    jobs_2 = raw_input("What is your back-up dream job?  ")
    pets_1 = raw_input("What kind of pet would you like to have?  ")
    pets_2 = raw_input("And if you couldn't have that pet, what pet would you want?  ")
    partner_1 = raw_input("Enter the name of someone you would like to marry:  ")
    partner_2 = raw_input("Enter the name of someone you wouldn't like to marry:  ")
    magic_number = int(raw_input("Now pick a number between 1-20  "))
    populate_player_dictionary(main_pets, pets_1, pets_2, pet_library)
    populate_player_dictionary(main_jobs, jobs_1, jobs_2, job_library)
    main_partners.append(partner_1)
    main_partners.append(partner_2)
    home = eliminate(mash_library, magic_number)
    job = eliminate(main_jobs, magic_number)
    pet = eliminate(main_pets, magic_number)
    partner = eliminate(main_partners, magic_number)
    kids = eliminate(kids_library, magic_number) 
    print """Your future has been predicted!  You will live in/on a(n) %s, your will be a/an %s, your partner will be %s, you will have %s kid(s), and a %s for a pet""" % (home, job, partner, kids, pet)
    exit() 


main()

if __name__ == '__main__':
    main()


# if index_to_remove >= len(main_pets):
        #     index_to_remove = 0

