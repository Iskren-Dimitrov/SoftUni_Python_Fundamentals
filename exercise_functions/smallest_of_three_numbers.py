def function_smallest_of_the_three_numbers(numbers):
    min_number = min(numbers)
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
all_number = [first_number, second_number, third_number]
print(function_smallest_of_the_three_numbers(all_number))
