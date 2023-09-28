data = input('Digite a data: ')

mes = data[3:5]
match mes:
    case '01':
        data = data.replace('/01/', '/Janeiro/')
    case '02':
        data = data.replace('/02/', '/Fevereiro/')
    case '03':
        data = data.replace('/03/', '/Março/')
    case '04':
        data = data.replace('/04/', '/Abril/')
    case '05':
        data = data.replace('/05/', '/Maio/')
    case '06':
        data = data.replace('/06/', '/Junho/')
    case '07':
        data = data.replace('/07/', '/Julho/')
    case '08':
        data = data.replace('/08/', '/Agosto/')
    case '09':
        data = data.replace('/09/', '/Setembro/')
    case '10':
        data = data.replace('/10/', '/Outubro/')
    case '11':
        data = data.replace('/11/', '/Novembro/')
    case '12':
        data = data.replace('/12/', '/Dezembro/')

print(data)