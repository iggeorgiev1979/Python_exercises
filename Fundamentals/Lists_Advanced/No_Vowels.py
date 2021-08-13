vowels = ['a', 'A', 'o', 'O', 'u', 'U', 'e', 'E', 'i', 'I']
text = input()
text_list = [x for x in text if x not in vowels]
print(*text_list, sep='')
