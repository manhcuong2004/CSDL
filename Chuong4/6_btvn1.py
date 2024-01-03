def nhap():
    n = int(input("n="))
    return n
def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n-1)
def inkq(n, j):
    print(n,"!=", j,sep="")
n = nhap()
j = giaithua(n)
inkq(n, j)

