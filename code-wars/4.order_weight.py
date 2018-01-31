def sum_dg(st):
    sum = 0
    for c in st:
        sum = sum + int(c)
    return sum        

def order_weight(strng):

    strng = strng.split(" ")
    leng = len(strng)
    for i in range(leng):        
        for j in range(leng-1):
            if sum_dg(strng[j]) > sum_dg(strng[j+1]):
                temp = strng[j]
                strng[j] = strng[j+1]
                strng[j+1] = temp
            if sum_dg(strng[j]) == sum_dg(strng[j+1]):
                if strng[j+1] < strng[j]:
                    temp = strng[j]
                    strng[j] = strng[j+1]
                    strng[j+1] = temp

    return " ".join(strng)      

# def order_weight(_str):
#     return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
        

print(order_weight("103 123 4444 99 2000"))

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123  "))