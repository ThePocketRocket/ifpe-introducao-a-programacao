str_1 = input('Digite a string: ')

lower_str_1 = str_1.lower()
esp = str_1.count(' ')
a = str_1.count('a')
e = str_1.count('e')
i = str_1.count('i')
o = str_1.count('o')
u = str_1.count('u')

print(f'''A String "{str_1}" contém:
{esp} espaços
{a} letras "a"
{e} letras "e"
{i} letras "i"
{o} letras "o"
{u} letras "u"''')