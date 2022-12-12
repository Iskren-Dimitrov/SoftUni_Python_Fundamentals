# def min_max_sum(numbers):
#     min_number = min(numbers)
#     max_number = max(numbers)
#     sum_number = sum(numbers)
#     return min_number, max_number, sum_number
#
#
# current_numbers = input().split()
# lst = []
# lst1 = []
# lst2 = []
# for elements in current_numbers:
#     lst.append(int(elements))
#     lst1.append(int(elements))
#     lst2.append(int(elements))
# for element2 in range(1, len(lst)):
#     max1 = max(lst)
#     lst.remove(max1)
# for element3 in range(1, len(lst1)):
#     min1 = min(lst1)
#     lst1.remove(min1)
# sum1 = sum(lst2)
#
# first = f"The maximum number is"
# second = f"The minimum number is"
# print(second, *lst)
# print(first, *lst1)
# print(f"The sum number is: {sum1}")
#

def min_max_sum(numbers):
    lst = []
    for current_number in numbers:
        lst.append(int(current_number))
    return lst


current_numbers_as_string = input().split()
result = min_max_sum(current_numbers_as_string)
print(f"The minimum number is {min(result)}")
print(f"The maximum number is {max(result)}")
print(f"The sum number is: {sum(result)}")