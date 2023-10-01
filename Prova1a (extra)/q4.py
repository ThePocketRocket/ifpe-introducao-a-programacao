from os import system
system('cls')

lista_renda_familias = []
while True:
    individuos = int(input('Digite o número de indivíduos da família: '))
    renda_total = 0
    # Gera renda total
    for _ in range(individuos): renda_total += float(input('Digite a renda mensal do indivíduo: '))
    
    renda_per_capita = float(renda_total/individuos)
    lista_renda_familias.append(renda_per_capita)

    print(f'''Renda total da família: R${renda_total}
A família possui {individuos} membros
A renda per-capita da família é: R${renda_per_capita}''')

    # Verifica se quer cadastrar mais famílias
    escolha = 'null'
    while 's' != escolha != 'n': escolha = input('Quer cadastrar mais famílias ("s" ou "n")? ').lower()
    if escolha == 'n': break
    elif escolha == 's': continue

renda_media_cidade = 0
renda_inferior = 0
renda_superior = 0
for i, renda in enumerate(lista_renda_familias):
    renda_media_cidade += renda
    if renda <= 1212: renda_inferior += 1
    elif renda > (10*1212): renda_superior += 1
renda_media_cidade /= len(lista_renda_familias)

system('cls')
print(f'''Renda média das famílias do município: R${renda_media_cidade}
Famílias com renda per-capita inferior a 1 salário mínimo: {(renda_inferior*100)/len(lista_renda_familias)}%
Famílias com renda per-capita superior a 10 salários mínimos: {renda_superior}''')


