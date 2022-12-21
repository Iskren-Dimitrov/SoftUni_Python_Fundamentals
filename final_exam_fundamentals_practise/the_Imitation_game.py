# encrypted_message = input()
# some_actions = input()
#
# while some_actions != "Decode":
#     command = some_actions.split("|")
#     current_command = command[0]
#     if current_command == "Move":
#         number_of_letters = int(command[1])
#         encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
#     elif current_command == "Insert":
#         index = int(command[1])
#         value = command[2]
#         encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
#     elif current_command == "ChangeAll":
#         substring = command[1]
#         replacement = command[2]
#         encrypted_message = encrypted_message.replace(substring, replacement)
#     some_actions = input()
# print(f"The decrypted message is: {encrypted_message}")

#
# def imitation_game(message):
#     command = input()
#     while command != "Decode":
#         command = command.split("|")
#         current_command = command[0]
#         if current_command == "Move":
#             number_of_letters = int(command[1])
#             message = message[number_of_letters:] + message[:number_of_letters]
#         elif current_command == "Insert":
#             index = int(command[1])
#             value = command[2]
#             message = message[:index] + value + message[index:]
#         elif current_command == "ChangeAll":
#             substring = command[1]
#             replacement = command[2]
#             message = message.replace(substring, replacement)
#         command = input()
#     print(f"The decrypted message is: {message}")
#
#
# data = input()
# imitation_game(data)


# def move(command: list, encrypted: str):
#     number_of_letters = int(command[1])
#     encrypted = encrypted[number_of_letters:] + encrypted[:number_of_letters]
#     return encrypted
#
#
# def insert(command: list, encrypted: str):
#     index, value = int(command[1]), command[2]
#     encrypted = encrypted[:index] + value + encrypted[index:]
#     return encrypted
#
#
# def change_all(command: list, encrypted: str):
#     substring, replacement = command[1], command[2]
#     encrypted = encrypted.replace(substring, replacement)
#     return encrypted
#
#
# message = input()
# instruction = input()
# while instruction != "Decode":
#     instruction = instruction.split("|")
#     action = instruction[0]
#     if action == "Move":
#         message = move(instruction, message)
#     elif action == "Insert":
#         message = insert(instruction, message)
#     elif action == "ChangeAll":
#         message = change_all(instruction, message)
#
#     instruction = input()
#
# print(f"The decrypted message is: {message}")


def move(numbers_of_letters, encrypted):
    encrypted = encrypted[numbers_of_letters:] + encrypted[:numbers_of_letters]
    return encrypted


def insert(index, value, encrypted):
    encrypted = encrypted[:index] + value + encrypted[index:]
    return encrypted


def change_all(substring, replacement, encrypted):
    encrypted = encrypted.replace(substring, replacement)
    return encrypted


def the_imitation_game(message):
    current_command = input()
    while current_command != "Decode":
        command = current_command.split("|")
        actions = command[0]
        if actions == "Move":
            numbers_of_letters = int(command[1])
            message = move(numbers_of_letters, message)
        elif actions == "Insert":
            index = int(command[1])
            value = command[2]
            message = insert(index, value, message)
        elif actions == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = change_all(substring, replacement, message)
        current_command = input()

    return print(f"The decrypted message is: {message}")


encrypted_message = input()
the_imitation_game(encrypted_message)
