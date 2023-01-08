def for_function(numbers):
    targets = []
    numbers = numbers.split()
    for number in range(len(numbers)):
        targets.append(int(numbers[number]))
    return targets


def shoot_function(index, power, targets):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            del targets[index]


def add_function(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_function(index, radius, targets):
    if index - radius >= 0 and index + radius < len(targets):
        del targets[index - radius:index + radius + 1]
    else:
        print("Strike missed!")


def result_function(targets):
    targets = [str(target) for target in targets]
    targets = f"{'|'.join(targets)}"
    return targets


def while_function(numbers):
    targets = for_function(numbers)
    command = input()
    while command != "End":
        command = command.split()
        actions = command[0]
        if actions == "Shoot":
            index = int(command[1])
            power = int(command[2])
            shoot_function(index, power, targets)
        elif actions == "Add":
            index = int(command[1])
            value = int(command[2])
            add_function(index, value, targets)
        elif actions == "Strike":
            index = int(command[1])
            radius = int(command[2])
            strike_function(index, radius, targets)
        command = input()
    print(result_function(targets))


sequence_of_targets = input()
while_function(sequence_of_targets)
