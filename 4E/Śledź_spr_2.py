# Wydawanie reszty
# Z.1
# def min_liczba_nominalow(nominaly, k):
#     max = k + 1
#     ln = [max] * (k + 1)
#     ln[0] = 0

#     for i in range(1, k + 1):
#         for j in nominaly:
#             if i >= j and ln[i - j] + 1 < ln[i]:
#                 ln[i] = ln[i - j] + 1
#     if ln[k] == max:
#         print("-1")
#     else:
#         print("Minimalna liczba nominałów", ln[k])

# plik = open("C:\\Users\\zuzan\\Desktop\\nominaly.txt", "r")
# nominaly = list(map(int, plik.read().split()))
# plik.close()
# # print(nominaly)

# k = int(input("Podaj kwotę: "))

# min_liczba_nominalow(nominaly, k)

# Z.2
# def min_licz_nomi(nominaly, k):
#     max = k + 1
#     ln = [max] * (k + 1)
#     prev = [-1] * (k + 1)
#     ln[0] = 0

#     for i in range(1, k + 1):
#         for j in nominaly:
#             if i >= j and ln[i - j] + 1 < ln[i]:
#                 ln[i] = ln[i - j] + 1
#                 prev[i] = j
#     x = k
#     u = []
#     while x > 0:
#         u.append(prev[x])
#         x -= prev[x]
#     wynik = {}
#     for n in u:
#         if n in wynik:
#             wynik[n] += 1
#         else:
#             wynik[n] = 1
#   if ln[k] == max:
#     print("-1")
#     return
#   else:
#     print("Min nominaly", ln[k])
#     for i in w.keys():
#         print(f"Użyte: {w[i]}x{i}")

# plik = open("C:\\Users\\zuzan\\Desktop\\nominaly.txt", "r")
# nominaly = list(map(int, plik.read().split()))
# plik.close()

# k = int(input("Podaj kwotę: "))

# min_licz_nomi(nominaly, k)

# Najdłuższy wspólny podciąg
# Z.2
# def z2(X, Y):
#     n = len(X)
#     m = len(Y)
#     D = [[0]*(m+1) for i in range(n+1)]

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if X[i - 1] == Y[j - 1]:
#                 D[i][j] = D[i][j -1] + 1
#             else:
#                 D[i][j] = max(D[i - 1][j], D[i][j - 1])
#     print("Długość: ", D[i][j])

# cg1 = list(map(int, input("Podaj 1 ciąg: ").split()))
# cg2 = list(map(int, input("Podaj 2 ciąg: ").split()))

# z2(cg1, cg2)

# Z.3
# def z3(X, Y):
#     n = len(X)
#     m = len(Y)
#     D = [[0]*(m + 1) for i in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if X[i - 1] == Y[j - 1]:
#                 D[i][j] = D[i][j - 1] + 1
#             else:
#                 D[i][j] = max(D[i - 1][j], D[i][j - 1])
#     i = n
#     j = m
#     w = []
#     while i > 0 and j > 0:
#         if X[i - 1] == Y[j - 1]:
#             w.append(X[i - 1])
#             i -= 1
#             j -= 1
#         else:
#             if D[i - 1][j] >= D[i][j - 1]:
#                 i -= 1
#             else:
#                 j -= 1
#     print("Wynik: ", w[::-1])

# cg1 = list(map(int, input("Podaj 1 ciąg:").split()))
# cg2 = list(map(int, input("Podaj 2 ciąg:").split()))

# z3(cg1, cg2)

# Z.4
# def z4(X, Y):
#     n = len(X)
#     m = len(Y)
#     D = [[0]*(m+1) for i in range(n+1)]

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if X[i - 1] == Y[j - 1]:
#                 D[i][j] = D[i][j -1] + 1
#             else:
#                 D[i][j] = max(D[i - 1][j], D[i][j - 1])
#     print("Długość: ", D[i][j])

# cg1 = input("Podaj 1 ciąg: ")
# cg2 = input("Podaj 2 ciąg: ")

# z4(cg1, cg2)

# Z.5
# def z5(X, Y):
#     n = len(X)
#     m = len(Y)
#     D = [[0]*(m + 1) for i in range(n + 1)]

#     for i in range(n + 1):
#         for j in range(m + 1):
#             if X[i - 1] == Y[j - 1]:
#                 D[i][j] = D[i][j - 1] + 1
#             else:
#                 D[i][j] = max(D[i - 1][j], D[i][j - 1])
#     i = n
#     j = m
#     w = []
#     while i > 0 and j > 0:
#         if X[i - 1] == Y[j - 1]:
#             w.append(X[i - 1])
#             i -= 1
#             j -= 1
#         else:
#             if D[i - 1][j] >= D[i][j - 1]:
#                 i -= 1
#             else:
#                 j -= 1
#     print("Wynik: ", w[::-1])

# cg1 = input("Podaj 1 ciąg: ")
# cg2 = input("Podaj 2 ciąg: ")

# z5(cg1, cg2)
