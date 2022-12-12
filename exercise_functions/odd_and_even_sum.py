def odd_and_even_sum(number):
    sum_odd = 0
    sum_even = 0
    for numbers in number:
        if int(numbers) % 2 == 0:
            sum_even += int(numbers)
        else:
            sum_odd += int(numbers)
    return sum_odd, sum_even


current_number = input()
sum_odd, sum_even = odd_and_even_sum(current_number)
print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


# def even_and_odd_numbers(number):
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#     for digit in number:
#         if int(digit) % 2 == 0:  # digit is even
#             sum_of_even_digits += int(digit)
#         else:  # digit is odd
#             sum_of_odd_digits += int(digit)
#     return sum_of_odd_digits, sum_of_even_digits
#
#
# number_as_string = input()
# sum_of_odd_digits, sum_of_even_digits = even_and_odd_numbers(number_as_string)
# print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")