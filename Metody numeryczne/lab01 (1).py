dane = [int(i) for i in open("dane.txt").readlines()]

def bisekcja(tabela, szukana):
    lb = 0
    ub = len(tabela) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if tabela[mid] < szukana:
            lb = mid + 1
        elif tabela[mid] > szukana:
            ub = mid - 1
        else:
            return mid
    return None

print(bisekcja(dane, 188))

# plik1 = [int(i) for i in open("sort1.txt", "r").readlines()]
# plik2 = [int(i) for i in open("sort2.txt", "r").readlines()]
# plik3 = [int(i) for i in open("sort3.txt", "r").readlines()]
#
# def minimum(tabela):
#     zwr_ind = 0
#     for i in range(1, len(tabela)):
#         if tabela[zwr_ind] > tabela[i]:
#             zwr_ind = i
#     return zwr_ind
#
# def maksimum(tabela):
#     zwr_ind = 0
#     for i in range(1, len(tabela)):
#         if tabela[zwr_ind] < tabela[i]:
#             zwr_ind = i
#     return zwr_ind
#
# print(plik1[minimum(plik1)], minimum(plik1))
# print(plik1[maksimum(plik1)], maksimum(plik1))

# import math
# p = 500
# print(math.sqrt(p), '\n')
# a = 1
# delta = 0.00001
# licz = 0
# while a*a < p:
#     licz += 1
#     a += delta
# print(a)
# print(licz)
# print()
# B = p
# A = 1
# Eps = 0.000001
# licz = 0
# while (A-B) > Eps or (A-B) < -Eps:
#     A = (A+B)/2
#     B = p/A
#     licz += 1
# print((A+B)/2)
# print(licz)