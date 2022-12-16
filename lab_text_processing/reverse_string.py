word = input()

while word != "end":
    reverse = ""
    current_word = word
    reverse += current_word[::-1]
    print(f"{word} = {reverse}")
    word = input()

word = input()

while word != "end":
    reverse = []
    current_word = word
    reverse += current_word[::-1]
    print(f"{word} = {''.join(reverse)}")
    word = input()

