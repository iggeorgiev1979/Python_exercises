from re import findall


def find_numbers(text: str):
    pattern = r'\d+'
    return findall(pattern, text)


def replace_number(number: str, text: str):
    index = text.index(number)
    if not index + len(number) == len(text):
        text = text[:index] + text[index + len(number): index + len(number) + 1] + text[index + len(number):]
    return text


message = input()
numbers = find_numbers(message)
for el in numbers:
    message = replace_number(el, message)
print(message)
