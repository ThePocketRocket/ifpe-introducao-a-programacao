str_1 = input('Digite a String: ')
str_2 = ''
l1 = input('Digite a letra l1: ')
l2 = input('Digite a letra l2: ')

for i in range(len(str_1)):
    if str_1[i] == l1:
        str_2 += l2
    elif str_1[i] == l2:
        str_2 += l1
    else:
        str_2 += str_1[i]

print(str_2)
