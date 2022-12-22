import re

text = input()

matched = re.findall(r"([=|\/])([A-Z][A-Za-z]{2,})\1", text)
result = []
numbers = []
if matched:
    for match in matched:
        result.append(match[1])
        numbers.append(len(match[1]))

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {sum(numbers)}")