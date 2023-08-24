import math

raio = float(input('Digite o raio: '))

area = math.pi * raio ** 2
circunferencia = 2 * math.pi * raio 
diametro = 2 * raio

print(f'''Dado o raio: {raio}
O diâmetro é: {diametro}
A circunferência é: {circunferencia:.2f}
A área é: {area:.2f}²''')