# lst = ['a', 'o', 'u', 'e', 'i']
# text = input()
# final_list = []
#
# for ch in text:
#     if ch not in lst:
#         final_list.append(ch)
# print("".join(final_list))


# lst = ['a', 'o', 'u', 'e', 'i']
# text = input()
# final_list = [ch for ch in text if ch not in lst]
# print("".join(final_list))


# 1.	No Vowels

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = ''
for ch in text:
    if ch.lower() not in vowels:
        result += ch

print(result)
