product_and_quantity = input().split(" ")
products = input().split(" ")
items = {}

for index in range(0, len(product_and_quantity), 2):
    key = product_and_quantity[index]
    value = product_and_quantity[index + 1]
    items[key] = value
for product in products:
    if product in items.keys():
        quantity = items[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")