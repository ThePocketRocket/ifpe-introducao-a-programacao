numero = int(input('Digite um numero inteiro, menor que 1000: '))

if numero < 1000:
    centenas = int(numero / 100)
    dezenas = int(numero % 100) // 10
    unidades = int(numero % 10)

    resultado = ''

    if centenas > 1:
        resultado += f'{centenas} centenas'
    elif centenas == 1:
        resultado += f'{centenas} centena'
    else:
        resultado = resultado

    if centenas > 0 and dezenas > 0 and unidades > 0:
        resultado += ', '
    if centenas > 0 and dezenas > 0 and unidades == 0:
        resultado += ' e '

    if dezenas > 1:
        resultado += f'{dezenas} dezenas'
    elif dezenas == 1:
        resultado += f'{dezenas} dezena'
    else:
        resultado = resultado

    if (centenas > 0 or dezenas > 0) and unidades > 0:
        resultado += ' e '

    if unidades > 1:
        resultado += f'{unidades} unidades'
    elif unidades == 1:
        resultado += f'{unidades} unidade'
    else:
        resultado = resultado

    print(resultado)

else:
    print('Valor fora do escopo.')
