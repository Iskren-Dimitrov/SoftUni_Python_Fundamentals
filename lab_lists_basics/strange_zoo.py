
my_list = []

for string in range(1, 3 + 1):
    data = input()
    my_list.append(data)
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)

