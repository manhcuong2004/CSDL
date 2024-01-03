def Nhap():
    x=int(input())
    y=int(input())
    z=int(input())
    return x,y,z
def trungvi(x,y,z):
    mid=x
    if x<y<z or x>y>z:
        mid=y
    if x<z<y or x>z>y:
        mid=z
    return mid
x,y,z=Nhap()
print('Gia tri trung vi:',trungvi(x,y,z))