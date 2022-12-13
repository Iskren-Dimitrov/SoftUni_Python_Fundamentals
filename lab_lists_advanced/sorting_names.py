names = input().split(", ")
sorted_list = []
for sort in names:
    sorted_list = sorted(names)
current = sorted(sorted_list, key=len, reverse=True)
print(current)


#
# names = input().split(', ')
# result = sorted(names, key=lambda item: (-len(item), item))
# print(result)