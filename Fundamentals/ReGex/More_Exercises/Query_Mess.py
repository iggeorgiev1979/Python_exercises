import re


def spaces(text: str):
    text = re.sub(r'(%20)|\+', ' ', text)
    text = re.sub(r'[\s]{2,}', ' ', text)
    return text


def split_elements(text: str):
    return re.split(r'&', text)


def extract_key_value(log: dict, elements: str):
    pattern = r'([^?]+)=([^?]+)'
    elements = re.findall(pattern, elements)
    key = elements[0][0].strip()
    value = elements[0][1].strip()
    if key not in log.keys():
        log[key] = []
    log[key].append(value)


text_input = input()
while not text_input == 'END':
    text_input = spaces(text_input)
    text_input = split_elements(text_input)
    tmp_dict = {}
    for el in text_input:
        extract_key_value(tmp_dict, el)
    [print(f'{i}=[{", ".join(j)}]', end='') for i, j in tmp_dict.items()]
    print()
    text_input = input()
