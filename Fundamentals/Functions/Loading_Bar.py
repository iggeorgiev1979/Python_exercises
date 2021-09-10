number = int(input())


def loading_bar(a):
    b = a // 10
    if a == 100:
        print(f'100% Complete!\n[%%%%%%%%%%]')
    else:
        print(f'{a}% ' + '[' + '%' * b + '.' * (10 - b) + ']')

        print('Still loading...')


loading_bar(number)