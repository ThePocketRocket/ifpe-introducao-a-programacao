str_1 = input('Digite um texto: ')
str_2 = ''

for i in range(len(str_1)):
    encontrou = 97 <= ord(str_1[i]) <= 122
    if encontrou:
        str_2 += chr(ord(str_1[i]) - 32)
    else:
        str_2 += str_1[i]

print(str_2)