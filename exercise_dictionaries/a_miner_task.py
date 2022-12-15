command = input()
miner_task = {}

while command != "stop":
    current_command = command
    current_quantity = int(input())
    if current_command not in miner_task.keys():
        miner_task[current_command] = 0
    miner_task[current_command] += current_quantity
    command = input()
for resource, quantity in miner_task.items():
    print(f"{resource} -> {quantity}")