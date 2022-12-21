def for_function(count):
    dictionary = {}
    for pieces in range(count):
        command = input().split("|")
        piece = command[0]
        composer = command[1]
        key = command[2]
        dictionary[piece] = [composer, key]
    return dictionary


def add_function(piece, composer, key, dictionary):
    if piece not in dictionary:
        dictionary[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_function(piece, dictionary):
    if piece in dictionary:
        del dictionary[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_function(piece, new_key, dictionary):
    if piece in dictionary:
        dictionary[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_function(dictionary):
    for piece, composer_key in dictionary.items():
        print(f"{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}")


def while_function(count):
    dictionary = for_function(count)
    command = input()
    while command != "Stop":
        command = command.split("|")
        actions = command[0]
        piece = command[1]
        if actions == "Add":
            composer = command[2]
            key = command[3]
            add_function(piece, composer, key, dictionary)
        elif actions == "Remove":
            remove_function(piece, dictionary)
        elif actions == "ChangeKey":
            new_key = command[2]
            change_key_function(piece, new_key, dictionary)
        command = input()
    return print_function(dictionary)


piece_count = int(input())
while_function(piece_count)

# def add_function(piece, composer, key, dictionary):
#     if piece not in dictionary:
#         dictionary[piece] = [composer, key]
#         print(f"{piece} by {composer} in {key} added to the collection!")
#     else:
#         print(f"{piece} is already in the collection!")
#     return dictionary
#
#
# def remove(piece, dictionary):
#     if piece in dictionary:
#         del dictionary[piece]
#         print(f"Successfully removed {piece}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#     return dictionary
#
#
# def change_key(piece, new_key, dictionary):
#     if piece in dictionary:
#         dictionary[piece][1] = new_key
#         print(f"Changed the key of {piece} to {new_key}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#     return dictionary
#
#
# count_pieces = int(input())
# dictionary = {}
#
# for pieces in range(count_pieces):
#     command = input().split("|")
#     piece = command[0]
#     composer = command[1]
#     key = command[2]
#
#     dictionary[piece] = [composer, key]
#
# new_command = input()
# while new_command != 'Stop':
#     new_command = new_command.split("|")
#     actions = new_command[0]
#     if actions == "Add":
#         piece = new_command[1]
#         composer = new_command[2]
#         key = new_command[3]
#         dictionary = add_function(piece, composer, key, dictionary)
#     elif actions == "Remove":
#         piece = new_command[1]
#         dictionary = remove(piece, dictionary)
#     elif actions == "ChangeKey":
#         piece = new_command[1]
#         new_key = new_command[2]
#         dictionary = change_key(piece, new_key, dictionary)
#     new_command = input()
#
# for piece, composer_key in dictionary.items():
#     print(f"{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}")

# def add_piece(piece, composer, key, collection):
#     if piece not in collection:
#         collection[piece] = {"composer": composer, "key": key}
#         print(f"{piece} by {composer} in {key} added to the collection!")
#     else:
#         print(f"{piece} is already in the collection!")
#     return collection
#
#
# def remove_piece(piece, collection):
#     if piece in collection:
#         del collection[piece]
#         print(f"Successfully removed {piece}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#     return collection
#
#
# def change_key(piece, new_key, collection):
#     if piece in collection:
#         collection[piece]["key"] = new_key
#         print(f"Changed the key of {piece} to {new_key}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#     return collection
#
#
# count = int(input())
# collection = {}
#
# for line in range(count):
#     piece, composer, key = input().split("|")
#     collection[piece] = {"composer": composer, "key": key}
#
# command = input()
# while command != "Stop":
#     command = command.split("|")
#     action = command[0]
#     if action == "Add":
#         piece, composer, key = command[1], command[2], command[3]
#         collection = add_piece(piece, composer, key, collection)
#     elif action == "Remove":
#         piece = command[1]
#         collection = remove_piece(piece, collection)
#     elif action == "ChangeKey":
#         piece, new_key = command[1], command[2]
#         collection = change_key(piece, new_key, collection)
#     command = input()
#
# for piece, info in collection.items():
#     print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
