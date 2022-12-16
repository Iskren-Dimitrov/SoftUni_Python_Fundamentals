text = input().split()
repeat_string = ""

for repeat in text:

    repeat_string += repeat * len(repeat)
print(repeat_string)