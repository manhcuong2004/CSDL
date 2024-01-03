def LaSoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def SoHopLe(n):
    return n <= 1
def NhapVaDem():
    j = 0
    while True:
        n = int(input())
        if SoHopLe(n):
            break
        if LaSoNguyenTo(n):
            j += 1
    return j
def InKQ(kq):
    print("Co",j,"so nguyen to")
print("Nhap day so:")
j = NhapVaDem()
InKQ(j)
