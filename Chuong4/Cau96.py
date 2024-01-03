def long(password):
    if len(password) >= 8:
        return True
    else:
        return False
def chuhoa(password):
    for char in password:
        if char.isupper():
            return True
    return False
def chuthuong(password):
    for char in password:
        if char.islower():
            return True
    return False
def coso(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def goodpass(password):
    if long(password) and chuhoa(password) and chuthuong(password) and coso(password):
        return True
    else:
        return False
def main():
    password = input('Nhap password cua ban: ')
    if goodpass(password):
        print('Password cua ban tot!!')
    else:
        print('Password cua ban khong tot')
main()
