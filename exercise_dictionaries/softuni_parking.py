count = int(input())
dictionaries = {}

for users in range(count):
    user = input().split()
    registration = user[0]
    if registration == "register":
        name = user[1]
        license_plate = user[2]
        if name not in dictionaries.keys():
            dictionaries[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif registration == "unregister":
        name = user[1]
        if name not in dictionaries.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del dictionaries[name]

for username, license_plate_number in dictionaries.items():
    print(f"{username} => {license_plate_number}")