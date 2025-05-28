nom = input('Informe seu nome: ')
quant = len(nom)
ult = nom[-1]
print('''
       Nome: {}
       Senha {}{}{}'''.format(nom, nom[0], quant, ult))
