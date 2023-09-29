from os import system
system('cls')

str_1 = input('Digite a primeira string: ').strip().upper()
str_2 = input('Digite a primeira string: ').strip().upper()

str_3 = ''
for letra in str_1:
    if str_2.count(letra) > 0 and str_3.count(letra) == 0:
        str_3 += letra

str_4 = ''
for i, letra in enumerate(str_1):
    if str_2.count(letra) == 0 and str_4.count(letra) == 0:
        str_4 += letra
for i, letra in enumerate(str_2):
    if str_1.count(letra) == 0 and str_4.count(letra) == 0:
        str_4 += letra

print(f'''Caracteres comuns: {str_3}
Caracteres distintos: {str_4}''')