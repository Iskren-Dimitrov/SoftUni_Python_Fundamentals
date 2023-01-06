sequence_integers = input().split()
integers = input()
count_shot_targets = 0
lst_sequence_integers = []
for numbers in sequence_integers:
    lst_sequence_integers.append(int(numbers))
while integers != "End":
    integers = int(integers)
    if integers < len(lst_sequence_integers):
        if lst_sequence_integers[integers] != - 1:
            current_target = lst_sequence_integers[integers]
            lst_sequence_integers[integers] = -1
            count_shot_targets += 1

            for target_index in range(len(lst_sequence_integers)):
                if lst_sequence_integers[target_index] != -1:
                    if lst_sequence_integers[target_index] > current_target:
                        lst_sequence_integers[target_index] -= current_target
                    else:
                        lst_sequence_integers[target_index] += current_target
    integers = input()

result = list(map(str, lst_sequence_integers))
result = " ".join(result)
print(f"Shot targets: {count_shot_targets} -> {result}")