#chuyển đổi thập  phân với thập lục và ngược lại
def hex2int(x):
    if x.upper() == "A" : return 10
    if x.upper() == "B" : return 11
    if x.upper() == "C" : return 12
    if x.upper() == "D" : return 13
    if x.upper() == "E" : return 14
    if x.upper() == "F" : return 15
    
def int2hex(x):
    s='0123456789ABCDEF'
    if int(x)<16: return s[int(x)]
    
def nhap():
    n=input() 
    if (n.isdigit()): 
        if int2hex(n) == None: return 0
        else: 
            print(int2hex(n))
            nhap()
    else: 
        if hex2int(n) == None: return 0
        else:
            print(hex2int(n))
            nhap()
            
nhap()


'''def hex2int(x):
    if x == "a" or x == "A" : return 10
    if x == "b" or x == "B" : return 11
    if x == "c" or x == "C" : return 12
    if x == "d" or x == "D" : return 13
    if x == "e" or x == "E" : return 14
    if x == "f" or x == "F" : return 15'''
'''def int2hex(x):
    if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9': 
        return x
    if x == '10': return "A"
    if x == '11': return "B"
    if x == '12': return "C"
    if x == '13': return "D"
    if x == '14': return "E"
    if x == '15': return "F" '''