height = int(input("Nhập chiều cao của kim tự tháp: "))

for i in range(1, height+1):
    print(" " * (height-i), end="")
    print("*" * (2*i-1), end="")
    print(" " * (height-i))
