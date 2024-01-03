#nhap n>=4
while True:
    n = int(input('n='))
    if n < 4 : 
        print("Khong hop le!!!\nMoi nhap lai")
    else : 
        break 
#nhap vao day n so
a = []
for i in range(n):
    a += [int(input())]
print(a)
#tim max min a
maxx = max(a)
minn = min(a)
#loai bo cac so max min
while minn in a:
    a.remove(minn)
while maxx in a:
    a.remove(maxx)
print(a)
