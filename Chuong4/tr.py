a=int(input())
b=int(input())
c=int(input())
mid = a
if a<b<c or a>b>c:
    mid=b
elif a<c<b or a>c>b:
    mid=c
print(mid)

