def Viethoa_str(s):
    s = s.capitalize()
    s = s.replace(" i ", " I ")
    for i in range(0,len(s)):
        #print(s[i],end=" ")
        if s[i]=='.' or s[i]=='!' or s[i]=='?' :
            j=i+1
            for j in range(i+1,len(s)):
                if s[j]!=' ': 
                    s=s[:j]+s[j:].capitalize()
                    break
    return s
a= input("Nhap 1 chuoi: ")
VIETHOA_str = Viethoa_str(a)
print(VIETHOA_str)