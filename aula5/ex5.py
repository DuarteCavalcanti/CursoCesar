import random
corredor1 = corredor2 = corredor3 = 0
primeiro = segundo = terceiro = ""

for i in range(11):
    if corredor1 < 10:
        if corredor1 == 0:
            corredor1 += 1
            print(f"Corredor 1 avançou {corredor1}")
        else: 
            corredor1 += random.randint(1, 3)
            if corredor1 > 10:
                corredor1 = 10
            print(f"Corredor 1 vançou {corredor1}")