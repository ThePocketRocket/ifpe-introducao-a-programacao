numero = int(input('Digite um número inteiro para saber seu fatorial: '))
fatorial = ''

contador = numero
if contador == 0 or contador == 1:
    fatorial = '1'
    res_fatorial = 1
    print(f'{numero}! = {res_fatorial}')
else:
    res_fatorial = numero
    while contador > 0:
        if contador != numero:
            res_fatorial *= contador
        
        if contador > 1:
            fatorial += f'{contador} x '
        else: 
            fatorial += f'{contador}'
        contador -= 1
    
    print(f'{numero}! = {fatorial} = {res_fatorial}')
