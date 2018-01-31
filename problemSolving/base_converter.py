from pythonds.basic.stack import Stack

def base_converter(dec_num, base):
    digits = "0123456789ABCDEF"

    baseStack = Stack()
    str = ""
    while dec_num > 0:
        baseStack.push( dec_num % base )
        dec_num = dec_num // base

    while not baseStack.isEmpty():
        str = str + digits[baseStack.pop()]
    
    return str

print(base_converter(25,2))
print(base_converter(256,16))
print(base_converter(25,8))
print(base_converter(26,26))