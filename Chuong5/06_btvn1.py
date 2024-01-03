def Input():
    L=[]
    n = int(input('n='))
    for i in range(n):
        j=int(input())
        L.append(j)
    x=int(input('x='))
    return L,x
def FirstAndLast(L):
    nL=[L[0],L[-1]]
    print(nL)
    return L
def Search(L,x):
    if x in L:
        print('True')
    else:
        print('False')
L,x=Input()
FirstAndLast(L)
Search(L,x)
    
        
    
    