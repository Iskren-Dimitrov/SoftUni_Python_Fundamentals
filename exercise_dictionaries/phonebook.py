phonebook = input()
dictionaries = {}

while len(phonebook) > 1:
    name, phone = phonebook.split("-")
    dictionaries[name] = phone
    phonebook = input()

for key in range(int(phonebook)):
    name = input()
    if name in dictionaries.keys():
        print(f"{name} -> {dictionaries[name]}")
    else:
        print(f"Contact {name} does not exist.")
