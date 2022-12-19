import re

text = input()
while text:
    matched = re.findall(r"\d+", text)
    if matched:
        print(" ".join(matched), end=" ")
    text = input()