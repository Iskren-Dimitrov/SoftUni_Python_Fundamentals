# employees_happiness = input().split(" ")
# happiness_factor = int(input())
# multiply_list = []
# filtered_list = []
# lst = []
# sums_multiply_list = 0
# for employees in employees_happiness:
#     multiply_list.append(int(employees) * happiness_factor)
# for filtered in employees_happiness:
#     sums_multiply_list += int(filtered)
# count = 1
# for averaged in multiply_list:
#     average = sums_multiply_list // len(multiply_list)
#     if count <= average:
#         lst.append(averaged)
#     count += 1


happiness_list = list(map(int, input().split()))
factor = int(input())
happiness_list = [number * factor for number in happiness_list]
average_happiness = sum(happiness_list) / len(happiness_list)


def happy_employees(happiness):
    if happiness >= average_happiness:
        return True
    return False


# happy_employees_list = [happy_employees(employee) for employee in happiness_list]  # returns a list of [True, False]
# happy_employees_count = happy_employees_list.count(True)  # calculates the count of happy employees.

happy_employees_list = list(filter(happy_employees, happiness_list))  # returns a list of the happy employees.

if len(happy_employees_list) >= len(happiness_list) / 2:
    print(f"Score: {len(happy_employees_list)}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees_list)}/{len(happiness_list)}. Employees are not happy!")