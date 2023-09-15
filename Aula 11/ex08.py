str_1 = input('Digite a primeira string: ')
str_2 = input('Digite a segunda string: ')

find_str_1 = str_1.lower()
find_str_2 = str_2.lower()
print(f'"{str_2}" encontrado na posição {find_str_1.find(find_str_2)} de "{str_1}"')