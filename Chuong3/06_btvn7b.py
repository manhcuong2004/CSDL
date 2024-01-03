while True:
    n=int(input())
    if n<0:
        break
    gt=1
    for i in range(1,n+1):
            gt*= i
    print(gt)