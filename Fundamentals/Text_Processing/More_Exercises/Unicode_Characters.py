def convert(symbol: str):
    el = hex(ord(symbol))
    return el[-2:]


text = input()
for i in text:
    print(f'\\u00{convert(i)}', end='')
print()
