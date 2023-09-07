dna = input('Digite a cadeia do DNA: ').upper()

dna_complementar = ''
for i in range(len(dna)):
    match dna[i]:
        case 'A':
            dna_complementar += 'T'
        case 'T':
            dna_complementar += 'A'
        case 'C':
            dna_complementar += 'G'
        case 'G':
            dna_complementar += 'C'

print(dna_complementar)