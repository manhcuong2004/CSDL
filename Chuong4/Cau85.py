def enter():
    num=int(input('n='))
    return num
def ordinal(num):
    ans=''
    if num==1:
        ans='fisrt'
    elif num==2:
        ans='second'
    elif num==3:
        ans='third'
    elif 4 <= num <= 12 :
        ans=str(num)+'th'
    return ans

def inkq(kq):
    print(kq)

num=enter()
kq=ordinal(num)
inkq(kq)