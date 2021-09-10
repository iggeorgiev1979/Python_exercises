import re


def email(text: str):
    text = re.findall(r'(.*)(?:@)(.*)', text)
    el_1 = sum([ord(x) for x in text[0][0]])
    el_2 = sum([ord(x) for x in text[0][1]])
    result = el_1 - el_2
    print('Call her!') if result >= 0 else print('She is not the one.')


message = input()
email(message)
