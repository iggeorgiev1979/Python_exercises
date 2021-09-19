def find_the_bunny():
    for row in range(size):
        for col in range(size):
            if field[row][col] == "B":
                return row, col


def collect_up(row, col):
    eggs = 0
    moves = []
    if not row == 0:
        for r in range(row - 1, -1, -1):
            if field[r][col] == "X":
                break
            else:
                eggs += int(field[r][col])
                moves.append(f'[{r}, {col}]')

    return {
        "direction": "up",
        "moves": moves,
        "eggs": eggs
    }


def collect_down(row, col):
    eggs = 0
    moves = []
    if not row == size - 1:
        for r in range(row + 1, size):
            if field[r][col] == "X":
                break
            else:
                eggs += int(field[r][col])
                moves.append(f'[{r}, {col}]')

    return {
        "direction": "down",
        "moves": moves,
        "eggs": eggs
    }


def collect_lef(row, col):
    eggs = 0
    moves = []
    if not col == 0:
        for c in range(col - 1, -1, -1):
            if field[row][c] == "X":
                break
            else:
                eggs += int(field[row][c])
                moves.append(f'[{row}, {c}]')

    return {
        "direction": "left",
        "moves": moves,
        "eggs": eggs
    }


def collect_right(row, col):
    eggs = 0
    moves = []
    if not col == size - 1:
        for c in range(col + 1, size):
            if field[row][c] == "X":
                break
            else:
                eggs += int(field[row][c])
                moves.append(f'[{row}, {c}]')

    return {
        "direction": "right",
        "moves": moves,
        "eggs": eggs
    }


size = int(input())
field = []
for _ in range(size):
    field.append(input().split())

winner = {
    "direction": "",
    "moves": [],
    "eggs": 0
}

row_index, col_index = find_the_bunny()

tmp = collect_up(row_index, col_index)
if tmp["eggs"] >= winner["eggs"]:
    winner = tmp

tmp = collect_down(row_index, col_index)
if tmp["eggs"] >= winner["eggs"]:
    winner = tmp

tmp = collect_lef(row_index, col_index)
if tmp["eggs"] >= winner["eggs"]:
    winner = tmp

tmp = collect_right(row_index, col_index)
if tmp["eggs"] >= winner["eggs"]:
    winner = tmp

print(winner["direction"])
print(*winner["moves"], sep='\n')
print(winner["eggs"])
