import random
def kbb():
    while True:
        n = int(input("Người: "))
        if n == 0:
            print("Chương trình kết thúc!")
            return
        elif n<1 or n>3:
            print("Chỉ nhập số nguyên từ 1 đến 3 hoặc 0 để kết thúc")
            continue
        m = random.randint(1, 3)
        print("Máy:",m)
        if n == m:
            print("Hòa")
        elif (n == 1 and m == 2) or (n == 2 and m == 3) or (n == 3 and m == 1):
            print("Người thắng")
        else:
            print("Máy thắng")

kbb()
