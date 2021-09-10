import re


def validate(text: str):
    pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
    result = [x[1] for x in re.findall(pattern, text)]
    return result


def calculate_points(destinations: list):
    result = 0
    for i in destinations:
        result += len(i)
    return result


locations = validate(input())
travel_points = calculate_points(locations)

print(f'Destinations: {", ".join(locations)}')
print(f'Travel Points: {travel_points}')
