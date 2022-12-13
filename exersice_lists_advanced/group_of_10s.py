# numbers = input()
# numbers_list = list(map(int, numbers.split(", ")))
#
# result = []
# boundary = 10
# while len(numbers_list) > 0:
#     group_list = []
#     min_number = min(numbers_list)
#     if min_number > boundary:
#         boundary += 10
#     for number in numbers_list:
#         if number in range(boundary - 9, boundary + 1):  # 1-10 -> 10's; 11-20 -> 20's
#             group_list.append(number)
#     for number in group_list:
#         numbers_list.remove(number)
#
#     result.append(f"Group of {boundary}'s: {group_list}")
# print(*result, sep="\n")


group_of_ten = input().split(", ")
lst_group_of_ten = [int(number) for number in group_of_ten]
result = []
boundary = 10
while len(lst_group_of_ten) > 0:
    group_list = []
    for num in lst_group_of_ten:
        if num <= boundary:
            group_list.append(num)
    for num in group_list:
        lst_group_of_ten.remove(num)
    result.append(f"Group of {boundary}'s: {group_list}")
    boundary += 10
print("\n".join(result))


