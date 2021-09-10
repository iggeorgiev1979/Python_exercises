key = [int(x) for x in input().split()]
text = input()
while not text == 'find':
    index = 0
    tmp_text = ''
    for el in text:
        tmp_text += chr(ord(el) - key[index])
        index += 1
        if index == len(key):
            index = 0
    name = tmp_text[tmp_text.index('&') + 1: tmp_text.rindex('&')]
    position = tmp_text[tmp_text.index('<') + 1: tmp_text.index('>')]
    print(f'Found {name} at {position}')
    text = input()
