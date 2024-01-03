toan=int(input())
ly=int(input())
hoa=int(input())
dtb=(toan*2+ly*3+hoa)/6
if dtb<3:
    print('Kem')
elif dtb<5:
    print('Yeu')
elif dtb<6:
    print('Trung binh')
elif dtb<7:
    print('Trung binh kha')
elif dtb<8:
    print('Kha')
elif dtb<9:
    print('Gioi')
else:
    print('Xuat sac')
    
    
    