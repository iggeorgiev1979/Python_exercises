password = input()


def check(a):
    valid_1 = False
    valid_2 = False
    valid_3 = False
    if 6 <= len(a) <= 10:
        valid_1 = True
    else:
        print('Password must be between 6 and 10 characters')
    alpha = a.isalnum()
    if alpha:
        valid_2 = True
    else:
        print('Password must consist only of letters and digits')
    counter = 0
    for i in a:
        digit = i.isdigit()
        if digit:
            counter += 1
    if counter >= 2:
        valid_3 = True
    else:
        print('Password must have at least 2 digits')
    if valid_1 and valid_2 and valid_3:
        print('Password is valid')


check(password)