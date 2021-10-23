def print_rhombus(size: int, step=1):
    print(generate_row(size, step))
    if step == size:
        return
    print_rhombus(size, step + 1)
    print(generate_row(size, step))


def generate_row(size: int, row: int):
    tmp_list = ["*"] * row
    total_elements = (size * 2) - 1
    star_space = (row * 2) - 1
    empty_spaces = (total_elements - star_space) // 2
    return f"{' ' * empty_spaces}{' '.join(tmp_list)}{' ' * empty_spaces}"


print_rhombus(int(input()))
