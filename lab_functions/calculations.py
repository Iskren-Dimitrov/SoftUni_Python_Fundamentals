def calculator(command, first_number, second_number):
    if command == "multiply":
        return first_number * second_number
    elif command == "divide":
        return int(first_number / second_number)
    elif command == "add":
        return first_number + second_number
    elif command == "subtract":
        return first_number - second_number


current_command = input()
current_first_number = int(input())
current_second_number = int(input())
print(calculator(current_command, current_first_number, current_second_number))