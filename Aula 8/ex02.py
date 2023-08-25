numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 4 == 0:
    print(f'{numero} é divisível tanto por 3 quanto por 4')
elif numero % 3 == 0:
    print(f'{numero} é divisível tanto por 3')
elif numero % 4 == 0:
    print(f'{numero} é divisível tanto por 4')
else:
    print(f'{numero} não é divisível por 3 nem por 4')
