numbers = input().split(" ")
split_list = list()

for split_numbers in numbers:
    split_list.append(abs(float(split_numbers)))
print(split_list)

