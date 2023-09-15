import math

area_para_pintar = float(input('Digite a área em m² que você deseja pintar: '))
quantidade_tinta = area_para_pintar/3
quantidade_latas = math.ceil(quantidade_tinta/18)
valor_gasto = quantidade_latas * 80

print(f'''A área que você deseja pintar é de: {area_para_pintar}m²
A quantidade de latas necessárias são: {quantidade_latas} latas
O valor a ser pago é: R${valor_gasto}''')