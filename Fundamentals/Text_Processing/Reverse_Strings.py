text = input()
while not text == 'end':
    print(text, '=', text[::-1])
    text = input()
