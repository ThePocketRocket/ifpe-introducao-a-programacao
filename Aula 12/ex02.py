lista_impar = list()
lista_par = list()

for i in range(10):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'A lista impar é {lista_impar}\nA lista par é {lista_par}')
