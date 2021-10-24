def reverse_arr(array, index=0):
    if index == len(array):
        return
    reverse_arr(array, index + 1)
    print(f"{array[index]} ", end='')


reverse_arr([1, 2, 3, 4, 5, 6, 7, 8, 9])
