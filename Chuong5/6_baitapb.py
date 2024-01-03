def remove_all(L, x):
    while x in L:
        L.remove(x)
def main():
    L = []
    for i in range(10):
        num = int(input())
        L.append(num)

    x = int(input("Enter x: "))

    remove_all(L, x)
    print(L)
main()
