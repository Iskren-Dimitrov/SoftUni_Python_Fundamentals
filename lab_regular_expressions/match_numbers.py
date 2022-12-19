import re

text = input()

matched = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(.[0-9]+)?($|(?=\s))", text)
output = []

for match in matched:
    output.append(match.group())

print(" ".join(output))