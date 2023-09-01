numero = int(input('Digite um número de 1 à 10 para gerar sua tabuada: '))

for _ in range(1, 11):
    print(f'{numero:^3} x {_:^3} = {numero * _:^5}')