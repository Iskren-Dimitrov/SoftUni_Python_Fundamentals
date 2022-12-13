# numbers = list(map(int, input().split(', ')))
# indices = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
# print(indices)


numbers = input().split(", ")
lst_numbers = []
even_index = []
for number in numbers:
    lst_numbers.append(int(number))
for digit, index in enumerate(lst_numbers):
    if index % 2 == 0:
        even_index.append(digit)
print(even_index)