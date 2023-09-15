str_1 = input('Digite um texto: ')
str_2 = ''

for _ in range(len(str_1)):
    str_2 += chr(ord(str_1[_]) + 1)
print(str_2)