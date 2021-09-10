import re

pattern = r"%(?P<name>[A-z][a-z]+)%([^\|\$\%\.]?)+<(?P<product>\w+)>([^\|\$\%\.]?)+\|(?P<count>\d+)\|([^\|\$\%\.0-9]?)+(?P<price>\d+\.?\d+)\$"
total_income = 0
text = input()

while not text == 'end of shift':
    match = re.match(pattern, text)
    if match:
        x = match.groupdict()
        print(f"{x['name']}: {x['product']} - {int(x['count']) * float(x['price']):.2f}")
        total_income += int(x['count']) * float(x['price'])

    text = input()
print(f'Total income: {total_income:.2f}')
