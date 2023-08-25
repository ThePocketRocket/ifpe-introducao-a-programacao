peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc >= 40:
    status = 'Obesidade Mórbida'
elif 35 <= imc < 40:
    status = 'Obesidade Moderada'
elif 30 <= imc < 35:
    status = 'Obesidade Leve'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 20 <= imc < 25:
    status = 'Normal'
else:
    status = 'Abaixo do Normal'

print(f'''Seu IMC é: {imc}
Você está na classificação: {status}''')