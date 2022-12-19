import re

text = input()

matches = re.finditer(r"(?P<first_name>\b[A-Z][a-z]+)(?P<separator>[ ])(?P<second_name>[A-Z][a-z]+\b)", text)
output = []
for match in matches:
    output.append(match.group())
print(" ".join(output))

