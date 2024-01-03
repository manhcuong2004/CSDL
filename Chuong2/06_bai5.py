import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
C=(a+b+c)/2
S= math.sqrt(C*(C-a)*(C-b)*(C-c))
print('Dien tich=', S)