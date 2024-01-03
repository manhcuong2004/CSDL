n=input()
L=n.split(' ')
ln=0
for i in range(1,len(L)):
    if ln < int(L[i])*int(L[i-1]):
        ln = int(L[i])*int(L[i-1])
print(ln)
    