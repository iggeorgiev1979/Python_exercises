def check_ticket(text: str):
    left_side = text[:10]
    right_side = text[10:]
    left = ''
    right = ''
    for i in range(10):
        if left_side[i] == '$' or left_side[i] == '#' or left_side[i] == '@' or left_side[i] == '^':
            left += left_side[i]
            for j in range(i + 1, 10):
                if left_side[j] == left[-1]:
                    left += left_side[j]
                else:
                    if len(left) < 6:
                        left = ''
                        break
            if len(left) <= 5:
                left = ''
            else:
                break

    if len(left) > 5:
        for i in range(10):
            if right_side[i] == '$' or right_side[i] == '#' or right_side[i] == '@' or right_side[i] == '^':
                right += right_side[i]
                for j in range(i + 1, 10):
                    if right_side[j] == right[-1]:
                        right += right_side[j]
                    else:
                        if len(right) < 6:
                            right = ''
                            break
                if len(right) > 5:
                    break
                else:
                    right = ''

    if right == left and len(right) == 10:
        print(f'ticket "{text}" - {len(right)}{right[0]} Jackpot!')
    elif not left == '' and not right == '' and left[0] == right[0]:
        if len(right) <= len(left):
            print(f'ticket "{text}" - {len(right)}{right[0]}')
        else:
            print(f'ticket "{text}" - {len(left)}{left[0]}')
    else:
        print(f'ticket "{text}" - no match')


ticket_str = input().strip().split(',')

for el in ticket_str:
    el = el.strip()
    if not len(el) == 20:
        print('invalid ticket')
    else:
        check_ticket(el)
