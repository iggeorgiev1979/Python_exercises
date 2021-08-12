line_1 = [int(i) for i in input().split(' ')]
line_2 = [int(i) for i in input().split(' ')]
line_3 = [int(i) for i in input().split(' ')]
winner = False
player_1 = False

x = set(line_1)
a = sum(x)
if len(x) == 1 and not a == 0:
    winner = True
    if a == 1:
        player_1 = True
if not winner:
    x = set(line_2)
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if not winner:
    x = set(line_3)
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if not winner:
    x = {line_1[0], line_2[0], line_3[0]}
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if not winner:
    x = {line_1[1], line_2[1], line_3[1]}
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if not winner:
    x = {line_1[2], line_2[2], line_3[2]}
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if not winner:
    x = {line_1[0], line_2[1], line_3[2]}
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if not winner:
    x = {line_1[2], line_2[1], line_3[0]}
    a = sum(x)
    if len(x) == 1 and not a == 0:
        winner = True
        if a == 1:
            player_1 = True
if winner:
    if player_1:
        print('First player won')
    else:
        print('Second player won')
else:
    print('Draw!')
