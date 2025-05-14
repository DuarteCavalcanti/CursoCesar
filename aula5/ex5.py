import random
corredor1 = corredor2 = corredor3 = 0
primeiro = segundo = terceiro = ""

for i in range(11):
    if corredor2 < 10:
        if corredor2 == 0:
            corredor2 += 1
            print(f"Corredor 1 avançou {corredor1}")
        else:
            corredor2 += random.randint(1, 3)
            if corredor2 > 10:
                corredor2 = 10
            print(f"Corredor 2 avançou {corredor2}")
    if corredor1 < 10:
        if corredor1 == 0:
            corredor1 += 1
            print(f"Corredor 1 avançou {corredor1}")
        else:
            corredor2 += random.randint(1, 3)
            if corredor2 > 10:
                corredor2 = 10
            print(f"Corredor 2 avançou {corredor2}")
    if corredor3 < 10:
        if corredor3 == 0:
            corredor3 += 1
            print(f"Corredor 3 avançou {corredor3}")
        else:
            corredor1 += random.randint(1, 3)
            if corredor3 > 10:
                corredor3 = 10
            print(f"Corredor 3 avançou {corredor3}")



  
