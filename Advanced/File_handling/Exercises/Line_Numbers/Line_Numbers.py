import re


def count_chars(txt: str):
    pattern = r'([A-Za-z])'
    return len(re.findall(pattern, txt))


def count_marks(txt: str):
    pattern = r'([\.\-\,\:\!\;\'\?])'
    return len(re.findall(pattern, txt))


input_file = open('text.txt', 'r')
output_file = open('output.txt', 'a')
index = 1
for line in input_file:
    chars = count_chars(line)
    marks = count_marks(line)
    output_file.writelines(f'Line {index}: {line[:-1]} ({chars})({marks})\n')
    index += 1
output_file.close()

