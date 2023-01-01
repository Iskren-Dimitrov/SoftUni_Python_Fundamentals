price = input()
current_command = 0

while price != "special" and price != "regular":
    command = float(price)
    if command < 0:
        print("Invalid price!")
    elif command > 0:
        current_command += command
    price = input()
if current_command <= 0:
    print("Invalid order!")

else:
    taxes = current_command * 0.2
    final_price = current_command + taxes

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {current_command:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if price == "special":
        final_price *= 0.9
    print(f"Total price: {final_price:.2f}$")