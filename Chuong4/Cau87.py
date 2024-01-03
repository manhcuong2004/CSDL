a=int(input('a='))
def trungtam(s,cd):
    if cd<len(s):
        return s
    b=(a-len(s))//2
    c=' '*b+s
    return c
def inkq():
    n=input('Nhap chuoi ki tu:')
    print(trungtam(n,a))
inkq()
    