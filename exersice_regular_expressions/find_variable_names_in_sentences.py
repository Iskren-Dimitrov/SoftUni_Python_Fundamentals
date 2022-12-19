import re

text = input()

matched = re.finditer(r"(\b_)(?P<word>[A-Za-z0-9]+)(\b)", text)
output = []
for match in matched:
    word = match.group("word")
    output.append(word)
print(",".join(output))
