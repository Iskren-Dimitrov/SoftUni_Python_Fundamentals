sequence_of_integers = input().split()
lst_sequence_of_integers = []
count = 0
for numbers in sequence_of_integers:
    lst_sequence_of_integers.append(int(numbers))
average_number = sum(lst_sequence_of_integers) // len(lst_sequence_of_integers)

lst_result = []
for greater_numbers in lst_sequence_of_integers:
    if greater_numbers > average_number:
        lst_result.append(greater_numbers)
        lst_result.sort(reverse=True)

if len(lst_result) == 0:
    print("No")
else:
    print(*lst_result[:5])
