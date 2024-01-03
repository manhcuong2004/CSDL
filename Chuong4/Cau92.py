def Nhap(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
def inkq():
    gt=int(input('Nhap mot so nguyen:'))
    if Nhap(gt):
        print(gt,'la so nguyen to.')
    else:
        print(gt,'khong la so nguyen to.')
inkq()