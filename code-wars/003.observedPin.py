def get_pins(observed):
#   '''TODO: This is your job, detective!'''
    comb_dict = {
        "0" : ['0', '8'],
        "1" : ['1', '2', '4'],
        "2" : ['2', '4', '6'],
        "3" : ['2', '3', '6'],
        "4" : ['1', '5', '7', '4'],
        "5" : ['2', '4', '5', '6', '8'],
        "6" : ['3', '5', '6', '9'],
        "7" : ['4', '7', '8'],
        "8" : ['5', '7', '8', '9', '0'],
        "9" : ['6', '8', '9']
    }
    combinations = []
    for i in str(observed):
        if len(combinations) == 0:
            combinations = comb_dict.get(i)
        else:
            new_combinations = []
            for val in comb_dict.get(i):
                for i in combinations:
                    new_combinations.append( i + val )
            combinations = new_combinations

    return combinations

print(get_pins2(123))
