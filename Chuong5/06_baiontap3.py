def delete(L, x):
    i = 0
    while i < len(L):
        if L[i] == x:
            del L[i]
        else:
            i += 1
    return L
x = int(input())
n = int(input())
L = []
for i in range(n):
    L.append(int(input()))

L = delete(L, x)
print(L)
