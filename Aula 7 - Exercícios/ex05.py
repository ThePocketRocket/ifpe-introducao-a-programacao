salario =  float(input('Digite seu salário: '))
cod_cargo = int(input('Digite o código do seu cargo: '))

if cod_cargo == 310:
    aumento = salario * 0.05
    novo_salario = salario + aumento
elif cod_cargo == 456:
    aumento = salario * 0.075
    novo_salario = salario + aumento
elif cod_cargo == 885:
    aumento = salario * 0.1
    novo_salario = salario + aumento
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento

print(f'''Salário antigo: R${salario}
Salário atualizado: R${novo_salario}
Valor do Aumento: R${aumento}''')