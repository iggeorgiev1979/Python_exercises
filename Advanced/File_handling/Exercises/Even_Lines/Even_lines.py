import re


def even_line(txt: str):
    pattern = r'[\?\!\-\,\.]'
    new_line = re.split(pattern, txt)
    new_line = "@".join(new_line)
    new_line = new_line.split()
    new_line.reverse()
    return " ".join(new_line)


file = open('text.txt', 'r')
line = file.readlines()
for index in range(len(line)):
    if index % 2 == 0:
        result = even_line(line[index])
        print(result)

