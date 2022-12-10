numbers = int(input())
without_filter = []
command = input()
for integers in range(numbers):
    current_command = input()
    without_filter.append(current_command)
print(without_filter)
for string in range(len(without_filter) - 1, - 1, -1):
    current_string = without_filter[string]
    if command not in current_string:
        without_filter.remove(current_string)
print(without_filter)