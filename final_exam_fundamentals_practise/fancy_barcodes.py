import re

count_fancy_barcodes = int(input())

for fancy_barcodes in range(count_fancy_barcodes):
    text = input()
    matches = re.findall(r"(@[#]+)([A-Z][A-Za-z0-9]{4,}([A-Z]))(@[#]+)", text)
    if matches:
        digits = []
        for match in matches:
            result = match[1]
            for letters in result:
                if letters.isdigit():
                    digits += letters
        if len(digits) > 0:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: {'00'}")

    else:
        print("Invalid barcode")