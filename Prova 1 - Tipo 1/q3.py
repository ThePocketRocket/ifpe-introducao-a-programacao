from os import system
system('cls')

valor = int(input('Digite um valor menor que R$1000: '))

valor_manipulavel = valor
cem = valor_manipulavel // 100
valor_manipulavel %= 100
cinquenta = valor_manipulavel // 50
valor_manipulavel %= 50
vinte = valor_manipulavel // 20
valor_manipulavel %= 20
dez = valor_manipulavel // 10
valor_manipulavel %= 10
cinco = valor_manipulavel // 5
valor_manipulavel %= 5
dois = valor_manipulavel // 2
valor_manipulavel %= 2
um = valor_manipulavel // 1

print(f'''Dado o valor R${valor}
{cem} notas de R$100
{cinquenta} notas de R$50
{vinte} notas de R$20
{dez} notas de R$10
{cinco} notas de R$5
{dois} notas de R$2
{um} notas de R$1''')