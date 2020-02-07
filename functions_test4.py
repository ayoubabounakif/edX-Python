# Returns the minimum of a list of numbers

def lowest_number(list):
    min = list [0]
    for i in list:
        if i < min:
            min = i
    return min


