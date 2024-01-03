str = input()
hoa = 0
thuong = 0
so = 0
Khac = 0
for ch in str:
    if ch.isupper():
        hoa+=1
    elif ch.islower():
        thuong+=1
    elif ch.isnumeric():
        so+=1
    else:
        Khac+=1
print(hoa, thuong, so, Khac)