import random
def sortowanie(tablica):


    mniejsze = []
    rowne = []
    wieksze = []

    if len(tablica) > 1:
        pivot = tablica[0]
        for x in tablica:
            if x < pivot:
                mniejsze.append(x)
            elif x == pivot:
                rowne.append(x)
            elif x > pivot:
                wieksze.append(x)

        return sortowanie(mniejsze)+rowne+sortowanie(wieksze)

    else:
        return tablica

tablica = []
for i in range(50):
    tablica.append(random.randint(0,100))
print(tablica,"\n")

print("Posortowane:", sortowanie(tablica))
