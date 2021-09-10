raw_key = input()
command = input().split('>>>')
while not command[0] == 'Generate':
    if command[0] == 'Contains':
        if command[1] in raw_key:
            print(f'{raw_key} contains {command[1]}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        raw = raw_key[int(command[2]):int(command[3])]
        if command[1] == 'Lower':
            raw = raw.lower()
        elif command[1] == 'Upper':
            raw = raw.upper()
        raw_list = list(raw_key)
        del raw_list[int(command[2]):int(command[3])]
        raw_list.insert(int(command[2]), raw)
        raw_key = ''.join(raw_list)
        print(raw_key)
    elif command[0] == 'Slice':
        raw_list = list(raw_key)
        del raw_list[int(command[1]):int(command[2])]
        raw_key = ''.join(raw_list)
        print(raw_key)
    command = input().split('>>>')
print(f'Your activation key is: {raw_key}')
