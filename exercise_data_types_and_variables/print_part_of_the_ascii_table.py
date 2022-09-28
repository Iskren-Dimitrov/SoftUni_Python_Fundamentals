first_number = int(input())
second_number = int(input())
sums = 0
for character in range(first_number, second_number + 1):
    current_number = chr(character)
    print(current_number, end=" ")
