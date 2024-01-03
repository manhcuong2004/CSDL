a=input()
b=input()
a=a.split()
b=b.split()
A=[]
for i in range(len(a)):
    if a[i] in b:
        A+=[a[i]]
print(A)
        
        