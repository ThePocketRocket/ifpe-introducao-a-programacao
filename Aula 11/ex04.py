text = input('Digite um texto: ')
text2 = text

for i in range(len(text)):
    print(text2)
    buffer = str(text[i])
    text2 = text2.replace(buffer, '')
