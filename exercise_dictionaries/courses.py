course = input()
dictionaries = {}

while course != "end":
    current_command = course.split(" : ")
    course_name = current_command[0]
    name = current_command[1]
    if course_name not in dictionaries.keys():
        dictionaries[course_name] = []
    dictionaries[course_name].append(name)
    course = input()

for course_name in dictionaries.keys():
    print(f"{course_name}: {len(dictionaries[course_name])}")
    for student in dictionaries[course_name]:
        print(f"-- {student}")
