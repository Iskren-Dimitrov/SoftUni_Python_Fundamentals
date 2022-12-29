def while_function_sail(pirates):
    dictionary = {}
    while pirates != "Sail":
        command = pirates.split("||")
        cities = command[0]
        population = int(command[1])
        gold = int(command[2])
        if cities not in dictionary.keys():
            dictionary[cities] = [population, gold]
        else:
            dictionary[cities][0] += population
            dictionary[cities][1] += gold
        pirates = input()
    return dictionary


def plunder_function(town, people, gold, dictionary):
    dictionary[town][0] -= people
    dictionary[town][1] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if dictionary[town][0] == 0 or dictionary[town][1] == 0:
        del dictionary[town]
        print(f"{town} has been wiped off the map!")
    return dictionary


def prosper_function(town, gold, dictionary):
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        dictionary[town][1] += gold

        print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town][1]} gold.")
    return dictionary


def result_function(dictionary):
    if len(dictionary) > 0:
        print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
        for town, people_gold in dictionary.items():
            print(f"{town} -> Population: {people_gold[0]} citizens, Gold: {people_gold[1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def while_function_end(pirates):
    dictionary = while_function_sail(pirates)
    command = input()
    while command != "End":
        command = command.split("=>")
        actions = command[0]
        if actions == "Plunder":
            town = command[1]
            people = int(command[2])
            gold = int(command[3])
            plunder_function(town, people, gold, dictionary)
        elif actions == "Prosper":
            town = command[1]
            gold = int(command[2])
            prosper_function(town, gold, dictionary)
        command = input()
    return result_function(dictionary)


text = input()
while_function_end(text)
