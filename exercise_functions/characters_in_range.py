def two_characters(first, second):
    character = []
    for char in range(ord(first) + 1, ord(second)):
        character.append(chr(char))
    return character


first_input = input()
second_input = input()
result = two_characters(first_input, second_input)
print(' '.join(result))

#
# def collect_charaters(first, second):
#     characters = []
#     for current_character in range(ord(first) + 1, ord(second)):
#         characters.append(chr(current_character))
#     return characters
#
#
# first_character = input()
# second_character = input()
# result = collect_charaters(first_character, second_character)
# print(' '.join(result))