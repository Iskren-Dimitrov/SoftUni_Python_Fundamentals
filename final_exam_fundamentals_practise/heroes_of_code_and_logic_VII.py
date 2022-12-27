heroes_count = int(input())
heroes_dictionaries = {}

for heroes in range(heroes_count):
    command = input().split()
    hero_name = command[0]
    hp = int(command[1])
    mp = int(command[2])
    heroes_dictionaries[hero_name] = [hp, mp]
command_while = input()
while command_while != "End":
    current_command = command_while.split(" - ")
    actions = current_command[0]
    if actions == "CastSpell":
        hero_name1 = current_command[1]
        mp_needed = int(current_command[2])
        spell_name = current_command[3]
        if heroes_dictionaries[hero_name1][1] >= mp_needed:
            heroes_dictionaries[hero_name1][1] -= mp_needed

            print(f"{hero_name1} has successfully cast {spell_name} and now has {heroes_dictionaries[hero_name1][1]} MP!")
        else:
            print(f"{hero_name1} does not have enough MP to cast {spell_name}!")

    elif actions == "TakeDamage":
        hero_name2 = current_command[1]
        damage = int(current_command[2])
        attacker = current_command[3]
        if heroes_dictionaries[hero_name2][0] - damage > 0:
            heroes_dictionaries[hero_name2][0] -= damage
            print(f"{hero_name2} was hit for {damage} HP by {attacker} and now has {heroes_dictionaries[hero_name2][0]} HP left!")
        else:
            del heroes_dictionaries[hero_name2]
            print(f"{hero_name2} has been killed by {attacker}!")
    elif actions == "Recharge":
        hero_name3 = current_command[1]
        amount = int(current_command[2])
        if heroes_dictionaries[hero_name3][1] + amount > 200:
            amount = 200 - heroes_dictionaries[hero_name3][1]
            heroes_dictionaries[hero_name3][1] += amount
        else:
            heroes_dictionaries[hero_name3][1] += amount
        print(f"{hero_name3} recharged for {amount} MP!")
    elif actions == "Heal":
        hero_name4 = current_command[1]
        amount2 = int(current_command[2])
        if heroes_dictionaries[hero_name4][0] + amount2 > 100:
            amount2 = 100 - heroes_dictionaries[hero_name4][0]
            heroes_dictionaries[hero_name4][0] += amount2
        else:
            heroes_dictionaries[hero_name4][0] += amount2
        print(f"{hero_name4} healed for {amount2} HP!")
    command_while = input()
print_result = ''
for result in heroes_dictionaries.keys():
    print_result += f'{result}\n  HP: {heroes_dictionaries[result][0]}\n  MP: {heroes_dictionaries[result][1]}\n'
print(print_result)
