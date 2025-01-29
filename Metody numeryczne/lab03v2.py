# zad 2
plik_palindromy = open("palindromy.txt").read().split()

def czyPalindrom(tekst):
    p = 0
    k = len(tekst) - 1
    while (p < k):
        if tekst[p] != tekst[k]:
            return False
        p += 1
        k -= 1
    return True

palindromy = []
for t in plik_palindromy:
    if czyPalindrom(t):
        palindromy.append(t)
print(palindromy)
print(len(palindromy))
print()

# zad 3
plik_anagramy = [tekst.split() for tekst in open("anagramy.txt").readlines()]

def czyAnagramy(t1, t2):
    if len(t1) != len(t2):
        return False
    tab = [0 for i in range(26)]    # tylko 26 znaków od 'A' do 'Z' włącznie
    for z in t1:
        tab[ ord(z) - 65 ] += 1     # 'A' ma kod 65, żeby było na indeksie 0 trzeba odjąć 65 od ord('A')
    for z in t2:
        tab[ ord(z) - 65 ] -= 1
    for i in range(26):
        if tab[i] != 0:
            return False
    return True

anagramy = []
for t in plik_anagramy:
    if czyAnagramy(t[0], t[1]):
        anagramy.append(t)

print(anagramy)
print(len(anagramy))
print()

# zad 5
def odbicie(tekst):
    N = len(tekst)
    wyjscie = ""
    for i in range(-1, -N-1, -1):
        wyjscie += tekst[i]
    return wyjscie

tekst = "Ala ma kota."
print(tekst)
print(odbicie(tekst))
print()

# zad 1
def szukanieBF(tekst, wzorzec):
    M = len(wzorzec)
    N = len(tekst)
    indeksy = []
    for i in range(N-M+1):
        flaga = True
        for j in range(M):
            if tekst[i+j] != wzorzec[j]:
                flaga = False
                break
        if flaga:
            indeksy.append(i)
    return indeksy

tekst = "BAABABAAABBAAB"
wzorzec = "AAB"
print(szukanieBF(tekst, wzorzec))
print()

# zad 4
def najdluzszyPalindrom(tekst):
    N = len(tekst)
    Z = N
    while (Z > 1):
        for i in range(N - Z + 1):
            tmp = ""
            for j in range(i, i + Z):
                tmp += tekst[j]
            if czyPalindrom(tmp):
                return [i, tmp]
        Z -= 1

print(najdluzszyPalindrom("ZZABCDCBABB"))