print('| p | q | (p and q) and not(p or q) |\n')
for p in [True, False]:
    for q in [True, False]:
        resultado = (p and q) and not(p or q)
        print(f'|{p:^3}|{q:^3}|{resultado:^27}|')

print('\n\n| p | q | not(p and not q) or q |\n')
for p in [True, False]:
    for q in [True, False]:
        resultado = not(p and not q) or q
        print(f'|{p:^3}|{q:^3}|{resultado:^23}|')