from pythonds.basic.stack import Stack

def infixToPostfix(expr):
    opStack = Stack()
    exprPref = {}
    exprPref['^'] = 4
    exprPref['/'] = 3
    exprPref['*'] = 3
    exprPref['+'] = 2
    exprPref['-'] = 2
    exprPref['('] = 1
    postFixExpr = []
    expr = expr.split()
    for token in expr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postFixExpr.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postFixExpr.append(top)
                top = opStack.pop()
        else:
            while not opStack.isEmpty() and exprPref[opStack.peek()] >= exprPref[token]:
                postFixExpr.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postFixExpr.append(opStack.pop())
    
    return " ".join(postFixExpr)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
