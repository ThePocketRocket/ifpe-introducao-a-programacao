altura = list()
idade = list()
contador_13 = 0
media_altura = 0
acima_media = 0

for i in range(5):
    idade.append(float(input('Digite a idade do aluno: ')))
    altura.append(float(input('Digite a altura do aluno: ')))
    if idade[i] > 13:
        contador_13 += 1
    else:
        media_altura += altura[i]
media_altura = media_altura / (5 - contador_13)

for i in range(5):
    if idade[i] > 13 and altura[i] > media_altura:
        acima_media += 1

print(f'{acima_media} alunos com mais de 13 anos têm altura maior que a média de {media_altura}cm' )