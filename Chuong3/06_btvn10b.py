n=int(input('n='))
x=0
for i in range(1,n+1):
    print(i, end=' ')
    x += 1
    if x == 5:
        print('')
        x=0