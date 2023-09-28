lista1 = ['oi', 'OLÁ', 15, 5, 15, 4]
lista2 = ['hello', 'olá', 'Olá', 2, 4, 15]
lista1_lower = list()
lista2_lower = list()
lista1_exclusivo = list()
lista2_exclusivo = list()
lista_iguais = list()
sem_repeticao = list()

for i in range(len(lista1)):
    if type(lista1[i]) == str:
        letra = str(lista1[i]).lower()
        lista1_lower.append(letra)
    else: lista1_lower.append(lista1[i])

for i in range(len(lista2)):
    if type(lista2[i]) == str:
        letra = str(lista2[i]).lower()
        lista2_lower.append(letra)
    else: lista2_lower.append(lista2[i])

for _ in lista1_lower:
    existe_na_lista2 = lista2_lower.count(_) > 0
    if existe_na_lista2 and lista_iguais.count(_) < 1:
        lista_iguais.append(_)
    elif not(existe_na_lista2):
        lista1_exclusivo.append(_)
    
    if lista1_lower.count(_) == 1 and sem_repeticao.count(_) == 0:
        sem_repeticao.append(_)

for _ in lista2_lower:
    existe_na_lista1 = lista1_lower.count(_) > 0
    if not(existe_na_lista1) and lista2_exclusivo.count(_) < 1:
        lista2_exclusivo.append(_)
    
    if lista2_lower.count(_) == 1 and sem_repeticao.count(_) == 0:
        sem_repeticao.append(_)

print(lista_iguais, 'Valores em comum')
print(lista1_exclusivo, 'Valores exclusivos da lista 1')
print(lista2_exclusivo, 'Valores exclusivos da lista 2')
print(sem_repeticao, 'Valores sem repetição, presentes nas listas')