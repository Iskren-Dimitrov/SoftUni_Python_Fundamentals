import re

text = input()

matches = re.finditer(
    r"(?P<phone_code_Bulgaria>\+359)(?P<separator>[- ])(?P<phone_code_Sofia>2)(?P=separator)(?P<three_digits>\d{3})("
    r"?P=separator)(?P<four_digits>\d{4}\b)",
    text)

output = []
for match in matches:
    output.append(match.group())
print(", ".join(output))
