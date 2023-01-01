people_waiting_to_get_on_the_lift = int(input())
current_state_of_the_lift = input().split()
empty_spots_for_the_wagon = 0
wagon_capacity = 4
wagons = []

for people_in_wagons in current_state_of_the_lift:
    wagons.append(int(people_in_wagons))
    empty_spots_for_the_wagon += 4

for index in range(len(wagons)):
    if people_waiting_to_get_on_the_lift < wagon_capacity:
        empty_spots = wagon_capacity - wagons[index]
        if empty_spots == people_waiting_to_get_on_the_lift:
            wagons[index] += empty_spots
        else:
            wagons[index] += people_waiting_to_get_on_the_lift
        people_waiting_to_get_on_the_lift -= empty_spots
        break
    else:
        people_in_wagon = wagons[index]
        empty_wagons = wagon_capacity - people_in_wagon
        wagons[index] += empty_wagons
        people_waiting_to_get_on_the_lift -= empty_wagons

wagons_result = 0
for result in range(len(wagons)):

    wagons_result += wagons[result]
if people_waiting_to_get_on_the_lift == 0 and empty_spots_for_the_wagon > wagons_result:

    print("The lift has empty spots!")
    print(*wagons, sep=' ')

elif people_waiting_to_get_on_the_lift > 0 and empty_spots_for_the_wagon == wagons_result:
    print(f"There isn't enough space! {people_waiting_to_get_on_the_lift} people in a queue!")
    print(*wagons, sep=' ')
















