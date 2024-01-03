m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
S=int(input('S='))
if S <= 100:
    tiendien=S*m1
elif S <= 150:
    tiendien=100*m1+(S-100)*m2
else:
    tiendien=100*m1+50*m2+(S-150)*m3
print('Phai tra=',tiendien,sep='')