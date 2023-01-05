receptionist = 3
employee_efficiency = []
for employee in range(receptionist):
    command = int(input())
    employee_efficiency.append(command)
all_employee_efficiency = sum(employee_efficiency)
students_count = int(input())
students_left = students_count
hours = 0

while students_left > 0:
    hours += 1

    if hours > 0 and hours % 4 == 0:
        continue

    students_left -= all_employee_efficiency
print(f"Time needed: {hours}h.")