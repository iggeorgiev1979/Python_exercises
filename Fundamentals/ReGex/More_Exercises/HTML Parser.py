import re


def title(text: str):
    pattern_title = r"(?:<title>)(.+)(?:</title>)"
    return re.findall(pattern_title, text)


def body(text: str):
    body_pattern = r"(?:<body>)(.+)(?:</body>)"
    return re.findall(body_pattern, text)


def remove_n(text: str):
    text = text.split('\\n')
    return ''.join(text)


def remove_tags(text: str):
    pattern = r"(<[^>]*>)"
    el = re.findall(pattern, text)
    for i in el:
        text = text.replace(i, ' ')
    text = text.strip()
    return text


text_input = input()
text_input = remove_n(text_input)
body_text = body(text_input)[0]
title_text = title(text_input)[0]
body_text = remove_tags(body_text)
title_text = remove_tags(title_text)
body_text = body_text.split()
title_text = title_text.split()

print(f'Title: {" ".join(title_text)}')
print(f'Content: {" ".join(body_text)}')
