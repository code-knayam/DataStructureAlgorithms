from __future__ import print_function
from pythonds.basic.stack import Stack

def balance_equation(expr):
    balanced = True
    bracket_stack = Stack()
    index = 0
    while index < len(expr) and balanced:
        if expr[index] == '(':
            bracket_stack.push('(')
        else:
            if bracket_stack.isEmpty():
                balanced = False
            else:
                bracket_stack.pop()
        index = index + 1

    if balanced and bracket_stack.isEmpty():
        return True
    else:
        return False

print(balance_equation('((()))'))
print(balance_equation('(())'))
