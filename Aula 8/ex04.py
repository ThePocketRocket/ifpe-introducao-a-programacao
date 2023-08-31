valor = float(input('Digite o valor a ser pago: '))

while(True):
    escolha = int(input('''Código                  Condição de pagamento
1           À vista em dinheiro ou cheque, recebe 10% de desconto
2           À vista no cartão de crédito, recebe 15% de desconto
3           Em duas vezes, preço normal de etiqueta sem juros
4           Em três vezes, preço normal de etiqueta mais juros de 10%
5           Em seis vezes, preço normal de etiqueta mais juros de 20%
Digite o código: '''))

    match escolha:
        case 1:
            valor_final = valor - (valor * 0.1)
            break
        case 2:
            valor_final = valor - (valor * 0.15)
            break
        case 3:
            valor_final = valor
            break
        case 4:
            valor_final = valor + (valor * 0.1)
            break
        case 5:
            valor_final = valor + (valor * 0.2)
            break
        case _:
            print('Método de pagamento inválido')

print(f'O valor do pagamento é de: R${valor_final}')