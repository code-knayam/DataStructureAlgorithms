#ˀ The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

def rgb(r, g, b):
    #your code here :)
    val = [r, g, b]
    new_string = ""
    for i in val:
        if i < 0:
            i = 0
        elif i > 256 :
            i = 255
        converted = str(toHex(i))            
        if len(converted) == 1:
            new_string = new_string + ("0" + converted)
        else:            
            new_string= new_string + (converted)
            
    return new_string    
    
    
def toHex(n):
    convert_string = "0123456789ABCDEF"
    if n < 16:
        return convert_string[n]
    else:
        return toHex( n // 16) + convert_string[n%16]


#  Best Practice ->

# def limit(num):
#     if num < 0:
#         return 0
#     if num > 255:
#         return 255
#     return num


# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))