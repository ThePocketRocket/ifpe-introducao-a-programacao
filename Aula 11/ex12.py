while True:
    n = int(input('Digite um número inteiro de 0 à 99: '))
    if 0 <= n <= 99:
        break

n2 = str(n)
if 9 < n < 20:
    if n2 == '10': print('Dez')
    elif n2 == '11': print('Onze')
    elif n2 == '12': print('Doze')
    elif n2 == '13': print('Treze')
    elif n2 == '14': print('Quatorze')
    elif n2 == '15': print('Quinze')
    elif n2 == '16': print('Dezesseis')
    elif n2 == '17': print('Dezessete')
    elif n2 == '18': print('Dezoito')
    elif n2 == '19': print('Dezenove')
elif n >= 20:
    if n2[0] == '2': print('Vinte ', end='')
    elif n2[0] == '3': print('Trinta ', end='')
    elif n2[0] == '4': print('Quarenta ', end='')
    elif n2[0] == '5': print('Cinquenta ', end='')
    elif n2[0] == '6': print('Sessenta ', end='')
    elif n2[0] == '7': print('Setenta ', end='')
    elif n2[0] == '8': print('Oitenta ', end='')
    elif n2[0] == '9': print('Noventa ', end='')

if n > 19:
    if n2[0] != '1' and n2[1] != '0':
        print('e', end=' ')
    n2 = n2[1]

match n2:
    case '0':
        if n == 0:
            print('Zero')
    case '1': print('Um')
    case '2': print('Dois')
    case '3': print('Três')
    case '4': print('Quatro')
    case '5': print('Cinco')
    case '6': print('Seis')
    case '7': print('Sete')
    case '8': print('Oito')
    case '9': print('Nove')
