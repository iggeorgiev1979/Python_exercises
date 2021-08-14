word = input()
print(*[f'{word[i]} -> {ord(word[i]) - 97}' for i in range(len(word))], sep='\n')
