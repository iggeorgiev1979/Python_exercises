import re


def validate(text: str):
    # pattern = r"(@#+)(?P<barcode>[A-Z][A-Za-z0-9]+[A-Z])\1"
    pattern = r"(@#+)(?P<barcode>[A-Z][A-Za-z0-9]+[A-Z])(@#+)"
    match = re.findall(pattern, text)
    if len(match) > 0 and len(match[0][1]) >= 6:
        return match[0][1]
    return None


def find_group(text: str):
    pattern = r"\d"
    digits = re.findall(pattern, text)
    group = ''
    for el in digits:
        group += el
    if group:
        return group
    return '00'


n = int(input())
for _ in range(n):
    barcode = validate(input())
    if barcode:
        barcode_group = find_group(barcode)
        print(f'Product group: {barcode_group}')
    else:
        print('Invalid barcode')
