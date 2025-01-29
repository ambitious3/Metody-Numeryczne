import time
N = [10000, 25000, 50000]
import random
random.seed(13)
for i in range(len(N)):
    plik = open("dane"+str(i)+".txt", "w")
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

for i in range(len(N)):
    print("Rozmiar: ", N[i])
    plik = open("C:\\WSB\\dane"+str(i)+".txt", "r").readlines()
    lista0 = [int(linia) for linia in plik]
    lista1 = lista0[:]
    lista2 = lista0[:]
    lista3 = lista0[:]
    lista4 = lista0[:]

    start = time.time()
    bubbleSort(lista1)
    stop = time.time()
    print("Bąbelkowe:", stop - start)

    start = time.time()
    selectionSort(lista1)
    stop = time.time()
    print("Selekcja:", stop - start)

    start = time.time()
    insertionSort(lista2)
    stop = time.time()
    print("Wstawianie:", stop - start)

    import sys
    sys.setrecursionlimit(10**4)
    start = time.time()
    mergeSort(lista3, 0, len(lista3) - 1)
    stop = time.time()
    print("Scalanie:", stop - start)

    start = time.time()
    sorted(lista4)
    stop = time.time()
    print("Systemowe (sorted()):", stop - start)

    print()