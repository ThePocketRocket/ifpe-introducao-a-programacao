from os import system
system('cls')

while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if n1 == n2:
        print('Intervalo inválido!')
    else:
        break

multiplicacao = 0
if n1 <= n2:
    multiplicacao = 1
    for i in range(n1 + 1, n2):
        if i % 2 != 0:
            multiplicacao *= i
else:
    multiplicacao = 1
    for i in range(n2 + 1, n1):
        if i % 2 != 0:
            multiplicacao *= i

soma = 0
if n1 <= n2:
    for i in range(n1, n2):
        if i % 2 == 0:
            soma += i
else:
    for i in range(n2, n1):
        if i % 2 == 0:
            soma += i

print(f'A multiplicação é igual: {multiplicacao}\nA soma é igual: {soma}')