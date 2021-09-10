import re


def extract(text: str):
    pattern = r'(\||#)(?P<name>[A-Za-z\s]+)\1(?P<date>[\d]{2}/[\d]{2}/[\d]{2})\1(?P<calories>[\d]+)\1'
    result = re.finditer(pattern, text)
    result_dicts = [x.groupdict() for x in result]
    return result_dicts


def calculate(dicts: list):
    total_calories = 0
    for el in dicts:
        total_calories += int(el['calories'])
    return total_calories // 2000


input_text = input()

products = extract(input_text)
days = calculate(products)
print(f"You have food to last you for: {days} days!")
for el in products:
    print(f"Item: {el['name']}, Best before: {el['date']}, Nutrition: {el['calories']}")
