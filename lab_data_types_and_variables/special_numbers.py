number = int(input())
for all_numbers in range(1, number + 1):
    current_number_as_string = str(all_numbers)
    for digits, index in enumerate(current_number_as_string):
        if int(digits) + int(index) == 5 or int(digits) + int(index) == 7 or int(digits) + int(index) == 11:
            print(f"{current_number_as_string} -> True")
        else:
            print(f"{current_number_as_string} -> False")

