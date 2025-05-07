nome = input('Informe seu nome: ')
print ('''
    Você é estudante 
        [ 1 ] SIM
        [ 2 ] NÂO''')
est = int (input(''))
idade = int (input('Informe sua idade: '))

if est == 2:
    print ('{}, você não tem DIREITO ao voto'.format(nome))
elif est == 1:
    if est == 1 and idade > 17:
        print('Você não pode votar!')
    elif est == 1 and idade < 18:
        print ('{}, você TEM DIREITO ao voto'.format(nome))
