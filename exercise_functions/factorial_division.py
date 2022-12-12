def factorial_division(number):
    for curr_number in range(1, number):
        number = number * curr_number
    return number


current_number = int(input())
second_number = int(input())
current_number_factorial = factorial_division(current_number)
second_number_factorial = factorial_division(second_number)
final = current_number_factorial // second_number_factorial
print(f"{final:.2f}")



# n = 5
#
# fact = 1
#
# for i in range(1, n + 1):
#     fact = fact * i
#
# print("The factorial of 23 is : ", end="")
# print(fact)