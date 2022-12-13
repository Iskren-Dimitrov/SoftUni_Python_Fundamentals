number_of_electrons = int(input())
lst_number_of_electrons = []
lst_2 = []
for electrons in range(1, number_of_electrons + 1):
    lst_number_of_electrons.append(2 * electrons ** 2)
for element in lst_number_of_electrons:
    if number_of_electrons > element:
        lst_2.append(element)
        number_of_electrons -= element
    else:
        lst_2.append(number_of_electrons)
        break
print(lst_2)
