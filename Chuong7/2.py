n=int(input())
t=0
for i in range(1,n):
    if n%i==0 and n != i:
        t+=i
if n == t:
    print('True')
else:
    print('False')  