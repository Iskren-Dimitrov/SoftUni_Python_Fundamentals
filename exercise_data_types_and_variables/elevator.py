import math
number_of_people = int(input())
capacity = int(input())
total = number_of_people / capacity
print(math.ceil(total))