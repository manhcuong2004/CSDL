import random
def play_game():
    while True:
        n = int(input("Người: "))    
        if n == 0:
            print("Kết thúc chương trình")
            break
        else:
            m = random.randint(1, 3)
            print("Máy:", m)
            if n == 1 and m == 3:
                return "Người thắng"
            elif n == 2 and m == 1:
                return "Người thắng"
            elif n == 3 and m == 2:
                return "Người thắng"
            elif n == m:
                return "Hòa"
            else:
                return "Máy Thắng"
result = play_game()
print("Kết quả:", result)
