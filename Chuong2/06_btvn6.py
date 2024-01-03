ten=input('Ho ten:')
snc=float(input('So ngay cong:'))
dgnc=float(input('Don gia ngay cong:'))
hspc=float(input('He so phu cap:'))
tu=float(input('Tam ung:'))
L=dgnc*snc*hspc
tl=L-tu
print('Nhan vien ', ten,', Co tien Luong=',L,', Tam ung=',tu,' va Thuc linh=',tl, sep=(''))