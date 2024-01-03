import random
def taomatkhaungaunhien():
    dodai = random.randint(7, 10)
    matkhau = ''
    for i in range(dodai):
        matkhau += chr(random.randint(33, 126))
    return matkhau
print(taomatkhaungaunhien())
