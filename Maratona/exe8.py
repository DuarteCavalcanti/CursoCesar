n = int(input('Informe a quantidade de pessoas na fila: '))
peso = []
for i in range(n):
    p = peso.append(int(input(f'Informe o quilo da {i+1} pessoa: ')))
x = int(input('Informe a capacidade max do elevador: '))
soma = sum(peso)
min = (soma//x) + 1
print(min)
