n=int(input('n='))
A=[]
for i in range(n):
    j=int(input())
    A.append(j)
Tong=0
for i in range(len(A)):
    if i%2 != 0:
        Tong+=A[i]
print('Tong=',Tong,sep='')
        
    