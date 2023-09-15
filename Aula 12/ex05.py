altura = list()
idade = list()
contador_13 = 0
media_altura = 0
acima_media = 0
quantidade_alunos = 0

while True:
    buffer_idade = float(input('Digite a idade do aluno: '))
    buffer_altura = float(input('Digite a altura do aluno: '))
    if buffer_altura == -1 or buffer_idade == -1:
        break
    idade.append(buffer_idade)
    altura.append(buffer_altura)

    if idade[quantidade_alunos] > 13:
        contador_13 += 1
    else:
        media_altura += altura[quantidade_alunos]
    quantidade_alunos += 1
media_altura = media_altura / (quantidade_alunos - contador_13)

for i in range(quantidade_alunos):
    if idade[i] > 13 and altura[i] > media_altura:
        acima_media += 1

print(f'{acima_media} alunos com mais de 13 anos têm altura maior que a média de {media_altura}cm' )