L=[]
M=[]
n=int(input('n='))
for i in range(n):
    x=int(input())
    if x not in L:
        L.append(x)
M=L.copy()
for i in M:    
    print(i, end=' ')