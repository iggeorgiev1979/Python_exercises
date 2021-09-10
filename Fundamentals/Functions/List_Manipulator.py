number = [int(x) for x in input().split()]


def manipulator(a):
    command = input().split(' ')
    while not command[0] == 'end':
        if command[0] == 'exchange':
            if int(command[1]) in range(len(a)):
                b = a[int(command[1]) + 1:] + a[:int(command[1]) + 1]
                a = b
            else:
                print('Invalid index')
        elif command[0] == 'max':
            if command[1] == 'odd':
                odd = [x for x in a if not x % 2 == 0]
                if len(odd) > 0:
                    max_odd = max(odd)
                    for i in range(len(a) - 1, -1, -1):
                        if max_odd == a[i]:
                            print(i)
                            break
                        elif i == 0:
                            print('No matches')
                else:
                    print('No matches')
            if command[1] == 'even':
                even = [x for x in a if x % 2 == 0]
                if len(even) > 0:
                    max_even = max(even)
                    for i in range(len(a) - 1, -1, -1):
                        if max_even == a[i]:
                            print(i)
                            break
                        elif i == 0:
                            print('No matches')
                else:
                    print('No matches')
        elif command[0] == 'min':
            if command[1] == 'odd':
                odd = [x for x in a if not x % 2 == 0]
                if len(odd) > 0:
                    min_odd = min(odd)
                    for i in range(len(a) - 1, -1, -1):
                        if min_odd == a[i]:
                            print(i)
                            break
                        elif i == 0:
                            print('No matches')
                else:
                    print('No matches')
            if command[1] == 'even':
                even = [x for x in a if x % 2 == 0]
                if len(even) > 0:
                    min_even = min(even)
                    for i in range(len(a) - 1, -1, -1):
                        if min_even == a[i]:
                            print(i)
                            break
                        elif i == 0:
                            print('No matches')
                else:
                    print('No matches')
        elif command[0] == 'first':
            if int(command[1]) > len(a):
                print('Invalid count')
            else:
                if command[2] == 'odd':
                    odd = [int(x) for x in a if not x % 2 == 0]
                    print(odd[:int(command[1])])
                else:
                    even = [int(x) for x in a if x % 2 == 0]
                    print(even[:int(command[1])])
        elif command[0] == 'last':
            if int(command[1]) > len(a):
                print('Invalid count')
            else:
                if command[2] == 'odd':
                    odd = [int(x) for x in a if not x % 2 == 0]
                    print(odd[-int(command[1]):])
                else:
                    even = [int(x) for x in a if x % 2 == 0]
                    print(even[-int(command[1]):])
        command = input().split(' ')
    print(a)


manipulator(number)