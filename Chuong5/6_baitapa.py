def Nhap():
    L = []
    for i in range(10):
        num = int(input())
        L+=[num]
    x = int(input("x="))
    return L,x

def thaythe(L, x):
    for i in range(len(L)):
        if L[i] == 5:
            L[i] = x
    return L
L, x = Nhap()
kq=thaythe(L, x)
print("Danh sách sau khi thay thế: ", kq)
