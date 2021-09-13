size = [int(x) for x in input().split()]
snake = input()
counter = 0
for i in range(size[0]):
    tmp_string = ''
    for j in range(size[1]):
        if i % 2 == 0:
            boolean = True
        else:
            boolean = False
        tmp_string += snake[counter]
        counter += 1
        if counter == len(snake):
            counter = 0
    print(tmp_string) if boolean else print(tmp_string[::-1])
