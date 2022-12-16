string = input()
result = ""
count = 0

for index in range(len(string)):
    if count > 0 and string[index] != ">":
        count -= 1
    elif string[index] == ">":
        result += string[index]
        count += int(string[index + 1])
    elif string[index].isalpha():
        result += string[index]
print(result)


