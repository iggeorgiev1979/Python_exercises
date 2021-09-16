from collections import deque


def check_colour(first_part, second_part):
    if first_part + second_part in wanted_colours.keys():
        return first_part + second_part
    if second_part + first_part in wanted_colours.keys():
        return second_part + first_part
    return None


wanted_colours = {
    "red": "red",
    "yellow": "yellow",
    "blue": "blue",
    "orange": "orange",
    "purple": "purple",
    "green": "green"
}

txt = deque(input().split())
colours = []
while len(txt) > 1:
    first = txt.popleft()
    second = txt.pop()
    colour = check_colour(first, second)
    if colour and colour not in colours:
        colours.append(colour)
    else:
        index = len(txt) // 2
        first = first[:-1]
        second = second[:-1]
        if second:
            txt.insert(index, second)
        if first:
            txt.insert(index, first)
if len(txt) == 1:
    if txt[0] in wanted_colours.keys() and txt[0] not in colours:
        colours.append(txt[0])

result = []
for el in colours:
    if el == 'orange':
        if 'red' in colours and 'yellow' in colours:
            result.append(el)
    elif el == 'purple':
        if 'red' in colours and 'blue' in colours:
            result.append(el)
    elif el == 'green':
        if 'yellow' in colours and 'blue' in colours:
            result.append(el)
    else:
        result.append(el)

print(result)
