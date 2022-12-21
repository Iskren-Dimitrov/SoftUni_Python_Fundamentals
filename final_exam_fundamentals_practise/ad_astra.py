import re

text = input()

matches = re.findall(r"([\#|\|])([A-Za-z ]+)\1(\d{2}(\/)\d{2}(\/)\d{2})\1(\d{1,4})\1", text)
print_result = ""
calories = 0

if matches:
    for result in matches:
        print_result += f"Item: {result[1]}, Best before: {result[2]}, Nutrition: {int(result[5])}\n"
        calories += int(result[5])

number_of_days = calories // 2000

print(f"You have food to last you for: {number_of_days} days!")
print(f"{print_result}")
