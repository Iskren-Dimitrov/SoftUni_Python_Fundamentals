def orders(command, quantity):
    if command == "coffee":
        return quantity * 1.50
    elif command == "water":
        return quantity * 1.00
    elif command == "coke":
        return quantity * 1.40
    elif command == "snacks":
        return quantity * 2.00


current_command = input()
current_quantity = int(input())
final_price = orders(current_command, current_quantity)
print(f"{final_price:.2f}")