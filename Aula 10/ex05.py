base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

if expoente == 0:
    resultado = 1

elif expoente < 0:
    expoente2 = expoente * -1 # Deixa expoente positivo
    base2 = 1/base # Ajusta a base
    resultado = base2
    for i in range(expoente2 + 1):
        if i > 1:
            resultado *= base2

else:
    resultado = base
    for i in range(expoente + 1):
        if i > 1:
            resultado *= base

print(f'{base}^{expoente} = {resultado}')
