products = input()
dictionaries = {}
count = {}

while products != "buy":
    current_products = products.split()
    key = current_products[0]
    price = float(current_products[1])
    quantity = current_products[2]
    if key not in dictionaries.keys():
        dictionaries[key] = 0
        count[key] = 0
    dictionaries[key] += int(quantity)
    count[key] = price
    products = input()
for product in dictionaries.keys():
    total_product = dictionaries[product] * count[product]
    print(f"{product} -> {total_product:.2f}")


# prices = {}
# quantities = {}
# command = input().split()
# while "buy" not in command:
#     current_product = command[0]
#     current_price = float(command[1])
#     current_quantity = int(command[2])
#     prices[current_product] = current_price
#     if current_product not in quantities:
#         quantities[current_product] = 0
#     quantities[current_product] += current_quantity
#     command = input().split()
# for product in prices:
#     total_price = prices[product] * quantities[product]
#     print(f"{product} -> {total_price:.2f}")
