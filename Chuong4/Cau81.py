import math
def nhap():
    a = float(input('Do dai canh thu nhat: '))
    b = float(input('Do dai canh thu hai: '))
    return a,b
def canhhuyen():
    c = math.sqrt(a**2 + b**2)
    return c
a,b=nhap()
c=canhhuyen()
print('Do dai canh huyen', c)