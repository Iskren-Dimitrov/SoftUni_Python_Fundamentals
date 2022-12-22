def add_stop_function(index, string, destination):
    if 0 <= index < len(destination):
        destination = destination[:index] + string + destination[index:]
    return destination


def remove_stop_function(start_index, end_index, destination):
    if 0 <= start_index <= end_index < len(destination):
        destination = destination[:start_index] + destination[end_index + 1:]
    return destination


def switch_old_new_string(old_string, new_string, destination):
    if old_string in destination:
        destination = destination.replace(old_string, new_string)
    return destination


def function_world_tour(destination):
    command = input()
    while command != "Travel":
        command = command.split(":")
        actions = command[0]
        if actions == "Add Stop":
            index = int(command[1])
            string = command[2]
            destination = add_stop_function(index, string, destination)
        elif actions == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            destination = remove_stop_function(start_index, end_index, destination)
        elif actions == "Switch":
            old_string = command[1]
            new_string = command[2]
            destination = switch_old_new_string(old_string, new_string, destination)
        print(destination)
        command = input()
    print(f"Ready for world tour! Planned stops: {destination}")


stops = input()
function_world_tour(stops)
