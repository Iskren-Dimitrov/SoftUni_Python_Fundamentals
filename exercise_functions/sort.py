# def sort_numbers(current_numbers):
#     sort = sorted(current_numbers)
#     return sort
#
#
# sort_num = input().split()
# lst = []
# for element in sort_num:
#     lst.append(int(element))
#     my_list = sorted(lst)
# print(my_list)

#
# def sort_numbers(current_numbers):
#     sort = sorted(current_numbers)
#
# numbers = input().split()
# sorted_numbers = []
# for element in numbers:
#     sort_numbers(int(element))
#     sorted_numbers.append(int(element))
# print(sorted_numbers)


def sort(numbers):
    lst = []
    for current_number in numbers:
        lst.append(int(current_number))
    return lst


current_numbers_as_string = input().split()
print(sorted(sort(current_numbers_as_string)))