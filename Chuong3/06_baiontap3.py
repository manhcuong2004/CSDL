kw = int(input("Tieu thu="))

if kw <= 100:
    dongia = 550
elif kw <= 150:
    dongia = 750
elif kw <= 200:
    dongia = 950
else:
    dongia = 1350
VAT = kw * dongia * 0.1
thanhtien = kw * dongia + VAT
print("Phai tra=",thanhtien,sep="")

