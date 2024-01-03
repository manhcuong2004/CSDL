import random

def game(n):
    n=int(input('Người chọn:'))
    m= random.randint(1, 3)
    print(f"Máy chọn:",n)
    if n == m:
        return "Hòa"
    elif (n == 1 and m == 3) or (n == 2 and m == 1) or (n == 3 and m == 2):
        return "Người Thắng"
    else:
        return "Máy Thắng"

n = int(input('Người chọn'))
print(game(n))




