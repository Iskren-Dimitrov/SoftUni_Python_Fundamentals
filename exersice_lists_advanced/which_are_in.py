first_sequences = input().split(", ")
second_sequences = input().split(", ")
only_the_strings_in_first_sequences = []

for first_word in first_sequences:
    for second_word in second_sequences:
        if first_word in second_word:
            only_the_strings_in_first_sequences.append(first_word)
            break
print(only_the_strings_in_first_sequences)