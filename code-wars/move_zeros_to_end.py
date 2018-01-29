def move_zeros(array):
    #your code here
    new_array = [] 
    
    new_index = 0
    while len(array) > 0:
        item = array.pop(0)
        if item == 0  and type(item) == int:
            new_array.append(item)
        else:
            new_array.insert(new_index, item)
            new_index = new_index + 1
    return new_array

    

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))

print( False == 0 )