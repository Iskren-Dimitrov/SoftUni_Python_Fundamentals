companions = int(input())
days = int(input())
coins = 0
for current_number in range(1, days + 1):
    if current_number % 10 == 0:
        companions -= 2
    if current_number % 15 == 0:
        companions += 5
    if current_number % 3 == 0:
        coins -= 3 * companions
    if current_number % 5 == 0:
        coins += 20 * companions
        if current_number % 3 == 0:
            coins -= 2 * companions

    coins += 50
    coins -= 2 * companions
each_companion = int(coins/companions)
print(f"{companions} companions received {each_companion} coins each.")