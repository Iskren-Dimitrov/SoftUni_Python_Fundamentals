money_beggars = input().split(", ")
beggars = int(input())
final = []
money_beggars_integer = []
counter_of_index = 0
for element in money_beggars:
    money_beggars_integer.append(int(element))
while counter_of_index < beggars:
    sum_for_current_beggar = 0
    for elements in range(counter_of_index, len(money_beggars), beggars):
        sum_for_current_beggar += money_beggars_integer[elements]
    counter_of_index += 1
    final.append(sum_for_current_beggar)
print(final)