import re


def validate(text: str):
    pattern = r"^(?P<begin>[$|%])(?P<tag>[A-Z][a-z]{2,})(?P=begin): \[(?P<first>\d+)\]\|\[(?P<second>\d+)\]\|\[(?P<third>\d+)\]\|$"
    match = re.match(pattern, text)
    if match:
        el = match.groupdict()
        return el


def decrypt(message_dict: dict):
    tag = message_dict["tag"]
    first = message_dict["first"]
    second = message_dict["second"]
    third = message_dict["third"]
    print_result = f"{tag}: {chr(int(first))}{chr(int(second))}{chr(int(third))}"
    print(print_result)


for _ in range(int(input())):
    message = input()
    result = validate(message)
    decrypt(result) if result else print("Valid message not found!")
