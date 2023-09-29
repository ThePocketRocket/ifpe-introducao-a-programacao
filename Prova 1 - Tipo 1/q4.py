from os import system
system('cls')

list_empr = list()
while True:
    cod = input('Digite o código do empreendimento: ')
    if cod == '000': break
    area = float(input('Digite a área do empreendimento em m²: '))
    valor_emp = float(input('Digite o valor do empreendimento: '))
    valor_alu = float(input('Digite o valor do aluguel: '))
    alugado = input('O empreendimento está alugado ("s" ou "n"?) ').lower()

    print(f'Cod: {cod}\nÁrea: {area}m²\nValor do empreendimento: R${valor_emp}\nValor do aluguel: R${valor_alu}\nAlugado? {alugado}')
    
    list_empr.append([cod, area, valor_emp, valor_alu, alugado])
    
patrimonio = 0
empr_alugados = 0
valor_mensal = 0

menor_valor = 0
id_menor_valor = ''

maior_valor = 0
id_maior_valor = ''

for emp in list_empr:
    patrimonio += float(emp[2])
    if emp[4] == 's':
        empr_alugados += 1
        valor_mensal += float(emp[3])
    else:
        if id_menor_valor == '':
            menor_valor = emp[3]
            id_menor_valor = emp[0]

        if menor_valor > emp[3]:
            menor_valor = emp[3]
            id_menor_valor = emp[0]

        if maior_valor < emp[3]:
            maior_valor = emp[3]
            id_maior_valor = emp[0]

print(f'''O patrimônio é: R${patrimonio}
O número de empreendimentos alugados é: {empr_alugados}
O valor total mensal arrecadado é: R${valor_mensal}
Empreendimento com menor valor, disponível para alugar é: ID {id_menor_valor}
Empreendimento com maior valor, disponível para alugar é: ID {id_maior_valor}''')