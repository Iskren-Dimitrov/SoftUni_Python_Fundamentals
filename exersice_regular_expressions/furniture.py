import re

output_furniture = []
total = 0
text = input()
while text != "Purchase":
    matched = re.finditer(r"(>>)(?P<furniture_name>[A-Za-z]+)(<<)(?P<price>\d+\.?\d+)(!)(?P<quantity>\d+)", text)

    for match in matched:
        furniture1 = match.group("furniture_name")
        price = match.group("price")
        quantity = match.group("quantity")
        output_furniture.append(furniture1)
        total += float(price) * int(quantity)
    text = input()
print("Bought furniture:")
for name in output_furniture:
    print(f"{name}")
print(f"Total money spend: {total:.2f}")


# import re
#
# output_furniture = []
# price_quantity = []
# total = 0
# text = input()
# while text != "Purchase":
#     matched = re.finditer(r"(>>)(?P<furniture_name>[A-Za-z]+)(<<)(?P<price>\d+\.?\d+)(!)(?P<quantity>\d+)", text)
#
#     for match in matched:
#         output_furniture.append(match.group("furniture_name"))
#         price_quantity.append(match.group("price"))
#         price_quantity.append(match.group("quantity"))
#     text = input()
# print("Bought furniture:")
# for name in output_furniture:
#     print(f"{name}")
# for calculation in range(0, len(price_quantity), 2):
#     price = float(price_quantity[calculation])
#     quantity = int(price_quantity[calculation + 1])
#     total += price * quantity
# print(f"Total money spend: {total:.2f}")