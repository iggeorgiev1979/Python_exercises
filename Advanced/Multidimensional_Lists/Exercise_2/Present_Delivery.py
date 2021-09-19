def move_up(row, col, kids_with_present, kids, gifts):
    if not row == 0:
        neighbourhood[row][col] = "-"
        row -= 1
        if neighbourhood[row][col] == "V":
            kids_with_present += 1
            kids -= 1
            gifts -= 1
        elif neighbourhood[row][col] == "X":
            pass
        elif neighbourhood[row][col] == "C":
            kids_with_present, kids, gifts = happy_santa(row, col, kids_with_present, kids, gifts)
    neighbourhood[row][col] = "S"
    return row, col, kids_with_present, kids, gifts


def move_down(row, col, kids_with_present, kids, gifts):
    if not row > len(neighbourhood) - 2:
        neighbourhood[row][col] = "-"
        row += 1
        if neighbourhood[row][col] == "V":
            kids_with_present += 1
            kids -= 1
            gifts -= 1
        elif neighbourhood[row][col] == "X":
            pass
        elif neighbourhood[row][col] == "C":
            kids_with_present, kids, gifts = happy_santa(row, col, kids_with_present, kids, gifts)
    neighbourhood[row][col] = "S"
    return row, col, kids_with_present, kids, gifts


def move_left(row, col, kids_with_present, kids, gifts):
    if not col == 0:
        neighbourhood[row][col] = "-"
        col -= 1
        if neighbourhood[row][col] == "V":
            kids_with_present += 1
            kids -= 1
            gifts -= 1
        elif neighbourhood[row][col] == "X":
            pass
        elif neighbourhood[row][col] == "C":
            kids_with_present, kids, gifts = happy_santa(row, col, kids_with_present, kids, gifts)
    neighbourhood[row][col] = "S"
    return row, col, kids_with_present, kids, gifts


def move_right(row, col, kids_with_present, kids, gifts):
    if not col > len(neighbourhood) - 2:
        neighbourhood[row][col] = "-"
        col += 1
        if neighbourhood[row][col] == "V":
            kids_with_present += 1
            kids -= 1
            gifts -= 1
        elif neighbourhood[row][col] == "X":
            pass
        elif neighbourhood[row][col] == "C":
            kids_with_present, kids, gifts = happy_santa(row, col, kids_with_present, kids, gifts)
    neighbourhood[row][col] = "S"
    return row, col, kids_with_present, kids, gifts


def count_kids(size):
    kids = 0
    rr = None
    cc = None
    for row in range(size):
        for col in range(size):
            if neighbourhood[row][col] == "V":
                kids += 1
            elif neighbourhood[row][col] == "S":
                rr = row
                cc = col
    return kids, rr, cc


def happy_santa(rr, cc, k_p, kk, gf):
    if neighbourhood[rr - 1][cc] == "V":
        k_p += 1
        kk -= 1
        gf -= 1
    elif neighbourhood[rr - 1][cc] == "X":
        gf -= 1
    neighbourhood[rr - 1][cc] = "-"
    if neighbourhood[rr + 1][cc] == "V":
        k_p += 1
        kk -= 1
        gf -= 1
    elif neighbourhood[rr + 1][cc] == "X":
        gf -= 1
    neighbourhood[rr + 1][cc] = "-"
    if neighbourhood[rr][cc - 1] == "V":
        k_p += 1
        kk -= 1
        gf -= 1
    elif neighbourhood[rr][cc - 1] == "X":
        gf -= 1
    neighbourhood[rr][cc - 1] = "-"
    if neighbourhood[rr][cc + 1] == "V":
        k_p += 1
        kk -= 1
        gf -= 1
    elif neighbourhood[rr][cc + 1] == "X":
        gf -= 1
    neighbourhood[rr][cc + 1] = "-"
    return k_p, kk, gf


presents = int(input())
neighbourhood_size = int(input())
neighbourhood = []
for _ in range(neighbourhood_size):
    neighbourhood.append(input().split())

nice_kids, santa_row, santa_col = count_kids(neighbourhood_size)
nice_kids_with_present = 0
command = input()

while not command == "Christmas morning":
    if command == "up":
        santa_row, santa_col, nice_kids_with_present, nice_kids, presents = move_up(santa_row, santa_col, nice_kids_with_present, nice_kids, presents)
    elif command == "down":
        santa_row, santa_col, nice_kids_with_present, nice_kids, presents = move_down(santa_row, santa_col, nice_kids_with_present, nice_kids, presents)
    elif command == "left":
        santa_row, santa_col, nice_kids_with_present, nice_kids, presents = move_left(santa_row, santa_col, nice_kids_with_present, nice_kids, presents)
    elif command == "right":
        santa_row, santa_col, nice_kids_with_present, nice_kids, presents = move_right(santa_row, santa_col, nice_kids_with_present, nice_kids, presents)
    if presents == 0:
        break
    command = input()

if presents == 0 and not nice_kids == 0:
    print("Santa ran out of presents!")

for el in neighbourhood:
    print(*el)

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_present} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
