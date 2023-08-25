idade1 = 10
idade2 = 12
idade3 = 15
idade4 = 17

media1 = (idade1 + idade2 + idade3 + idade4) / 4
print('A média das idades é: {}'.format(media1))
media2 = (idade1 + idade2 + idade3 + idade4 + 16) / 5
variacao_media = ((media2 * 100)/media1) - 100
print('A nova média vai ser {}\n'
      'Caso seja introduzido um individuo com 16 anos, a média vai variar em {:.2f}%.'.format(media2, (variacao_media)))