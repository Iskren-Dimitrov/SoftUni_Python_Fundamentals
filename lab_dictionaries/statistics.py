products = {}

command = input()

while command != "statistics":
    key, value = command.split(": ")
    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)
    command = input()
print("Products in stock:")

for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(int(s) for s in products.values())}")