def for_function(array_values):
    array_list = []
    array_values = array_values.split()

    for array in range(len(array_values)):
        array_list.append(int(array_values[array]))
    return array_list


def swap_function(index1, index2, array_list):
    array_list[index1], array_list[index2] = array_list[index2], array_list[index1]


def multiply_function(index1, index2, array_list):
    array_list[index1] = array_list[index1] * array_list[index2]


def decrease_function(array_list):
    for decrease in range(len(array_list)):
        array_list[decrease] -= 1


def print_function(array_list):
    array_list = [str(numbers) for numbers in array_list]
    return array_list


def while_function(array_values):
    array_list = for_function(array_values)
    command = input()
    while command != "end":
        command = command.split()
        actions = command[0]
        if actions == "swap":
            index1 = int(command[1])
            index2 = int(command[2])
            swap_function(index1, index2, array_list)
        elif actions == "multiply":
            index1 = int(command[1])
            index2 = int(command[2])
            multiply_function(index1, index2, array_list)
        elif actions == "decrease":
            decrease_function(array_list)
        command = input()
    print(", ".join(print_function(array_list)))


commands = input()
while_function(commands)
