a = input()
L = list(a)
T = []
H = []
for i in range(len(a)):
    if a[i].isnumeric() and a[i-1] != '-':
        T.append(a[i])
    elif a[i] == '-':
        H.append(a[i+1])
tong = 0
for i in range(len(T)):
    tong += int(T[i])
for i in range(len(H)):
    tong -= int(H[i])
print(tong)