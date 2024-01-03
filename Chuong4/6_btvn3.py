import math
def nhap():
    while True:
        a = int(input("a="))
        b = int(input("b="))
        c = int(input("c="))
        if a != 0 and b != 0 and c != 0:
            return a, b, c
def giaipt(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co nghiem kep")
        print("x1=x2=",x,sep='')
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co hai nghiem")
        inkq(x1, x2)
def inkq(x1, x2):
    print("x1=",x1,sep="")
    print("x2=",x2,sep="")
print('Nhap 3 so nguyen:')
a, b, c = nhap()
giaipt(a, b, c)