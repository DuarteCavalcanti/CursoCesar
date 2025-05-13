numeros = int(input("Digite um numero:"))
primeira_vez = True
soma = 0
for i in range(1, numeros +1):
  numero = int(input("Digite um numero para verificação:"))
  if primeira_vez:
    menor = numero
    maior = numero
    primeira_vez = False

  if maior < numero:
    maior = numero
  if menor > numero:
    menor = numero

  soma += numero

print(f" O maior numero é {maior}")
print(f"O menor numero é {menor}")
print(f"A soma dos numeros é {soma} ")