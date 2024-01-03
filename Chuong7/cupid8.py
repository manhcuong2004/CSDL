s = input()
A=list(s)
L=[]
for i in A:
    if A.count(i)>1:
       if i not in L:
           L.append(i)
if len(L)==0:
    print('None')
for i in L:
    print(i)

