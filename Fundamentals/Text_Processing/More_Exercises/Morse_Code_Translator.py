morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
              '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
              '--..': 'Z'}

text = input()
word = ''
for el in text:
    if not el == '|':
        word += el
    else:
        word = word.split()
        for i in word:
            print(morse_code[i], end='')
        print(' ', end='')
        word = ''
word = word.split()
for i in word:
    print(morse_code[i], end='')
print()
