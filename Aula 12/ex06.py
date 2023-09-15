data = input('Digite a data no padrão dd/mm/aaaa: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print(f'{data[0:2]}/{meses[int(data[3:5])]}/{data[6:]}')
