def Nhap():
    n = int(input("n="))
    return n
def uocso(n):
    uoc = []
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)
    return uoc
n = Nhap()
print(uocso(n))
