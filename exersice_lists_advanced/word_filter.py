words = input().split()
word_filter = [word for word in words if len(word) % 2 == 0]
print(*word_filter, sep=" \n")
# print("\n".join(word_filter))