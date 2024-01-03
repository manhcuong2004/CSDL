n = int(input())
nstr = str(n)
mh = ''
for i in nstr:
    if i == '0':
        mh += 'A'
    elif i == '1':
        mh += 'B'
    elif i == '2':
        mh += 'C'
    elif i == '3':
        mh += 'D'
    elif i == '4':
        mh += 'E'
    elif i == '5':
        mh += 'F'
    elif i == '6':
        mh += 'G'
    elif i == '7':
        mh += 'H'
    elif i == '8':
        mh += 'K'
    elif i == '9':
        mh += 'L'
print(mh)


