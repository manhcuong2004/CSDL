import math
def Nhap():
    a=int(input('Nhap tu so:'))
    b=int(input('Nhap mau so:'))
    return a,b
def rutgonphanso(a,b):
    d=math.gcd(a,b)
    e=a//d
    f=b//d
    return e,f
a,b=Nhap()
e,f=rutgonphanso(a,b)
print('Phansorutgon:',e,f)
    