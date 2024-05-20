# def f(x):
#     return pow(x,4)/500 - pow(x,2)/200 - 3/250

# def g(x):
#     return -pow(x,3)/30+x/20+1/6

# def prostokatf(af,bf,nf):
#     dxf = (bf - af) / nf
#     sumf = 0
#     for i in range(nf):
#         sumf += f(af + i + dxf * dxf/2) * dxf
#     return sumf
# print(prostokatf(2,10,1000))

# def prostokatg(ag,bg,ng):
#     dxg = (bg - ag) / ng
#     sumg = 0
#     for ig in range(ng):
#         sumg += g(ag + ig + dxg * dxg/2) * dxg
#     return sumg
# print(prostokatg(2,10,1000))

# Zad.1
# Pole = a*b
# pole_prostokata = 2*(19*61/125+(-32*2/3))
# powierzchnia_materialu = pole_prostokata - (prostokatf+prostokatg)

# Zad.2
# x = 1
# obwodf = 0
# for i in range(1,1000):
#     lamanaf = (x+1,f(x+1))
#     obwodf += lamanaf + prostokatf(2,10,1000)
# print(obwodf)

# obwodg = 0
# for i in range(1,1000):
#     lamanag = (x+1,g(x+1))
#     obwodg += lamanag + prostokatg(2,10,1000)
# print(obwodg)

# Zad.3
