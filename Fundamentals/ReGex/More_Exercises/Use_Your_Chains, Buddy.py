import re


def extract_text(text: str):
    pattern = r'(?:<p>)(.+?)(?:</p>)'
    text = re.findall(pattern, text)
    return ''.join(text)


def spaces(text: str):
    text = re.sub(r'[^a-z0-9]', ' ', text)
    # text = re.sub(r'[\s]{2,}', ' ', text)
    return text


def replace_letters(text: str):
    result = ''
    for el in text:
        if 97 <= ord(el) <= 109:
            replacement = chr(ord(el) + 13)
            result += replacement
        elif 110 <= ord(el) <= 122:
            replacement = chr(ord(el) - 13)
            result += replacement
        else:
            result += el
    return result


def remove_spaces(text: str):
    text = re.sub(r'[\s]{2,}', ' ', text)
    return text


input_text = input()
input_text = extract_text(input_text)
input_text = replace_letters(input_text)
input_text = spaces(input_text)
input_text = remove_spaces(input_text)
print(input_text)
