numbers_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowballs in range(numbers_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    quality_time = int(input())
    total = (snowball_weight / snowball_time) ** quality_time
    if total > max_value:
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = quality_time
        max_value = total
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")

