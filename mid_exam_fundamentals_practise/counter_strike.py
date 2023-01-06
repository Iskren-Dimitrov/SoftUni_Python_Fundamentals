initial_energy = int(input())
distance = input()
count_won_battles = 0
current_energy = initial_energy
while distance != "End of battle":

    if current_energy >= int(distance):
        count_won_battles += 1
        current_energy -= int(distance)
        if count_won_battles % 3 == 0:
            current_energy += count_won_battles
    else:
        print(f"Not enough energy! Game ends with {count_won_battles} won battles and {current_energy} energy")
        break
    distance = input()
if distance == "End of battle":
    print(f"Won battles: {count_won_battles}. Energy left: {current_energy}")

