def get_magic_triangle(n: int, row=2, result=[[1], [1, 1]]):
    if row < n:
        tmp = []
        tmp_el = result[-1]
        for el in range(row + 1):
            if el == 0:
                tmp.append(tmp_el[0])
            elif el == row:
                tmp.append(tmp_el[-1])
            else:
                tmp.append(tmp_el[el] + tmp_el[el - 1])
        result.append(tmp)
        return get_magic_triangle(n, row + 1, result)

    return result


print(get_magic_triangle(5))
