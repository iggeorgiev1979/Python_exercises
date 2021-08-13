electrons = int(input())
shells_list = []
position = 1
while not electrons == 0:
    shells_list.append(2 * (position ** 2)) if electrons >= 2 * (position ** 2) else shells_list.append(electrons)
    electrons -= shells_list[position - 1]
    position += 1
print(shells_list)
