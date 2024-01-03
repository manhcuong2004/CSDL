mk = input()
so=0
chuth=0
chuh=0
kt=0
if len(mk)>0 and len(mk)<17:
    for i in mk:
        if i.isdigit():
            so+=1
        if i.islower():
            chuth+=1
        if i.isupper():
            chuh+=1
        if i in '$#@':
            kt+=1
if so>0 and chuth>0 and chuh>0 and kt>0:
    print('True')
else:
    print('False')
        