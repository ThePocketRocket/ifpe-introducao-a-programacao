str_1 = input('Digite a primeira string: ')
str_2 = input('Digite a segunda string: ')

lower_str_1 = str_1.lower()
lower_str_2 = str_2.lower()
str_3 = ''
for i in range(len(str_1)):
    position = lower_str_2.find(lower_str_1[i])
    if position != -1 and str_3.lower().find(lower_str_1[i]) == -1 and lower_str_1[i] != ' ':
        str_3 += str_1[i]

print(f'''1ª String: {str_1}
2ª String: {str_2}
Resultado: {str_3}''')
