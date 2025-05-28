nom = input('Informe seu nome: ')
invert = nom[::-1]
substA = invert.replace('a', '@')
substE = substA.replace('e', '3')
substI = substE.replace('i', '!')
substO = substI.replace('o', '0')
substU = substO.replace('u', '¨')
print('''A senha de: {} é {}'''.format(nom, substU))
