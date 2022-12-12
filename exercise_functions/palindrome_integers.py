def palindrome_checker(current_integers):
    for number in current_integers:
        is_palindrome = number == number[::-1]
        print(is_palindrome)


current_integer = input().split(", ")
palindrome_checker(current_integer)

#
# def palindrome_checker(lst):
#     for num in lst:
#         is_palindrome = num == num[::-1]
#         print(is_palindrome)
#
#
# positive_ints = input().split(", ")
# palindrome_checker(positive_ints)