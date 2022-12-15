string = input().split()
str = ''.join(string)
dictionaries = {}

for elements in str:
    if elements not in dictionaries.keys():
        dictionaries[elements] = 0
    dictionaries[elements] += 1
for char, occurrences in dictionaries.items():
    print(f"{char} -> {occurrences}")
