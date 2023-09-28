from os import system
system('cls')

strings = ['olá mundo', 'hello world', 'olá', 'daniel']

strings_slr = [] #strigs sem letras repetidas
for i, str_i in enumerate(strings):
    tem_repeticao = 0
    for d in range(len(str_i)):
        if str_i.count(str_i[d]) > 1:
            tem_repeticao = 1
            break
    if not(tem_repeticao):
        strings_slr.append(str_i)

maior_string = ''
for str_slr in strings_slr:
    if len(str_slr) > len(maior_string):
        maior_string = str_slr

print(maior_string)


