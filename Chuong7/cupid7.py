n=int(input())
A=[]
B=[]

if n<=0:
    print('None')
else:
    for i in range(n):
        x=input()
        A.append(x)
        B.append(len(x))
    a=max(B)
    b=B.index(a)
print(A[b])
print(a)
    