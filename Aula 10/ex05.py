base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

resultado = base
if expoente == 0:
    resultado = 1
else:
    for i in range(expoente+1):
        if i > 1:
            resultado *= base

print(f'{base} ^ {expoente} = {resultado}')
