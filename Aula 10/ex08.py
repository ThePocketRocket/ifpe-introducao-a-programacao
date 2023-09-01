numero = int(input('Digite um número para saber o valor da soma de sua série harmônica: '))

serie_harmonica = 0
for _ in range(1, numero + 1):
    serie_harmonica += 1 / _

print(f'A soma da série harmônica de {numero} é: {serie_harmonica}')