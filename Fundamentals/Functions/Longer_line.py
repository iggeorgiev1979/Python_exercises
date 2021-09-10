from math import floor


def line(x1, y1, x2, y2):
    side_a = abs(x1) + abs(y1)
    side_b = abs(x2) + abs(y2)
    return side_a + side_b


def point(a, b):
    return abs(a) + abs(b)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

line_1 = line(x_1, y_1, x_2, y_2)
line_2 = line(x_3, y_3, x_4, y_4)
point_1 = point(x_1, y_1)
point_2 = point(x_2, y_2)
point_3 = point(x_3, y_3)
point_4 = point(x_4, y_4)

if line_1 >= line_2:
    print(f'({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})') if point_1 <= point_2 else print(
        f'({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})')
else:
    print(f'({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})') if point_3 <= point_4 else print(
        f'({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})')
