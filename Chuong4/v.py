n=int(input())
if n<100:
    st=n*3000
if n>100:
    st=30000+(n-100)*4500
print(st)