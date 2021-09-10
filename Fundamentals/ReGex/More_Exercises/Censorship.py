import re


def replace_word(word: str, text: str):
    replacement = '*' * len(word)
    text = re.sub(rf'{word}', f'{replacement}', text)
    return text


input_word = input()
input_text = input()
print(replace_word(input_word, input_text))
