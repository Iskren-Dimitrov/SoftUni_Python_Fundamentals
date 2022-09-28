number_lines = int(input())
sums = 0
for letters in range(1, number_lines + 1):
    letter = input()
    sums += ord(letter)
print(f"The sum equals: {sums}")