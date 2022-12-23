def for_function(number_of_cars):
    cars_dictionary = {}
    for car in range(number_of_cars):
        current_cars = input().split("|")
        car = current_cars[0]
        distance = int(current_cars[1])
        fuel = int(current_cars[2])
        cars_dictionary[car] = [distance, fuel]
    return cars_dictionary


def drive_function(car, distance, fuel, cars_dictionary):
    if cars_dictionary[car][1] < fuel:
        print(f"Not enough fuel to make that ride")
    elif cars_dictionary[car][1] > fuel:
        cars_dictionary[car][0] += distance
        cars_dictionary[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if cars_dictionary[car][0] >= 100000:
        del cars_dictionary[car]
        print(f"Time to sell the {car}!")


def refuel_function(car, fuel, cars_dictionary):
    if cars_dictionary[car][1] + fuel <= 75:
        cars_dictionary[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif cars_dictionary[car][1] + fuel > 75:
        diff = 75 - (cars_dictionary[car][1])
        print(f"{car} refueled with {diff} liters")
        cars_dictionary[car][1] = 75


def revert_function(car, kilometers, cars_dictionary):
    cars_dictionary[car][0] -= kilometers
    if cars_dictionary[car][0] < 10000:
        cars_dictionary[car][0] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


def result_function(cars_dictionary):
    for car, mileage_fuel in cars_dictionary.items():
        print(f"{car} -> Mileage: {mileage_fuel[0]} kms, Fuel in the tank: {mileage_fuel[1]} lt.")


def while_function(number_of_cars):
    cars_dictionary = for_function(number_of_cars)
    command = input()
    while command != "Stop":
        command = command.split(" : ")
        actions = command[0]
        if actions == "Drive":
            car = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            drive_function(car, distance, fuel, cars_dictionary)
        elif actions == "Refuel":
            car = command[1]
            fuel = int(command[2])
            refuel_function(car, fuel, cars_dictionary)
        elif actions == "Revert":
            car = command[1]
            kilometers = int(command[2])
            revert_function(car, kilometers, cars_dictionary)
        command = input()
    return result_function(cars_dictionary)


count_cars = int(input())
while_function(count_cars)
