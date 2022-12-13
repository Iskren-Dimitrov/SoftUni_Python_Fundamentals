number_of_wagons = int(input())
train = [0 for number in range(number_of_wagons)]

command = input()
while command != "End":
    explode = command.split(" ")
    current = explode[0]
    if current == "add":
        number_of_people = int(explode[1])
        train[-1] += number_of_people
    if current == "insert":
        position = int(explode[1])
        number_of_people = int(explode[2])
        train[position] += number_of_people
    if current == "leave":
        position = int(explode[1])
        number_of_people = int(explode[2])
        train[position] -= number_of_people
    command = input()
print(train)

# number = int(input())
# wagons = [0] * number
# command = input()
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     split_command = command.split(' ')  # insert 0 15
#     current_command = split_command[0]
#
#     if current_command == 'add':
#         people_to_add = int(split_command[1])
#         wagons[-1] += people_to_add
#
#     elif current_command == 'insert':
#         index = int(split_command[1])  # insert 0 15
#         number_of_people = int(split_command[2])
#         wagons[index] += number_of_people
#
#     elif current_command == 'leave':
#         index = int(split_command[1])
#         people_to_leave = int(split_command[2])
#         wagons[index] -= people_to_leave
#
# print(wagons)