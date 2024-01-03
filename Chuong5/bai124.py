def ttsanght(tokens):
    operators = []
    postfix = []
    uutien = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token in uutien:
            # Nếu token là một toán tử, xử lý các toán tử hiện tại trong danh sách operators
            while operators and operators[-1] != '(' and uutien[token] <= uutien[operators[-1]]:
                postfix.append(operators.pop())
            operators.append(token)
        elif token == '(':
            # Nếu token là một dấu ngoặc mở, thêm nó vào danh sách operators
            operators.append(token)
        elif token == ')':
            # Nếu token là một dấu ngoặc đóng, xử lý các toán tử trong danh sách operators cho đến khi gặp dấu ngoặc mở
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()

    while operators:
        postfix.append(operators.pop())
    return postfix

def gthauto(hauto):
    gtL = []
    for token in hauto:
        if token.isdigit():
            gtL.append(int(token))
        else:
            right = gtL.pop()
            left = gtL.pop()
            if token == '+':
                gtL.append(left + right)
            elif token == '-':
                gtL.append(left - right)
            elif token == '*':
                gtL.append(left * right)
            elif token == '/':
                gtL.append(left / right)
            elif token == '^':
                gtL.append(left ** right)
    return gtL[0]

def main():
    trungto = input("Nhap bieu thuc trung to: ")
    hauto = ttsanght(trungto)
    print("Bieu thuc hau to:", ''.join(hauto))
    gt = gthauto(hauto)
    print("Gia tri cua bieu thuc:", gt)

main()
