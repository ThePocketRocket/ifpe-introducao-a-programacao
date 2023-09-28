n = int(input('Digite o n-ésimo termo da sequência de Fibonacci: '))

ant = 0
fibo = 1
for i in range(n):
    print(fibo)
    temp = fibo
    fibo += ant
    ant = temp
