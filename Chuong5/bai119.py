import random
def taobai():
    deck = []
    chat = ['h', 'd', 'c', 's']
    so = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for c in chat:
        for s in so:
            deck.append(s + c)
    return deck
def deal(taybai, slbai, deck):
    random.shuffle(deck) #Hàm shuffle được sử dụng để xáo trộn một chuỗi
    hands = []
    for i in range(taybai):
        hand = []
        for j in range(slbai):
            hand.append(deck.pop())
        hands.append(hand)
    return hands, deck
deck = taobai()
hands, deck = deal(4, 5, deck)
count = 1
for hand in hands:
    print(hand)
    count += 1
print(deck)


