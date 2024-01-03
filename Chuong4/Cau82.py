def Nhap():
    a=int(input('Quang duong khach da di :'))
    t=giave(a)
    print('Gia taxi la: $',t,sep='')
    
def giave(a):
    return 4.00+(a*1000//140)*0.25 #//:chia lấy nguyên
Nhap()