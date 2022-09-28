first_number = int(input())
second_number = int(input())
for current_number in range(second_number, first_number, -1):
    if current_number % first_number == 0:
        break
print(current_number)
