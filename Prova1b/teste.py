# Lista para armazenar os dados de cada cidade
dados_cidades = []

while True:
    cidade = input("Digite o nome da cidade (ou 'sair' para encerrar a coleta): ").strip().lower()
    
    if cidade == 'sair':
        break
    
    novos_casos = int(input(f"Digite o número de novos casos em {cidade}: "))
    dia = input(f"Digite a data (dia/mês/ano) para {cidade}: ")
    
    # Verifica se a cidade já está na lista
    cidade_existente = False
    for cidade_data in dados_cidades:
        if cidade_data['cidade'] == cidade:
            cidade_data['casos'].append(novos_casos)
            cidade_data['dias'].append(dia)
            cidade_data['total_casos'] += novos_casos
            cidade_existente = True
            break
    
    # Se a cidade não estiver na lista, adicione-a
    if not cidade_existente:
        dados_cidade = {'cidade': cidade, 'casos': [novos_casos], 'dias': [dia], 'total_casos': novos_casos}
        dados_cidades.append(dados_cidade)
    
    print(f"Dados registrados para {cidade} em {dia}: Novos casos: {novos_casos}, Total acumulado: {dados_cidade['total_casos']}")
    
# Calcula as informações solicitadas
for cidade_data in dados_cidades:
    cidade = cidade_data['cidade']
    total_casos = cidade_data['total_casos']
    dias = cidade_data['dias']
    casos_diarios = cidade_data['casos']
    
    media_casos_diarios = sum(casos_diarios) / len(casos_diarios)
    
    dia_maior_casos = dias[casos_diarios.index(max(casos_diarios))]
    
    print(f"\nCidade: {cidade}")
    print(f"Total de casos acumulados: {total_casos}")
    print(f"Dia com o maior número de casos: {dia_maior_casos}")
    print(f"Média de casos diários: {media_casos_diarios:.2f}")

# Encontra a cidade com o maior número acumulado de casos
cidade_maior_acumulado = max(dados_cidades, key=lambda cidade_data: cidade_data['total_casos'])
print(f"\nCidade com o maior número acumulado de casos: {cidade_maior_acumulado['cidade']}")