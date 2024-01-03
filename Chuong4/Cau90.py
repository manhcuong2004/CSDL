def NhapChuoi():
    n=str(input('Nhap chuoi: '))
    b=0
    for j in n:
        b=b+1
    while b==0:
        n=str(input('Nhap lai chuoi hop le: '))
        for j in n:
            b=b+1
    return n
def isInterger(n):
    a=0
    b=0
    c=0
    for j in n:
        b=b+1
    for i in n:
        for h in n:
            while c==0:
                if h=='+' or h=='-':
                    a=a+1
                    c=c+1
                else:
                    break
            break
        if i==' ':
            a=a+1
        if '0'<=i<='9':
            a=a+1
    if a==b:
        print('Chuoi nay dai dien cho so nguyen')
    else:
        print('Chuoi nay khong dai dien cho so nguyen')
n=NhapChuoi()
isInterger(n)