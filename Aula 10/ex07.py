numero = int(input('Digite um número para saber a soma dos seus divisores: '))

resultado = 0
for _ in range(1, numero):
    if numero % _ == 0:
        resultado += _

print(f'A soma dos divisores de {numero} é: {resultado}')