import re

text = input()
digits = []
for digit in range(len(text)):
    if text[digit].isdigit():
        digits += text[digit]
cool_threshold = 1
for di in digits:
    cool_threshold *= int(di)
matches = re.findall(r"(\*\*|\:\:)([A-Z]{1}[a-z]{2,})(\1)", text)
cool = []
if matches:

    count_emojis = 0
    for match in matches:
        sums = 0
        count_emojis += 1
        result = match[1]
        for asci in range(len(result)):
            if result[asci].isalpha:
                sums += ord(result[asci])

        if sums > cool_threshold:
            cool.append(''.join(match))

    print(f"Cool threshold: {cool_threshold}")
    print(f"{count_emojis} emojis found in the text. The cool ones are:")
    for emoji in cool:
        print(f"{emoji}")