def getMask():
    m = ""
    i = ord('0')
    k = ord('9') + 1
    while i < k:
        m += chr(i)
        i += 1
    i = ord('A')
    k = ord('Z') + 1
    while i < k:
        m += chr(i)
        i += 1
    return m
maska = getMask()

def dec2Any(liczba, system):
    tmp = ""
    while liczba > 0:
        tmp += maska[liczba%system]
        liczba //= system
    i = len(tmp)
    sliczba = ""
    while i > 0:
        sliczba += tmp[i - 1]
        i -= 1
    return sliczba

print("Zad 4:")
print(dec2Any(215, 12))

def bisection(tabela, szukana, rozmiar):
    lb = 0
    ub = rozmiar - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if tabela[mid] < szukana:
            lb = mid + 1
        elif tabela[mid] > szukana:
            ub = mid - 1
        else:
            return mid
    return None

def toUpper(znak):
    val = ord(znak)
    if val >= 97 and val <= 122:
        return chr( val - 32 )
    return znak

def any2Dec(sliczba : str, system : int):
    liczba = 0
    i = 0
    k = len(sliczba)
    while i < k:
        liczba *= system
        liczba += bisection(maska, toUpper(sliczba[i]), system)
        i += 1
    return liczba

print("\nZad 5:")
print(any2Dec("5312", 7))
print(any2Dec("f2", 16))



def simpleRLE(tekst):
    obecny = tekst[0]
    dlugosc = 1
    i = 1
    wyjscie = ""
    while i < len(tekst):
        while i < len(tekst) and obecny == tekst[i]:
            dlugosc += 1
            i += 1
        wyjscie += str(dlugosc) + obecny
        if i < len(tekst):
            dlugosc = 1
            obecny = tekst[i]
        i += 1
    if wyjscie[-1] != tekst[-1]:
        wyjscie += str(dlugosc) + tekst[-1]
    return wyjscie

print("\nZad 6 v1:")
print(simpleRLE("AAABBAAAC"))

def simpleRLEv2(tekst):
    obecny = tekst[0]
    dlugosc = 1
    i = 1
    wyjscie = ""
    while i < len(tekst):
        while i < len(tekst) and obecny == tekst[i]:
            dlugosc += 1
            i += 1
        if dlugosc > 1:
            wyjscie += str(dlugosc)
        wyjscie += obecny
        if i < len(tekst):
            dlugosc = 1
            obecny = tekst[i]
        i += 1
    if wyjscie[-1] != tekst[-1]:
        if dlugosc > 1:
            wyjscie += str(dlugosc)
        wyjscie += tekst[-1]
    return wyjscie

print("\nZad 6 v2:")
print(simpleRLEv2("AAABBAAAC"))

def isDigit(znak):
    val = ord(znak)
    if (val >= 48 and val <= 57):
        return True
    return False

def simpleDeRLE(tekst):
    cyfry = '1'
    i = 0
    if isDigit(tekst[0]):
        cyfry = tekst[0]
        i = 1
    wyjscie = ""
    while i < len(tekst):
        while isDigit(tekst[i]):
            cyfry += tekst[i]
            i += 1
        j = 0
        k = any2Dec(cyfry,10)
        while j < k:
            wyjscie += tekst[i]
            j += 1
        cyfry = ""
        i += 1
        if i < len(tekst) and not isDigit(tekst[i]):
            cyfry = '1'
    return wyjscie

print("\nZad 7:")
print(simpleDeRLE("B3A2B3A1C"))
print(simpleDeRLE("1B3A2B3A1C"))