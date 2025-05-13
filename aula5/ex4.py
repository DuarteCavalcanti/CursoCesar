soma = 0
for i in range(1, 101):
  if i % 2 != 0:
   soma += i
   print(i)
print(f"A soma dos numero impares é {soma}")