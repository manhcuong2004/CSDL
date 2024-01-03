def nhap():
    a=int(input("canh thu nhat: "))
    b=int(input("canh thu hai: "))
    c=int(input("canh thu ba: "))
    return a,b,c
def ktrTamgiac(a,b,c):
    if (a+b>c and a+c>b and b+c>a): 
        return True
    return False
a,b,c=nhap()
print(ktrTamgiac(a,b,c))