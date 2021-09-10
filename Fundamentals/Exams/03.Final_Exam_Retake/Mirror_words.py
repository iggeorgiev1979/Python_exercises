import re


def validate(text: str):
    pattern = r"(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
    result = re.findall(pattern, text)
    return result


def find_mirror(words: list):
    mirror = {}
    for el in words:
        if el[1] == el[2][::-1]:
            mirror[el[1]] = el[2]
    return mirror


text_input = input()
result_list = validate(text_input)
if len(result_list) == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f'{len(result_list)} word pairs found!')
    mirror_words = find_mirror(result_list)
    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(*[f"{i} <=> {j}" for i, j in mirror_words.items()], sep=', ')
