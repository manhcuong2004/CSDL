l=[]
a=input()
while a!='':
    if a not in l:
        l.append(a)
    a=input()
for a in l:
    print(a)
    