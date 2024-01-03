while True:
    n=int(input())
    if n<0:
        break
    gt = 1
    i=1
    while i <= n:
        gt*=i
        i+=1
    print(gt)
