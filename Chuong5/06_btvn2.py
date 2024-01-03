def Input():
    n=int(input('n='))
    L=[]
    for i in range(n):
        j=int(input())
        L.append(j)
    return L
def Search(L):
    max=L[0]
    min=L[0]
    for i in range(len(L)):
        if max < L[i]:
            max=L[i]
        if min > L[i]:
            min=L[i]
    return max, min
def Output(max,min):
    print(max,min)
L=Input()
max,min=Search(L)
Output(max,min) 