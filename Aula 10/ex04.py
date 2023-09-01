numero = int(input('Digite um número para saber seu fatorial: '))

fatorial = numero
for i in range(numero, 0, -1):
    if fatorial != i:
        fatorial *= i

print(f'{numero}! = {fatorial}')
