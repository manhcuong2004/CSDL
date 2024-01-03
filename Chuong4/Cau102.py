def nhap():
    n=int(input("So luong: "))
    x=input("Dung cu: ")
    return n,x

def quydoi(n,x):
    m = n
    if x == "coc" : 
        c = n
        print(c,"coc")
    elif x == "muong canh" : 
        c = n//16
        mc = n%16
        if c == 0 : print(n,"muong canh")
        elif c != 0 and mc == 0 : print(c,"coc")
        else : print(n//16," coc",n%16," muong canh")
    elif x == "muong ca phe" :
        m = n%3
        mc = (n//3)%16
        c = n//48
        #print(c," ",mc," ",m)
        if c != 0 and mc == 0 and m == 0: print(c,"coc")
        elif c != 0 and mc != 0 and m == 0: print(c,"coc,",mc,"muong canh")
        elif c == 0 and mc != 0 and m == 0: print(mc,"muong canh")
        elif c == 0 and mc != 0 and m != 0: print(mc,"muong canh,", m,"muong ca phe")
        else : print(c,"coc,",mc,"muong canh,", m,"muong ca phe")

n,x = nhap()   
quydoi(n,x)    
