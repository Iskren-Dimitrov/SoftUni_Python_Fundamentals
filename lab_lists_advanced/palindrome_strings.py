# def palindrome_filtered(word):
#     if word == word[::-1]:
#         return word
#
#
# words = input().split(' ')
# palindrome = input()
#
# palindrome_list = [word for word in words if palindrome_filtered(word)]
# palindrome_counter = palindrome_list.count(palindrome)
#
# print(palindrome_list)
# print(f'Found palindrome {palindrome_counter} times')
#

words = input().split(" ")
palindrome = input()
lst_palindrome = []
lst_palindrome1 = []

for word in words:
    lst_palindrome.append(word)
for word1 in lst_palindrome:
    if word1 == word1[::-1]:
        lst_palindrome1.append(word1)
palindrome_counter = lst_palindrome1.count(palindrome)
print(lst_palindrome1)
print(f"Found palindrome {palindrome_counter} times")

