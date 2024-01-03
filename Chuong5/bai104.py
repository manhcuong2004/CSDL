L=[]
while True:
    n=int(input())
    L.append(n)
    L.sort()
    if n==0:
        break
i=L.pop(0)
print('Cac so nguyen da nhap:')
for n in L:
    print(n)