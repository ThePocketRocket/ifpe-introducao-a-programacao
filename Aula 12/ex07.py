meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = list()
media_temp = 0

for i in range(12):
    print(f'Digite a média de temperatura do mês de {meses[i]}', end=': ')
    temp = float(input())
    temperaturas.append(temp)
    media_temp += temp
media_temp /= 12

print(f'A temperatura média do ano é: {media_temp:.2f}')
for i in range(12):
    print(f'{temperaturas[i]} - {meses[i]}')


