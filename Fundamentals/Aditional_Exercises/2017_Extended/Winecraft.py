def greater_grapes(list_of_grapes):
    tmp_list = []
    for i in range(1, len(list_of_grapes) - 1):
        if list_of_grapes[i] > list_of_grapes[i - 1] and list_of_grapes[i] > list_of_grapes[i + 1]:
            tmp_list.append(i)
    return tmp_list


grapes = [int(x) for x in input().split()]
n = int(input())
boolean = True
while len(grapes) >= n:
    for _ in range(n):
        if len(grapes) > 2:
            greater_list = greater_grapes(grapes)
        else:
            greater_list = []
        for i in range(len(grapes)):
            if i == 0 and i + 1 in greater_list:
                if not grapes[i] == 0:
                    grapes[i] -= 1
                    grapes[i + 1] += 1
            elif i == len(grapes) - 1 and i - 1 in greater_list:
                if not grapes[i] == 0:
                    grapes[i] -= 1
                    grapes[i - 1] += 1
            elif i in greater_list:
                pass
            elif i + 1 in greater_list:
                if not grapes[i] == 0:
                    grapes[i] -= 1
                grapes[i + 1] += 1
                if i - 1 in greater_list:
                    if not grapes[i] == 0:
                        grapes[i] -= 1
                    grapes[i - 1] += 1
                if not grapes[i] == 0 and i - 1 in greater_list and i + 1 in greater_list:
                    grapes[i] -= 1
            elif i - 1 in greater_list:
                if not grapes[i] == 0:
                    grapes[i] -= 1
                grapes[i - 1] += 1
                if i + 1 in greater_list:
                    if not grapes[i] == 0:
                        grapes[i] -= 1
                    grapes[i + 1] += 1
                if not grapes[i] == 0 and i - 1 in greater_list and i + 1 in greater_list:
                    grapes[i] -= 1
            else:
                grapes[i] += 1
    grapes = list(filter(lambda x: x > n, grapes))
print(*grapes, sep=' ')
