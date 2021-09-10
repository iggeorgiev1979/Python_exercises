text = input()
x = input()
while True:
    boolean = False
    if not x:
        break
    tmp = text.split(x, 1)
    if len(tmp) > 1:
        boolean = True
    else:
        break
    if boolean:
        tmp = ''.join(tmp)
    tmp = tmp.rsplit(x, 1)
    if len(tmp) == 1:
        boolean = False
    if boolean:
        text = ''.join(tmp)
        print('Shaked it.')
        x = x[:len(x) // 2] + x[len(x) // 2 + 1:]
        if not x:
            boolean = False
            break
    else:
        break
if not boolean:
    print('No shake.')
    print(text)
