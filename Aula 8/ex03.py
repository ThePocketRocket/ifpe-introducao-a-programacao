horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
valor_da_hora = float(input('Digite o valor da sua hora trabalhada: '))
salario_bruto = valor_da_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif 1500 >= salario_bruto > 900:
    ir = salario_bruto * 0.05
elif 2500 >= salario_bruto > 1500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

inss = salario_bruto * 0.11
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
salario_liquido = salario_bruto - ir - inss - sindicato
descontos = salario_bruto - salario_liquido

print(f'''Salário bruto : {salario_bruto}
(-) IR : {ir}
(-) INSS (10%) : {inss}
(-) Sindicato (3%): {sindicato}
FGTS (11%): {fgts}
Total de descontos: {descontos}
Salário Líquido: {salario_liquido}''')