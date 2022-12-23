def insert_space(insert, message):
    message = message[:insert] + " " + message[insert:]
    print(message)
    return message


def reverse(substring, message):
    if substring in message:
        message = message.replace(substring, "", 1)
        message = message + substring[::-1]
        print(message)
    else:
        print("error")

    return message


def change_all(substring, replacement, message):
    message = message.replace(substring, replacement)
    print(message)
    return message


def while_function(message):
    command = input()
    while command != "Reveal":
        command = command.split(":|:")
        actions = command[0]
        if actions == "InsertSpace":
            index = int(command[1])
            message = insert_space(index, message)
        elif actions == "Reverse":
            substring = command[1]
            message = reverse(substring, message)
        elif actions == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = change_all(substring, replacement, message)

        command = input()
    return print(f"You have a new text message: {message}")


text = input()
while_function(text)
