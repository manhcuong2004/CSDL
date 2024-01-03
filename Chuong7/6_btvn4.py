str=input()
L=str.split(',')
M=[]
for i in L:
    if i not in M:
        M.append(i)
M.sort()
str=','.join(M)
print(str)