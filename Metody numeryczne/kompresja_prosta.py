def dec2BinN(liczba, size):
    tmp = ""
    while liczba > 0:
        tmp += str(liczba%2)
        liczba //= 2
    i = len(tmp)
    while i < size:
        tmp += '0'
        i += 1
    sliczba = ""
    while i > 0:
        sliczba += tmp[i - 1]
        i -= 1
    return sliczba

def bin2Dec(sliczba):
    liczba = 0
    i = 0
    k = len(sliczba)
    while i < k:
        liczba *= 2
        liczba += int(sliczba[i])
        i += 1
    return liczba

def getDict(tekst):
    tab = [0 for i in range(128)]
    for znak in tekst:
        tab[ ord(znak) ] = 1
    i = 0
    slownik = ""
    while i < 128:
        if tab[i] == 1:
            slownik += chr(i)
        i += 1
    return slownik

def bisection(tabela, szukana):
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

import math

def compression(tekst):
    print()
    k = len(tekst)
    s = getDict(tekst)
    X = len(s)
    N = math.ceil(math.log2(X))
    R = (8 - (3 + k*N)%8)%8
    biny = [dec2BinN(i, N) for i in range(X)]
    print("\u001b[34mPrzygotowania.\u001b[32m")
    print("\u001b[32mDlugosc tekstu:\u001b[33m", k)
    print("\u001b[32mSlownik:\u001b[33m", s)
    print("\u001b[32mDlugosc slownika:\u001b[33m", X)
    print("\u001b[32mLiczba bitow na kod znaku:\u001b[33m", N)
    print("\u001b[32mNadmiarowe:\u001b[33m", R)
    print("\u001b[32mMapa bitów:\u001b[33m", biny)
    zwrotka = chr(X)
    zwrotka += s
    skompresowany = dec2BinN(R, 3)
    for znak in tekst:
        ind = bisection(s, znak)
        skompresowany += biny[ind]
    i = 0
    while i < R:
        skompresowany += '1'
        i += 1

    i = 0
    print("\n\u001b[34mPrzebieg kompresji.\u001b[32m")
    while i < len(skompresowany):
        tmp = skompresowany[i:i+8]
        val = bin2Dec(tmp)
        print("\u001b[37m" + tmp, "\u001b[0m-\u001b[35m",val, "\u001b[0m-\u001b[36m", chr(val))
        zwrotka += chr(val)
        i += 8
    print("\u001b[0m")

    return zwrotka

def decompression(skompresowany):
    X = ord(skompresowany[0])
    N = math.ceil(math.log2(X))
    biny = [dec2BinN(i, N) for i in range(X)]
    s = skompresowany[1:1+X]
    i = 1 + X
    tmp = dec2BinN(ord(skompresowany[i]),8)
    R = bin2Dec(tmp[:3])
    tmp = tmp[3:]
    i += 1
    while i < len(skompresowany):
        tmp += dec2BinN(ord(skompresowany[i]),8)
        i += 1
    tmp = tmp[:-R]
    i = 0
    dekompresowany = ""
    while i < len(tmp):
        dekompresowany += s[ bisection(biny, tmp[i:i+N]) ]
        i += N
    return dekompresowany



# print(dec2BinN(5, 6))
# print(bin2Dec("11001"))
# print(getDict("DDAACAABABBBBAACCCCAAAD"))

oryginalny = "vxcmvnxcmnvmxcnmxc"
print("Oryginalny:\t\t", oryginalny)
print("Rozmiar:", len(oryginalny))
skompresowany = compression(oryginalny)
print("Skompresowany:", skompresowany)
print("Rozmiar:", len(skompresowany))
dekompresowany = decompression(skompresowany)
print("Zdekompresowany:", dekompresowany)
print("Rozmiar:", len(dekompresowany))
print(oryginalny == dekompresowany)