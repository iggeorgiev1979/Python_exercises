import sys
import os
import re
from io import StringIO

input_1 = """Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End"""

sys.stdin = StringIO(input_1)


def create_file(name: str):
    return open(name, 'w')


def add_content(name: str, content: str):
    some_file = open(name, 'a')
    some_file.writelines(f'{content}\n')
    some_file.close()
    return some_file


def replace_content(name, old_str, new_str):
    file_path = os.path.exists(name)
    if not file_path:
        print("An error occurred")
    else:
        lines = []
        some_file = open(name, 'r')
        for line in some_file:
            pattern = rf'{old_str}'
            new_line = re.split(pattern, line)
            lines.append(f'{new_str}'.join(new_line))
        some_file = open(name, 'w')
        for el in lines:
            some_file.writelines(el)
        some_file.close()


def delete_file(name):
    file_path = os.path.exists(name)
    if not file_path:
        print("An error occurred")
    else:
        os.remove(name)


command = input()

while not command == 'End':
    command = command.split("-")
    if command[0] == "Create":
        file_name = command[1]
        file = create_file(file_name)
        file.close()
    elif command[0] == "Add":
        file_name = command[1]
        new_content = command[2]
        file = add_content(file_name, new_content)

    elif command[0] == "Replace":
        file_name = command[1]
        old_content = command[2]
        new_content = command[3]
        replace_content(file_name, old_content, new_content)
    elif command[0] == "Delete":
        file_name = command[1]
        delete_file(file_name)

    command = input()
