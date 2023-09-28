n = int(input('Digite o número de linhas do Triângulo de Floyd: '))

indice = 1
for i in range(1, n + 1):
    for c in range(i):
        print(indice, end=' ')
        indice += 1
    print()