#
#
# message = input().split()
# secret_message = []
#
# for word in message:
#     secret_word = []
#     first_letter = ""
#     rest_letters = ""
#     for character in word:
#         if character.isdigit():
#             first_letter += character
#         else:
#             rest_letters += character
#     first_letter = chr(int(first_letter))
#     rest_letters = list(rest_letters)
#     rest_letters[0], rest_letters[-1] = rest_letters[-1], rest_letters[0]
#     rest_letters = "".join(rest_letters)
#     secret_word = first_letter + rest_letters
#
#     secret_message.append(secret_word)
#
# print(*secret_message)
#
#
#
#


secret_message = input().split()
lst_secret_message = [message for message in secret_message]
digit = []
for word in lst_secret_message:
    num = ""
    words = ""
    for nums in word:
        if nums.isdigit():
            num += nums
        else:
            words += nums
    num = chr(int(num))
    words = list(words)
    words[0], words[-1] = words[-1], words[0]
    words = "".join(words)
    secret_word = num + words
    digit.append(secret_word)
print(" ".join(digit))
