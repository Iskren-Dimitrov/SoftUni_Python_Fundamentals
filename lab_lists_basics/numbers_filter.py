number_filter = int(input())
numbers = []
command_even = "even"
command_odd = "odd"
command_negative = "negative"
command_positive = "positive"

for these_numbers in range(number_filter):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []
for number in numbers:
    filtered_passes = (
        (command == command_even and number % 2 == 0) or
        (command == command_odd and number % 2 != 0) or
        (command == command_negative and number < 0) or
        (command == command_positive and number >= 0)
    )
    if filtered_passes:
        filtered_numbers.append(number)
print(filtered_numbers)