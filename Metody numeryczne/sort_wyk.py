import matplotlib.pyplot as plt
import time
N = [100*i for i in range(1, 51)]
pliki = []
import random
random.seed(234)
for i in range(len(N)):
    plik = open("dane"+str(i)+".txt", "w")
    pliki.append("dane"+str(i)+".txt")
    for i in range(N[i]):
        plik.write(str(random.randint(-5000*(i+1), 5000*(i+1))) + "\n")
    plik.close()

def bubbleSort(A):
    N = len(A)
    for i in range(N):
        for j in range(1, N):
            if A[j-1] > A[j]:
               A[j-1], A[j] = A[j], A[j-1]
    return A

def selectionSort(A):
    N = len(A)
    for i in range(N):
        ind = i
        for j in range(i+1, N):
            if A[j] < A[ind]:
                ind = j
        A[i], A[ind] = A[ind], A[i]
    return A

def insertionSort(A):
    N = len(A)
    for i in range(N):
        x = A[i]
        j = i
        while j > 0 and x < A[j-1]:
            A[j] = A[j-1]
            j -= 1
        A[j] = x
    return A

def merge(A, p, q, r):
    temp = []
    P = p
    Q = q+1
    while P < q+1 and Q < r+1:
        if A[P] < A[Q]:
            temp.append(A[P])
            P += 1
        else:
            temp.append(A[Q])
            Q += 1
        if P == q+1:
            while Q < r+1:
                temp.append(A[Q])
                Q += 1
        else:
            while P < q+1:
                temp.append(A[P])
                P += 1
    N = len(temp)
    for i in range(N):
        A[i + p] = temp[i]


def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)
    return A

def Partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return A

rozmiarami = []
babelkowe = []
selekcja = []
wstawianie = []
scalanie = []
szybkie = []
iterator = 0
for nazwa in pliki:
    lista = []
    plik = open(nazwa, "r").readlines()
    lista0 = [int(linia) for linia in plik]
    lista1 = lista0[:]
    lista2 = lista0[:]
    lista3 = lista0[:]
    lista4 = lista0[:]

    print("Rozmiar:", len(lista1))
    start = time.time()
    bubbleSort(lista1)
    stop = time.time()
    babelkowe.append(stop - start)
    lista.append(stop - start)
    print("Bąbelkowe:", stop - start)

    start = time.time()
    selectionSort(lista1)
    stop = time.time()
    selekcja.append(stop - start)
    lista.append(stop - start)
    print("Selekcja:", stop - start)

    start = time.time()
    insertionSort(lista2)
    stop = time.time()
    wstawianie.append(stop - start)
    lista.append(stop - start)
    print("Wstawianie:", stop - start)

    import sys
    sys.setrecursionlimit(10**4)
    start = time.time()
    mergeSort(lista3, 0, len(lista3) - 1)
    stop = time.time()
    scalanie.append(stop - start)
    lista.append(stop - start)
    print("Scalanie:", stop - start)
    rozmiarami.append(lista)

    start = time.time()
    quickSort(lista4, 0, len(lista4) - 1)
    stop = time.time()
    szybkie.append(stop - start)
    lista.append(stop - start)
    print("Szybkie:", stop - start)
    rozmiarami.append(lista)
    print()

Y = [babelkowe, selekcja, wstawianie, scalanie, szybkie]

klucze = ["Bąbelkowe", "Selekcja", "Wstawianie", "Scalanie", "Szybkie"]
kolory = ['b', 'g', 'r', 'c', 'm', 'y']

for i in range(len(klucze)):
    plt.plot(N, Y[i], label=klucze[i], 	color=kolory[i], linewidth=2, marker='*', 	markersize=10, markerfacecolor=kolory[i+1])
plt.title("Porownanie zbiorcze")
plt.legend()
plt.savefig("zbiorcze.png")
plt.show()

# for j in range(len(N)):
#     for i in range(len(rozmiarami[j])):
#         plt.bar(klucze[i], rozmiarami[j][i], color=kolory[i], width=0.4)
#     plt.title("Rozmiar: " + str(N[j]))
#     plt.savefig("rozmiar_" + str(N[j]) + ".png")
#     plt.show()