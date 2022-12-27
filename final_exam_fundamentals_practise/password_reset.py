def take_odd(password):
    new_password = ""
    for index in range(len(password)):
        if int(index) % 2 != 0:
            new_password += password[index]
    print(new_password)
    return new_password


def cut_function(index, length, password):
    substring = password[index:index + length]
    password = password.replace(substring, "", 1)
    print(password)
    return password


def substitute1(substring, substitute, password):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")
    return password


def while_function(password):
    command = input()
    while command != "Done":
        command = command.split()
        actions = command[0]
        if actions == "TakeOdd":
            password = take_odd(password)
        elif actions == "Cut":
            index = int(command[1])
            length = int(command[2])
            password = cut_function(index, length, password)
        elif actions == "Substitute":
            substring = command[1]
            substitute = command[2]
            password = substitute1(substring, substitute, password)
        command = input()
    return print(f"Your password is: {password}")


text = input()
while_function(text)
