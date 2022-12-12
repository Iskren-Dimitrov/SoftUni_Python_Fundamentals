def even_numbers(numbers):
    lst = []
    final = []
    for element in numbers:
        lst.append(int(element))
    for element2 in lst:
        if element2 % 2 == 0:
            final.append(element2)
    return final


current_numbers_as_string = input().split()
print(even_numbers(current_numbers_as_string))
