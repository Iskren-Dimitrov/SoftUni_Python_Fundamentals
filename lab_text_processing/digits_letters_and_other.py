some_text = input()
digits = ""
letters = ""
characters = ""
for elements in some_text:

    if elements.isdigit():
        digits += elements
    elif elements.isalpha():
        letters += elements
    else:
        characters += elements
print(digits)
print(letters)
print(characters)


some_text = input()
digits = []
letters = []
characters = []
for elements in some_text:

    if elements.isdigit():
        digits.append(elements)
    elif elements.isalpha():
        letters.append(elements)
    else:
        characters.append(elements)
print("".join(digits))
print("".join(letters))
print("".join(characters))