from os import system
system('cls')

numero = int(input('Digite um número inteiro: '))

for i in range(5, numero, 2):
    fatores = []
    soma_fatores = 0
    for d in range(1, i):
        if numero % d == 0:
            fatores.append(d)
            soma_fatores += d

if soma_fatores == numero:
    print(f'{numero} é perfeito.')
else:
    print(f'{numero} não é perfeito.')

for _ in range(numero - 1, 5, -1):
    for i in range(_):
        fatores = []
        soma_fatores = 0
        for d in range(1, i):
            if _ % d == 0:
                fatores.append(d)
                soma_fatores += d

    if soma_fatores == _:
        print(f'{_} é perfeito.')