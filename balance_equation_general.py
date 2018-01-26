from pythonds.basic.stack import Stack

def matches(open, close):
    openrs = '([{'
    closers = ')]}'
    return openrs.index(open) == closers.index(close)


def balance_equation_general(str):
    st = Stack()
    index = 0
    balanced = True

    while index < len(str) and balanced:
        symbol = str[index]
        if symbol  in '([{':
            st.push(symbol)
        else:
            if st.isEmpty():
                balanced = False
            else :
                top = st.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    
    if st.isEmpty() and balanced:
        return True
    else:
        return False

print(balance_equation_general('{{([][])}()}'))
print(balance_equation_general('[{()]'))
