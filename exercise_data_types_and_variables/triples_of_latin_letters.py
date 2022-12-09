number = int(input())
for latin_letters in range(0, number):
    for latin_letters2 in range(0, number):
        for latin_letters3 in range(0, number):
            print(f"{chr(97 + latin_letters)}{chr(97 + latin_letters2)}{chr(97 + latin_letters3)}")