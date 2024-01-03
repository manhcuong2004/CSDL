def nhap():
    n=int(input("So luong hang da mua: "))
    return n
def tienvanchuyen(n):
    n-=1
    s=10.95+n*2.95
    print("Phi van chuyen cho don hang:",s)
n=nhap()
tienvanchuyen(n)