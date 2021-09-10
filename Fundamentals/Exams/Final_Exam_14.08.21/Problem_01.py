def make(text: str, arg: str):
    if arg == 'Upper':
        return text.upper()
    elif arg == 'Lower':
        return text.lower()


def getdomain(text: str, count: int):
    print(text[len(text) - count:])


def get_name(text: str):
    result = ""
    for el in text:
        if el == "@":
            break
        else:
            result += el
    print(result) if "@" in text else print(f"The email {text} doesn't contain the @ symbol.")


def replace(text: str, arg: str):
    result = text.replace(arg, "-")
    print(result)
    return result


def encrypt(text: str):
    for el in text:
        print(ord(el), end=" ")
    print()


email = input()
command = input()
while not command == 'Complete':
    command = command.split()
    if command[0] == 'Make':
        email = make(email, command[1])
        print(email)
    elif command[0] == 'GetDomain':
        getdomain(email, int(command[1]))
    elif command[0] == 'GetUsername':
        get_name(email)
    elif command[0] == 'Replace':
        email = replace(email, command[1])
    elif command[0] == 'Encrypt':
        encrypt(email)
    command = input()
