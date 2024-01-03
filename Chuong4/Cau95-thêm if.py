import random
def bienso():
    chu1=chr(random.randint(65,90))
    chu2=chr(random.randint(65,90))
    chu3=chr(random.randint(65,90))
    so1=chr(random.randint(48,57))
    so2=chr(random.randint(48,57))
    so3=chr(random.randint(48,57))
    so4=chr(random.randint(48,57))
    if random.random() > 0.5 :
        print('Bien so xe ngau nhien la: ',chu1,chu2,chu3,'-',so1,so2,so3,so4,sep='')
    else: print('Bien so xe ngau nhien la: ',chu1,chu2,chu3,'-',so1,so2,so3,sep='')
    
bienso()