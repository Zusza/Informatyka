# Zad.1.1
# def przestaw(n):
#     if n < 10:
#         return n

#     r = n % 100
#     n = n // 100
#     r = (r % 10) * 10 + r // 10

#     return r + 100 * przestaw(n)

# print(przestaw(316498))

# Zad.1.2
# n = 316498
# k = len(str(n))
# w = k // 2 + 1
# print(w)

# Zad.1.3
# def przestaw(n):
#     wynik = 0
#     mnoznik = 1

#     while n >= 10:
#         r = n % 100
#         n = n // 100

#         r = (r % 10) * 10 + r // 10

#         wynik += r * mnoznik
#         mnoznik *= 100

#     wynik += n * mnoznik
#     return wynik
# print(przestaw(316498))

# Zad.2.1
# with open("symbole.txt") as plik:
#     napisy = [linia.strip() for linia in plik]

# licznik = 0

# for napis in napisy:
#     if napis == napis[::-1]:
#         print(napis)
#         licznik += 1

# print("Liczba palindromów: ", licznik)

# Zad.2.2
# with open("symbole.txt") as plik:
#     napisy = [linia.strip() for linia in plik]

# licznik = 0

# for napis in napisy:
#     znaleziono = False
#     for kolumna in range(2):
#         znak = napis[kolumna]

#         if (napis[kolumna + 1] == znak and
#             napis[kolumna + 2] == znak and
#             napis[kolumna + 3] == znak and
#             napis[kolumna + 4] == znak and
#             napis[kolumna + 5] == znak and
#             napis[kolumna + 6] == znak and
#             napis[kolumna + 7] == znak and
#             napis[kolumna + 8] == znak and
#             napis[kolumna + 9] == znak and
#             napis[kolumna + 10] == znak):
#             znaleziono = True
#     if znaleziono:
#         licznik += 1
# print("Liczba kwadratów 3x3: ", licznik)

# Zad.2.3
# def na_dziesietny(napis):
#     wynik = 0

#     for znak in napis:
#         if znak == 'o':
#             cyfra = 0
#         elif znak == '+':
#             cyfra = 1
#         else:
#             cyfra = 2
#         wynik = wynik * 3 + cyfra
#     return wynik
# print(na_dziesietny("o+*"))

# Zad.2.4
# def na_dziesietny(napis):
#     wynik = 0

#     for znak in napis:
#         if znak == 'o':
#             cyfra = 0
#         elif znak == '+':
#             cyfra = 1
#         else:
#             cyfra = 2
#         wynik = wynik * 3 + cyfra
#     return wynik

# def na_symbole(liczba):
#     if liczba == 0:
#         return "o"

#     wynik = ""

#     while liczba > 0:
#         reszta = liczba % 3

#         if reszta == 0:
#             wynik = "o" + wynik
#         elif reszta == 1:
#             wynik = "+" + wynik
#         else:
#             wynik = "*" + wynik

#         liczba //= 3
#     return wynik

# with open("symbole.txt") as plik:
#     napisy = [linia.strip() for linia in plik]

# Zad.3.1
# def nwd(a, b):
#     a = abs(a)
#     b = abs(b)

#     while b != 0:
#         a, b = b, a % b
#     return a

# with open("dron.txt") as plik:
#     pary = [list(map(int, linia.split())) for linia in plik]

# licznik = 0

# for a, b in pary:
#     if nwd(a, b) > 1:
#         licznik += 1
# print("Liczba par: ", licznik)

# Zad.3.2
# with open("dron.txt") as plik:
#     pary = [list(map(int, linia.split())) for linia in plik]

# x = 0
# y = 0
# licznik = 0

# for a, b in pary:
#     x += a
#     y += b

#     if 0 < x < 5000 and 0 < y < 5000:
#         licznik += 1

# print("Liczba punktów w kwadracie: ", licznik)

# Zad.3.3
# with open("dron.txt") as plik:
#     pary = [list(map(int, linia.split())) for linia in plik]

# punkty = [(0, 0)]
# x = 0
# y = 0

# for a, b in pary:
#     x += a
#     y += b
#     punkty.append((x, y))

# znaleziono = False

# for i in range(len(punkty)):
#     for j in range(i + 1, len(punkty)):
#         for k in range(j + 1, len(punkty)):
#             x1, y1 = punkty[i]
#             x2, y2 = punkty[j]
#             x3, y3 = punkty[k]

#             if (2 * x2 == x1 + x3 and 2 * y2 == y1 + y3):
#                 print("Początek: ", punkty[i])
#                 print("Środkowy: ", punkty[j])
#                 print("Koniec: ", punkty[k])
#                 znaleziono = True
#                 break
#         if znaleziono:
#             break
#     if znaleziono:
#         break
# if not znaleziono:
#     print("Nie ma punktów")
