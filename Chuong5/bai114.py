import random
veso = []
while len(veso)<6:
    num = random.randint(1, 50)
    if num not in veso:
        veso.append(num)
veso.sort()
print(veso)
