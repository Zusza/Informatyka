# path = 'C:\Users\Student\Desktop\dane_systemy1.txt'
# with open(path) as f:
#     T = f.read().split()

# # Zad.1
# T = [f]
# najwytemp = None
# najmntemp = None
# for i in range(len(T)):
#     if T[i] < najwytemp:
#         najwytemp = T[i]
#     if T[i] > najmntemp:
#         najmntemp = T[i]
# print("Najniższa temperatura: ", najmntemp, "Najwyższa temperatura: ", najwytemp)

# # Zad.2
# T = [f]
# for n in range(len(T)):
#     n+=1
# stanzegara = 12
# liczba = 0
# for i in range(len(T)):
#     stanzegara = stanzegara + pow(stanzegara, n)
#     poprzstanzegara = (stanzegara - 1) 
#     if stanzegara != poprzstanzegara: #?
#         liczba += 1  
# print("Liczba niepoprawnych stanów zegara: ", liczba)

# # Zad.3
# pomiar = [f]
# rekord = 0
# lrekordow = 0
# godz = 0
# for i in range(len(pomiar)):
#     if pomiar[i] > pomiar[i-1]:
#         rekord = pomiar[i]
#         lrekordow += 1
#         godz = pomiar
#         print("Liczba rekordów: ", lrekordow, "Godzina: ", godz)


# # Zad.4
# T = [f]
# for n in range(len(T)):
#     a = n%2
#     i = T[a]
#     j = T[a+1]
#     r= (i - j)^2
#     skok = r / i - j
# print("Największy skok: ", skok)