numbers = input().split()
count_of_remove = int(input())
int1 = []
for element in numbers:
    int1.append(int(element))
for element2 in range(count_of_remove):
    min_number = min(int1)
    int1.remove(min_number)
print(*int1, sep=", """)


# numbers_str = input().split()
# numbers = []
#
# for num in numbers_str:
#     numbers.append(int(num))
#
# remover = int(input())
#
# for _ in range(remover):
#     numbers.remove(min(numbers))
#
# print(*numbers, sep=", ")