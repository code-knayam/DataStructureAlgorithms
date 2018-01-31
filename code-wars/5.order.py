### 
# Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.
# For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
###

import re

def order(string):
    string = string.split(" ")
    newString = [""] * len(string)
    for index in range(len(string)):
        if re.search("\d", string[index]) != None:
            newIndex = int(string[index][re.search("\d", string[index]).start()])
            newString[newIndex - 1] = string[index]        
    return " ".join(newString)

print(order("is2 Thi1s T4est a"))
