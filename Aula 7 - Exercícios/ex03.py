idade_nadador = int(input('Digite sua idade: '))
grupo = ''

if idade_nadador > 18:
    grupo = 'adulto'
elif 14 <= idade_nadador <= 17:
    grupo = 'juvenil B'
elif 11 <= idade_nadador <= 13:
    grupo = 'juvenil A'
elif 8 <= idade_nadador <= 10:
    grupo = 'infantil B'
elif 5 <= idade_nadador <= 7:
    grupo = 'infantil A'
else:
    grupo = 'fora do escopo de idades'

print(f'Você se enquadra em: {grupo}')
