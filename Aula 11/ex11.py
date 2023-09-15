str_1 = input('Digite a string: ')

lower_str = str_1
str_2 = ''
conta_letra = 0
conta_repetido = 0
for _ in range(len(str_1)):
    conta_letra = lower_str.find(lower_str[_])
    if str_2.find(lower_str[_]) == -1:
        conta_repetido += 1
        str_2 += lower_str[_]
        print(f'{str_2[conta_repetido]}: {conta_letra}x')
