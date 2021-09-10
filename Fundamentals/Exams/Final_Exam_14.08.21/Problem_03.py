def new(name: str, log: dict):
    if name not in log.keys():
        log[name] = 0


def like(name: str, likes: int, log: dict):
    if name not in log.keys():
        log[name] = 0
    log[name] += likes


def comment(name: str, log: dict):
    if name not in log.keys():
        log[name] = 0
    log[name] += 1


def block(name: str, log: dict):
    if name in log.keys():
        log.pop(name)
    else:
        print(f"{name} doesn't exist.")


followers = {}
command = input()
while not command == "Log out":
    command = command.split(": ")
    if command[0] == "New follower":
        new(command[1], followers)
    elif command[0] == "Like":
        like(command[1], int(command[2]), followers)
    elif command[0] == "Comment":
        comment(command[1], followers)
    elif command[0] == "Blocked":
        block(command[1], followers)
    command = input()

print(f'{len(followers)} followers')
[print(f'{i}: {j}') for i, j in sorted(followers.items(), key=lambda x: (-x[1], x[0]))]
