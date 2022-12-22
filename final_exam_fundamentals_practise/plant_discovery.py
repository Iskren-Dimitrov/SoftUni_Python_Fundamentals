def for_function(plants):
    plant_discovery = {}
    for plants in range(plants):
        command = input().split("<->")
        plant = command[0]
        rarity = int(command[1])
        plant_discovery[plant] = [rarity, []]

    return plant_discovery


def rate_function(plant, rating, plant_discovery):
    if plant in plant_discovery:
        plant_discovery[plant][1].append(rating)
    else:
        print("error")


def update_function(plant, new_rarity, plant_discovery):
    if plant in plant_discovery:
        plant_discovery[plant][0] = new_rarity
    else:
        print("error")


def reset_function(plant, plant_discovery):
    if plant in plant_discovery:
        plant_discovery[plant][1] = []
    else:
        print("error")


def print_function(plant_discovery):
    print(f"Plants for the exhibition:")
    for plant, rarity_rating in plant_discovery.items():
        if sum(rarity_rating[1]) > 0:
            rating = sum(rarity_rating[1]) / len(rarity_rating[1])
            print(f"- {plant}; Rarity: {rarity_rating[0]}; Rating: {rating:.2f}")
        else:
            rarity_rating[1] = 0
            print(f"- {plant}; Rarity: {rarity_rating[0]}; Rating: {rarity_rating[1]:.2f}")


def while_function(plants):
    plant_discovery = for_function(plants)
    command = input()
    while command != "Exhibition":
        command = command.split(": ")
        actions = command[0]
        if actions == "Rate":
            command = command[1].split(" - ")
            plant = command[0]
            rating = int(command[1])
            rate_function(plant, rating, plant_discovery)
        elif actions == "Update":
            command = command[1].split(" - ")
            plant = command[0]
            new_rarity = int(command[1])
            update_function(plant, new_rarity, plant_discovery)
        elif actions == "Reset":
            plant = command[1]
            reset_function(plant, plant_discovery)
        command = input()
    return print_function(plant_discovery)


plant_count = int(input())
while_function(plant_count)
