def points(card: str):
    x = card_type[card[-1:]]
    y = power[card[:-1]]
    return x * y


def register(log: dict, score: dict, card: list, name: str):
    if name not in log.keys():
        log[name] = []
        score[name] = 0
    for el in card:
        if el not in log[name]:
            log[name].append(el)
            score[name] += points(el)


power = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
card_type = {'S': 4, 'H': 3, 'D': 2, 'C': 1}
player = {}
total_points = {}
command = input().split(': ')
while not command[0] == 'JOKER':
    player_name = command[0]
    cards_list = command[1].split(', ')
    register(player, total_points, cards_list, player_name)
    command = input().split(': ')
[print(f'{i}: {j}') for i, j in total_points.items()]
