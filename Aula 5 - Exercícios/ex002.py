CONVERSOR = 60
horas = 1
minutos = 34

print('Você finalizou a prova em {}:{}h\n'
      'Equivale a {} minutos\n'
      'Equivale a {} segundos'.format(
    horas, minutos, (horas * CONVERSOR) + minutos, (horas * CONVERSOR * CONVERSOR) + (minutos * CONVERSOR)))
