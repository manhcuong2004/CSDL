# nhập n, in kq số nguyên tố sau n
def nhap():
    n=int(input())
    return n
def nextPrime(n):
    for i in range(n+1,10000000000):
        d=0
        for j in range(2,i):
            if i%j==0: 
                d=1
                break
        if d==0: return i
n=nhap()
print(nextPrime(n))
        
            
        