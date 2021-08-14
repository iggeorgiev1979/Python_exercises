def convert_notes(number_notes, codes):
    return_list = []
    for i in number_notes:
        return_list.append(codes[codes.index(i) - 1])
    return return_list


def naturals(number_notes, codes):
    return_list = []
    for i in number_notes:
        if len(codes[codes.index(i) - 1]) == 1:
            return_list.append(codes[codes.index(i) - 1])
    return return_list


def sharps(number_notes, codes):
    return_list = []
    for i in number_notes:
        if len(codes[codes.index(i) - 1]) == 2:
            return_list.append(codes[codes.index(i) - 1])
    return return_list


def natural_sum(number_notes, codes):
    return_list = []
    for i in number_notes:
        if len(codes[codes.index(i) - 1]) == 1:
            return_list.append(i)
    return return_list


def sharp_sum(number_notes, codes):
    return_list = []
    for i in number_notes:
        if len(codes[codes.index(i) - 1]) == 2:
            return_list.append(i)
    return return_list


notes = ['C', 261.63, 'C#', 277.18, 'D', 293.66, 'D#', 311.13, 'E', 329.63, 'F', 349.23, 'F#', 369.99, 'G', 392.00,
         'G#', 415.30, 'A', 440.00, 'A#', 466.16, 'B', 493.88]
numbers = [float(x) for x in input().split()]
print(f"Notes: {' '.join(convert_notes(numbers, notes))}")
print(f"Naturals: {', '.join(naturals(numbers, notes))}")
print(f"Sharps: {', '.join(sharps(numbers, notes))}")
print(f"Natural sum: {sum(natural_sum(numbers, notes)):.2f}")
print(f"Sharps sum: {sum(sharp_sum(numbers, notes)):.2f}")
