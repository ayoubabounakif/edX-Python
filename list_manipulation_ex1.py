# A function that accepts a list (which has a length of 4 or more)
# and a string and returns the list such that the second through
# the fourth element (index 1 through 3 both inclusive) in the input list
# are replaced by the input string

def replace_list(input_list, input_string):
    for i in range(1,4):
        input_list[i] = input_string
    return input_list
