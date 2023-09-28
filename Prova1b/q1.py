string = input('Digite uma palavra: ')

string2 = ''
for i in range(len(string)):
    string2 = string[:i+1]
    print(string2)

string2 = ''
for i in range(len(string)):
    string2 = string[i:]
    print(string2)