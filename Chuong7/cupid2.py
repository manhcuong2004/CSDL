a = input()
b = a.split()
A = []
B = []
for i in range(len(b)):
    if i == 1 or i == 3 or i == 4:
        A = A + [b[i]]
for i in b:
    if i not in A:
        B = B + [i]
print(B)