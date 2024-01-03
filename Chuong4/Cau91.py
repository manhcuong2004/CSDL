def nhap():
    tt = input("Nhap vao mot toan tu (+, -, *, /, ^): ")
    return tt
def uutien(toantu):
    if toantu == '+' or toantu == '-':
        return 1
    elif toantu == '*' or toantu == '/':
        return 2
    elif toantu == '^':
        return 3
    else:
        return -1
tt=nhap()
kq = uutien(tt)
print("Do uu tien la:",kq)


