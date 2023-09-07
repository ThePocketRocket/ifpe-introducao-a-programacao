user = input('Digite seu nome de usuário: ')
user_upper = user.upper()

for i in range(len(user_upper)):
    print(user_upper[-i-1]) #-i-1 inverte a leitura da string