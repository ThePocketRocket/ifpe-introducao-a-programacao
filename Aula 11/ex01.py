str1 = input('Digite seu texto: ')
str2 = input('Digite outro texto: ')
compr_str1 = len(str1)
compr_str2 = len(str2)

print(f'A string: {str1}    Possui {compr_str1} caracteres')
print(f'A string: {str2}    Possui {compr_str2} caracteres')

if compr_str1 == compr_str2:
    print('As strings digitadas tem o mesmo tamanho.')
    if str1 == str2: print('O conteúdo das Strings são iguais.')
else:
    print('As strings digitadas possuem tamanhos diferentes.\nO conteúdo das Strings são diferentes.')
