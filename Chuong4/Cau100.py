from calendar import monthrange
def thangvanam():
    a=int(input('Thang:'))
    b=int(input('Nam:'))
    c=monthrange(b,a) [1]
    return c
def ketqua(c):
    print(c)
c=thangvanam()
ketqua(c)