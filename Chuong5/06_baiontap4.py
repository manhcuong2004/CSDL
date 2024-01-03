n = int(input())
L = []
for i in range(n):
    L.append(int(input()))
def count(L):
    count = 0
    for i in L:
        count += 1
    return count
print(count(L))


