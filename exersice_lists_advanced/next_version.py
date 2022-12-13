# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9:
#         version[index] = 0
#         if index - 1 >= 0:
#             version[index - 1] += 1
# print('.'.join(str(number) for number in version))


version = input().split(".")
lst_version = []
for numbers in version:
    lst_version.append(int(numbers))
lst_version[-1] += 1
for index in range(len(lst_version) - 1, -1, -1):
    if lst_version[index] > 9:
        lst_version[index] = 0
        if index - 1 >= 0:
            lst_version[index - 1] += 1
print(*lst_version, sep=".")
