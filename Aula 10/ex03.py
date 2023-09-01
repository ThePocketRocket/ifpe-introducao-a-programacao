n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

contador = 0
for i in range(n1 + 1, n2):
    if i % 2 == 0:
        contador += 1

print(f'A quantidade de números pares entre {n1} e {n2} é: {contador}')