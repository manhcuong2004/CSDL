while True:
    a=float(input('a='))
    b=float(input('b='))
    tt = input('Nhap toan tu')
    if tt == '+':
        print(a,'+',b,'=',a+b,sep='')
    elif tt == '-':
        print(a,'+',b,'=',a-b,sep='')
    elif tt == '*':
        print(a,'*',b,'=',a*b,sep='')
    elif tt == '/':
            if b == 0:
                print('Khong the chi cho 0')
            else:
                print(a,'/',b,'=',a / b,sep=0)
    else:
        print('Toan tu khong hop le')
    choice = input('Nhap T hoac t de ket thuc: ')
    if choice == 'T' or choice == 't':
        break
    print('ket thuc chuong trinh')




