l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do segundo lado: '))
l3 = float(input('Digite o tamanho do terceiro lado: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and (l1 > 0 or l2 > 0 or l3 > 0):
    if l1 == l2 == l3:
        classe = 'equilátero'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        classe = 'isósceles'
    else:
        classe = 'escaleno'
else:
    classe = 'impossível'

print(f'Dado os lados {l1}, {l2} e {l3} o triângulo é: {classe}')