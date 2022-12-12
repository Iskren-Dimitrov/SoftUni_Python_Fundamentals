def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    if number < 100:
        curr_number = f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading..."
        return curr_number


current_number = int(input())
print(loading_bar(current_number))