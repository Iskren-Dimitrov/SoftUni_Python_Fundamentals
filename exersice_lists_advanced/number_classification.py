numbers = input().split(", ")
lst_comprehension = [int(num) for num in numbers]
positive = []
negative = []
even = []
odd = []
for number in lst_comprehension:
    if number >= 0:
        positive.append(int(number))
    if number < 0:
        negative.append(int(number))
    if number % 2 == 0:
        even.append(int(number))
    if number % 2 != 0:
        odd.append(int(number))
print(f'Positive: {", ".join(str(positive) for positive in positive)}')
print(f'Negative: {", ".join(str(negative) for negative in negative)}')
print(f'Even: {", ".join(str(even) for even in even)}')
print(f'Odd: {", ".join(str(odd) for odd in odd)}')
