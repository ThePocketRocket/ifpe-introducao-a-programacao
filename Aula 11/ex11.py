str_1 = input('Digite a string: ')

lower_str = str_1
str_2 = ''
conta_letra = 0
for _ in range(len(str_1)):
    conta_letra = lower_str.count(lower_str[_])
    if str_2.find(lower_str[_]) == -1 and lower_str[_] != ' ':
        str_2 += lower_str[_]
        print(f'{str_1[_].upper()}: {conta_letra}')
