n=input()
L=n.split(', ')
D=[]
for i in range(len(L)):
    D.append(int(L[i]))
D.sort(reverse=1)
for i in D:
    print(i,end=' ')