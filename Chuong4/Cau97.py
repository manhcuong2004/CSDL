import random
def matkhaungaunhien():
    dodai=random.randint(7,10)
    matkhau=''
    for i in range(dodai):
        matkhau=matkhau+chr(random.randint(33,126))
    return matkhau
def kiemtramatkhau(mk):
    kiemtrachuhoa=False
    kiemtrachuthuong=False
    kiemtraso=False
    for i in mk:
        if 'A'<=i<='z':
            kiemtrachuhoa=True
        if 'a'<=i<='z':
            kiemtrachuthuong=True
        if '0'<=i<='9':
            kiemtraso=True
    return len(mk)>=8 and kiemtraso and kiemtrachuhoa and kiemtrachuthuong
mk=""
d=0
while kiemtramatkhau(mk)!=True:
    mk=matkhaungaunhien()
    if kiemtramatkhau(mk)==False: d+=1
    else: 
        print("Mat khau la: ",mk)
        print("So lan tao ngau nhien: ",d+1)
        