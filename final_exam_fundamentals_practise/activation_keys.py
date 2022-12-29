def contains_function(substring, key):
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")
    return key


def flip_function(upper_lower, start_index, end_index, key):
    if upper_lower == "Upper":
        key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
    else:
        key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
    print(key)
    return key


def slice_function(start_index, end_index, key):
    key = key[:start_index] + "" + key[end_index:]
    print(key)
    return key


def while_function(key):
    command = input()
    while command != "Generate":
        command = command.split(">>>")
        actions = command[0]
        if actions == "Contains":
            substring = command[1]
            key = contains_function(substring, key)
        elif actions == "Flip":
            upper_lower = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            key = flip_function(upper_lower, start_index, end_index, key)
        elif actions == "Slice":
            start_index = int(command[1])
            end_index = int(command[2])
            key = slice_function(start_index, end_index, key)
        command = input()
    return print(f"Your activation key is: {key}")


text = input()
while_function(text)
