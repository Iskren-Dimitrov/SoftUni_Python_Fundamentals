lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
expense = 0
for expenses in range(1, lost_fight_count + 1):
    if expenses % 2 == 0:
        expense += helmet_price
    if expenses % 3 == 0:
        expense += sword_price
        if expenses % 2 == 0:
            expense += shield_price
    if expenses % 12 == 0:
        expense += armour_price
print(f"Gladiator expenses: {expense:.2f} aureus")