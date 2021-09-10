from math import floor


def triangle(a, b):
    return abs(a) + abs(b)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

point_1 = triangle(x_1, y_1)
point_2 = triangle(x_2, y_2)
print(f'({floor(x_1)}, {floor(y_1)})') if point_1 <= point_2 else print(f'({floor(x_2)}, {floor(y_2)})')
