from pythonds.basic.stack import Stack



def evalPostFix(expr):
    expr = expr.split()

    opStack = Stack()

    for token in expr:
        if token in "0123456789":
            opStack.push(int(token))
        else :
            opB = opStack.pop()
            opA = opStack.pop()
            opStack.push( operate(token, opA, opB) )
    return opStack.pop()

def operate(symbol, opA, opB):
    if symbol == "*":
        return opA * opB
    elif symbol == "/":
        return opA / opB
    elif symbol == "+":
        return opA + opB
    else:
        return opA - opB

print(evalPostFix('7 8 + 3 2 + /'))