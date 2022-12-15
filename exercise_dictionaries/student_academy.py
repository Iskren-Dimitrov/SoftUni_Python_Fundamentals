student_count = int(input())
dictionaries = {}
average_grade = 4.5

for students in range(student_count):
    current_student = input()
    current_grade = float(input())
    if current_student not in dictionaries.keys():
        dictionaries[current_student] = []
    dictionaries[current_student].append(current_grade)

for name in dictionaries.keys():
    total_sum = sum(dictionaries[name])
    total_average = total_sum / len(dictionaries[name])
    if total_average >= average_grade:
        print(f"{name} -> {total_average:.2f}")

