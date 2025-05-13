numero = int(input("Digite o numero para a tabuada:"))
inicio = int(input("Digite o numero de começo da tabuada:"))
fim = int(input("Digite o número de fim da tabuada"))
for i in range(inicio, fim +1):
  print(f"{numero} x {i} = {numero * i}")