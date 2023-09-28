from os import system
system('cls')

casos_diarios = []
while True:
    casos = []
    casos.append(input('Digite a cidade: ').upper())
    casos.append(int(input('Digite o dia: ')))
    casos.append(int(input('Digite o número de casos do dia: ')))
    casos_diarios.append(casos)

    print(f'A cidade {casos[0]}, no dia {casos[1]}, teve {casos[2]} casos.')

    escolha = 'null'
    while 'n' != escolha != 's':
        escolha = input('Deseja continuar cadastrando novos casos ("s" ou "n")? ').lower()
        
    if escolha == 's':
        continue
    elif escolha == 'n':
        break
casos_diarios.sort()

cidades = []
casos_por_cidade = []
for d, valor in enumerate(casos_diarios):
    total_casos = 0
    cidade = casos_diarios[d][0]
    for i in range(len(casos_diarios)):
        if cidade == casos_diarios[i][0]:
            total_casos += casos_diarios[i][2]
    
    if cidades.count(cidade) == 0:
        cidades.append(cidade)
        casos_por_cidade.append(total_casos)

print(casos_diarios)
for i in range(len(cidades)):
    print(f'{cidades[i]}: {casos_por_cidade[i]} casos.')



mais_casos = []
for i in range(len(cidades)):
    if casos_por_cidade[i] > mais_casos:
        mais_casos.append([cidades[i], casos_por_cidade[i]])
print(f'A cidade {mais_casos[0]} tem o maior número de casos acumulados')