n = input()
L=['#','*','!','$','^']
M=[]
for i in n:
    if i not in L:
        M+=[i]
kq=''.join(M)
print(kq)