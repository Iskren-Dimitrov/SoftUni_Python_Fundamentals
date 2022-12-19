import re

text = input()

matched = re.findall(r"\s([a-z0-9]+[a-z0-9\._-]*@[a-z-]+\.[a-z]+\.?[A-Za-z]+)", text)

print("\n".join(matched))

