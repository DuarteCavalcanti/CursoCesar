# idade = int (input('Informe sua idade: '))
# if idade < 18:
#     print ('Você não pode votar')
# elif idade > 18:
#     print('Você pode votar!')
# else:
#     print ('Impossivel')
    
    
print(f"{"Você pode votar" if int(input("Informe sua idade: ")) < 17 else "Você não pode votar"}")