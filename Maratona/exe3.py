vidas = int(input('Informe a quantidade de vidas que você possui: '))
if vidas == 0:
    print('Gamer Over')
elif vidas >= 1 and vidas <= 2:
    print('Cuidado!')
elif vidas >= 3 and vidas <= 5:
    print('Está indo bem!')
