text = input('Digite seu nome de usuário: ')
text2 = text.replace(' ', '')

text3 = ''
for i in range(len(text2)):
    text3 += text2[-i-1]

if text2 == text3:
    print(f'{text} é um palíndromo!')
else:
    print(f'{text} não é um palíndromo!')