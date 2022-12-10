number_in_lines = int(input())
positive_number = []
negative_number = []
positive_count = 0
negative_count = 0
for numbers in range(number_in_lines):
    current_number = int(input())
    if current_number >= 0:
        positive_number.append(current_number)
        positive_count += 1
    else:
        negative_number.append(current_number)
        negative_count += current_number
print(positive_number)
print(negative_number)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_count}")