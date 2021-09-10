def register(log: dict, info: list):
    piece, composer, key = info
    log[piece] = [composer, key]


def add(log: dict, info: list):
    del info[:1]
    piece, composer, key = info
    if piece in log.keys():
        print(f"{piece} is already in the collection!")
    else:
        log[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove(log: dict, info: list):
    piece = info[1]
    if piece in log.keys():
        log.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change(log: dict, info: list):
    del info[:1]
    piece, key = info
    if piece in log.keys():
        log[piece][1] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


pieces = {}
for _ in range(int(input())):
    info_list = input().split('|')
    register(pieces, info_list)
command = input()
while not command == 'Stop':
    command = command.split('|')
    if command[0] == 'Add':
        add(pieces, command)
    elif command[0] == 'Remove':
        remove(pieces, command)
    elif command[0] == 'ChangeKey':
        change(pieces, command)
    command = input()
[print(f"{i} -> Composer: {j[0]}, Key: {j[1]}") for i, j in sorted(pieces.items(), key=lambda x: (x[0], x[1][0]))]
