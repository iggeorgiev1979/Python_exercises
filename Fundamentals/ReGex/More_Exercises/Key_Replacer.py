import re


def find_keys(text: str):
    pattern = r'(^[A-Za-z]+)(?:\||\<|\\)(?:.+)?(?:\||\<|\\)([A-Za-z]+$)'
    result = re.findall(pattern, text)
    return result[0]


def find_text(text: str, keys: list):
    start, end = keys
    pattern = rf'(?:{start})(.*?)(?:{end})'
    result = re.findall(pattern, text)
    return ''.join(result)


key_str = input()
message = input()
start_end = find_keys(key_str)
final_message = find_text(message, start_end)
if final_message:
    print(final_message)
else:
    print('Empty result')
