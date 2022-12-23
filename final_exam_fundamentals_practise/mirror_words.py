import re


text = input()

matches = re.findall(r"([@#])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)", text)
count = 0
mirrors = []
for match in matches:
    if match[1] == match[3][::-1]:
        mirrors.append(f"{match[1]} <=> {match[3]}")
    count += 1

if count > 0:

    print(f'{count} word pairs found!')

    if not mirrors:

        print('No mirror words!')

    else:

        print('The mirror words are:')

        print(', '.join(mirrors))


else:

    print('No word pairs found!')

    print('No mirror words!')