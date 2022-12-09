number_of_lines = int(input())
water_capacity = 255
litters_count = 0
for liters_of_water in range(number_of_lines):
    current_litres = int(input())
    if water_capacity - current_litres < 0:
        print("Insufficient capacity!")
        continue
    water_capacity -= current_litres
    litters_count += current_litres
print(litters_count)
