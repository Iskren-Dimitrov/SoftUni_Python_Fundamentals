sequence_of_elements = input().split()
indexes = input()
count_moves = 0
while indexes != "end":
    first_index = int(indexes.split()[0])
    second_index = int(indexes.split()[1])
    count_moves += 1
    if first_index < 0 or second_index < 0 or first_index == second_index or first_index >= len(sequence_of_elements) \
            or second_index >= len(sequence_of_elements):
        middle_of_the_sequence = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_of_the_sequence, f"-{count_moves}a")
        sequence_of_elements.insert(middle_of_the_sequence + 1, f"-{count_moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        deleted_elements = sequence_of_elements[first_index]
        x = sequence_of_elements.pop(first_index)
        sequence_of_elements.remove(x)
        print(f"Congrats! You have found matching elements - {deleted_elements}!")
    elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {count_moves} turns!")
        break
    indexes = input()
if indexes == "end":
    print("Sorry you lose :(")
    print(f"{' '.join(sequence_of_elements)}")




