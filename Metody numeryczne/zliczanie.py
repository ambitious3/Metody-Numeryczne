import random
random.seed(7)
dane = []
for i in range(50000):
    dane.append(random.randint(0, 500000))


def countingSort(lista):
    C = []
    maxN = max(lista)
    for i in range(0, maxN+1):
        C.append(0)
    for i in range(0, len(lista)):
        C[ lista[i] ] += 1
    wynik = []
    for i in range(maxN + 1):
        for j in range(C[i]):
            wynik.append(i)
    return wynik


countingSort(dane)


