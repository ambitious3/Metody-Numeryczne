print("\nZad 1:")
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
    return -1

def slownik(w):
    tab = [0 for i in range(128)]
    s = ""
    for znak in w:
        tab[ord(znak)] = 1
    for i in range(128):
        if tab[i] == 1:
            s += chr(i)
    return s

def aBM(tekst, wzorzec):
    s = slownik(wzorzec)
    dt = len(tekst)
    dw = len(wzorzec)
    i = 0
    while i < dt - dw + 1:
        j = dw - 1
        while j > -1:
            if tekst[i + j] != wzorzec[j]:
                #print(tekst[i+j], bisekcja(s, tekst[i+j]))
                if bisekcja(s, tekst[i+j]) == -1:
                    i += j + 1
                else:
                    i += 1
                break
            j -= 1
        if j == -1:
            print("znalazlem wzorzec na pozycji:", i)
            i += 1

aBM("ABCADABCJABKZCAABCADUIOPABCADWACDZAZ", "ABCAD")

print("\n\nZad 2:")
def isLower(znak):
    if znak >= 'a' and znak <= 'z':
        return True
    return False

def isUpper(znak):
    if znak >= 'A' and znak <= 'Z':
        return True
    return False

def szyfrCezara(tekst, kod):
    zaszyfrowany = ""
    for znak in tekst:
        nowy = ord(znak)
        if isLower(znak):
            nowy = (nowy + kod - 97) % 26 + 97
        elif isUpper(znak):
            nowy = (nowy + kod - 65) % 26 + 65
        zaszyfrowany += chr(nowy)
    return zaszyfrowany

print(szyfrCezara("Ala ma kota.", 3))
print(szyfrCezara(szyfrCezara("Ala ma kota.", 3), -3))

print("\n\nZad 3:")
def szyfrPrzestawieniowy(tekst, klucz, dekodowanie = False):
    zaszyfrowany = ""
    i = 0
    for znak in tekst:
        nowy = ord(znak)
        kod = ord(klucz[i])
        if dekodowanie:
            kod = - kod
        if isLower(znak):
            nowy = (nowy + kod - 97) % 26 + 97
            i += 1
        elif isUpper(znak):
            nowy = (nowy + kod - 65) % 26 + 65
            i += 1
        i %= len(klucz)
        zaszyfrowany += chr(nowy)
    return zaszyfrowany

print(szyfrPrzestawieniowy("Ala ma kota.", "koty"))
print(szyfrPrzestawieniowy(szyfrPrzestawieniowy("Ala ma kota.", "pies"), "pies", True))
