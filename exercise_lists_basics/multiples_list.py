factor = int(input())
count = int(input())
multiples_list = []
for element in range(1, count + 1):
    multiples_list.append(element * factor)
print(multiples_list)