def search(L, x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
x = int(input())
n = int(input())

L = []
for i in range(n):
    L.append(int(input()))
kq = search(L, x)

if kq is not None:
    print(kq)
else:
    print("None")
