def nhap():
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    kq=a
    if kq < b:
        kq=b
    elif kq < c:
        kq=c
    return kq
def inkq(kq):
    print('So lon nha la:',kq)
print('Nhap 3 so nguyen')
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)
