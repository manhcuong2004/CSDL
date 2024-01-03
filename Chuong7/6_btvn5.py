str=input()
L=str.split(' ')
x=input()
for i in range(len(L)):
    if L[i]==x:
        print(i+1)
if x not in L:
    print(0)