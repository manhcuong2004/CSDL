str=input()
L=str.split(',')
M=[]
for i in L:
    if int(i,2) % 3 == 0:
        M.append(i)
str=','.join(M)
print(str)       