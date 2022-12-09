year = int(input())

while True:
    counter_index = 0
    counter_digits = 0
    year += 1
    year_as_string = str(year)
    for digit in year_as_string[0]:
        for digit1 in year_as_string[1:4]:
            if digit in digit1:
                counter_digits += 1
    for digit in year_as_string[1]:
        for digit1 in year_as_string[2:4]:
            if digit in digit1:
                counter_digits += 1
    for digit in year_as_string[2]:
        for digit1 in year_as_string[3:4]:
            if digit in digit1:
                counter_digits += 1
    if counter_digits == 0:
        print(year_as_string)
        break


# year = int(input())
# year_is_happy = False
# counter = 0
# counter_digits = 0
# while not year_is_happy:
#     year += 1
#     year_as_string = str(year)
#     for digit in year_as_string:
#         new_year = (year_as_string[(counter + 1):])
#         if digit in new_year:
#             counter = 0
#             break
#         else:
#             counter_digits += 1
#         counter += 1
#     if counter_digits == len(year_as_string):
#         year_is_happy = True
#         break
#     else:
#         counter_digits = 0
# print(year)
