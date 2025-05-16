import random
corredor1 = corredor2 = corredor3 = 0
primeiro = segundo = terceiro = ""

for i in range(11):
    if corredor1 < 10:
        corredor1 += random.randint(1, 3)
        if corredor1 > 10:
            corredor1 = 10
        print(f"Corredor 1 avançou para {corredor1} metros")
        if corredor1 >= 10:
            if primeiro == "":
                primeiro = "Corredor 1"
            elif segundo == "" and primeiro != "Corredor 1":
                segundo = "Corredor 1"
            elif terceiro == "" and primeiro != "Corredor 1" and segundo != "Corredor 1":
                terceiro = "Corredor 1"
    
    if corredor2 < 10:
        corredor2 += random.randint(1, 3)
        if corredor2 > 10:
            corredor2 = 10
        print(f"Corredor 2 avançou para {corredor2} metros")
        if corredor2 >= 10:
            if primeiro == "":
                primeiro = "Corredor 2"
            elif segundo == "" and primeiro != "Corredor 2":
                segundo = "Corredor 2"
            elif terceiro == "" and primeiro != "Corredor 2" and segundo != "Corredor 2":
                terceiro = "Corredor 2"
    
    if corredor3 < 10:
        corredor3 += random.randint(1, 3)
        if corredor3 > 10:
            corredor3 = 10
        print(f"Corredor 3 avançou para {corredor3} metros")
        if corredor3 >= 10:
            if primeiro == "":
                primeiro = "Corredor 3"
            elif segundo == "" and primeiro != "Corredor 3":
                segundo = "Corredor 3"
            elif terceiro == "" and primeiro != "Corredor 3" and segundo != "Corredor 3":
                terceiro = "Corredor 3"

    if primeiro != "" and segundo != "" and terceiro != "":
        break

print("Ordem de chegada:")
print(f"1º lugar: {primeiro}")
print(f"2º lugar: {segundo}")
print(f"3º lugar: {terceiro}")
