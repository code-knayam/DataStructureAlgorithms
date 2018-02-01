# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    #your code here
    new_array = [] 
    
    new_index = 0
    while len(array) > 0:
        item = array.pop(0)
        if item == 0 and  not type(item) == bool :
            new_array.append(item)
        else:
            new_array.insert(new_index, item)
            new_index = new_index + 1
    return new_array