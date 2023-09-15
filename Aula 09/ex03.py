n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 + 1 < n2:
    while n1 + 1 < n2:
        n1 += 1
        if n1 % 2 == 0:
            print (n1)
        
elif n1 - 1 > n2:
    while n1 - 1 > n2:
        n1 -= 1
        if n1 % 2 == 0:
            print (n1)
else:
    print('Os números são iguais!')