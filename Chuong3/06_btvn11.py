am = 0
duong = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n > 0:
        duong += 1
    else:
        am += 1
print(duong,'so duong')
print(am,'so am')
