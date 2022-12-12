def perfect_number(number):
    sum_number = 0
    is_perfect = True
    for curr_number in range(1, number):
        if number % curr_number == 0:
            sum_number += curr_number
    if sum_number == number:
        return is_perfect
    is_perfect = False
    print("It's not so perfect.")


current_number = int(input())
number_is_perfect = perfect_number(current_number)
if number_is_perfect:
    print("We have a perfect number!")










# def is_perfect(some_number):
#     sum = 0
#     for divisor in range(1, some_number):
#         if some_number % divisor == 0:
#             sum += divisor
#     if sum == some_number:
#         return "We have a perfect number!"
#     return "It's not so perfect."
#
#
# number = int(input())
# print(is_perfect(number))