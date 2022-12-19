import re

text = input()
searched_word = input()
pattern = fr"{searched_word}"
matched = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(matched))


# import re
#
# text = input()
# searched_word = input()
# matched = re.findall(fr"\b{searched_word}\b", text, flags=re.IGNORECASE)
# print(len(matched))
#
#
