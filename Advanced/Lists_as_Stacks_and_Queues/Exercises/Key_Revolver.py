bullet_price = int(input())
barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(x) for x in input().split()]
intelligence = int(input())
shooting_counter = 0
while True:
    for el in range(len(bullets) - 1, -1, -1):
        bullet = bullets.pop(el)
        shooting_counter += 1
        intelligence -= bullet_price
        if bullet <= locks[0]:
            locks.pop(0)
            print('Bang!')
        else:
            print('Ping!')
        if shooting_counter == barrel and len(bullets) > 0:
            print('Reloading!')
            shooting_counter = 0
        if len(locks) == 0:
            break
    if len(bullets) == 0 or len(locks) == 0:
        break

print(f'{len(bullets)} bullets left. Earned ${intelligence}') if len(locks) == 0 else print(f'Couldn\'t get through. Locks left: {len(locks)}')
