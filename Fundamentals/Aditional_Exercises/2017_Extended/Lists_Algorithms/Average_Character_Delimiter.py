letters = input().split()
letters_string = ''.join(letters)
average_character = chr(sum([ord(x) for x in letters_string]) // len(letters_string)).upper()
print(f'{average_character}'.join(letters))
