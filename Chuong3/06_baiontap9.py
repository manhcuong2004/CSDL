n = int(input('n='))
f = True
for i in range(2,n):
    if n % i == 0:
        f = False
        break
if f:
    print(n,'La SNT')
else:
    print(n,'Khong la SNT')
    

