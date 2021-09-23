def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes = []
    fill = True
    for el in args:
        if el == "Finish":
            fill = False
        elif fill:
            if volume - el >= 0:
                volume -= el
            else:
                el -= volume
                volume = 0
                cubes.append(el)
        else:
            cubes.append(el)

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    return f"No more free space! You have {sum(cubes)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
