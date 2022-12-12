# def password_validator(password):
#     valid = True
#     if len(password) < 6 or len(password) > 10:
#         print("Password must be between 6 and 10 characters")
#         valid = False
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         valid = False
#     digit_counter = 0
#     for character in password:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         print("Password must have at least 2 digits")
#         valid = False
#     if valid:
#         print("Password is valid")
#
#
# current_password = input()
# password_validator(current_password)

def password_validation(some_password):
    pass_is_valid = True
    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
        pass_is_valid = False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        pass_is_valid = False
    digit_counter = 0
    for character in some_password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False
    return pass_is_valid


password = input()
password_is_valid = password_validation(password)
if password_is_valid:
    print("Password is valid")


# 9.1

# def password_validation(some_password):
#     validation = []
#     if len(some_password) < 6 or len(some_password) > 10:
#         validation.append("Password must be between 6 and 10 characters")
#     if not some_password.isalnum():
#         validation.append("Password must consist only of letters and digits")
#     digit_counter = 0
#     for character in some_password:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         validation.append("Password must have at least 2 digits")
#     return validation
#
