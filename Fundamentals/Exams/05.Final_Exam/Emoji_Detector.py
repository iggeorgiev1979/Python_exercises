import re


def cool_threshold(text: str):
    pattern = r"(\d)"
    numbers = re.findall(pattern, text)
    result = 1
    for el in numbers:
        result *= int(el)
    return result


def find_emoji(text: str):
    pattern = r"([*]{2}|[:]{2})(?P<emoji>[A-Z][a-z][a-z]+)\1"
    emoji = re.finditer(pattern, text)
    return [x.group() for x in emoji]


def find_cool_emoji(emoji_list: list, points: int):
    result = []
    for el in emoji_list:
        tmp_el = el[2:-2]
        sum_points = 0
        for i in tmp_el:
            sum_points += ord(i)
        if sum_points >= points:
            result.append(el)
    return result


text_input = input()
valid_emoji = find_emoji(text_input)
threshold = cool_threshold(text_input)
cool_emoji = find_cool_emoji(valid_emoji, threshold)
print(f"Cool threshold: {threshold}")
print(f"{len(valid_emoji)} emojis found in the text. The cool ones are:")
print(*cool_emoji, sep='\n')
