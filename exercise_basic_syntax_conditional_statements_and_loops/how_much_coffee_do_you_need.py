command = input()
coffee_count = 0
while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_count += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_count += 2
    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)