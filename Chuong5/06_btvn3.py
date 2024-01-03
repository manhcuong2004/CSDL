n=int(input('n='))
L=[]
for i in range(n):
    j=int(input())
    L.append(j)
snd=0
for i in L:
    if i>0:
        snd+=1
t=0
n=0
for i in L:
    if i%2 == 0:
        n+=1
        t+=i
if n == 0:
    tbc=0
print('SND=',snd,sep='')
print('TBC=',tbc,sep='')