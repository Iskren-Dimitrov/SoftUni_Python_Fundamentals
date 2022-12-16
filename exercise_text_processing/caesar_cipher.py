text = input()
encrypted = ""

for word in text:
    encrypted += chr(ord(word) + 3)
print(encrypted)


