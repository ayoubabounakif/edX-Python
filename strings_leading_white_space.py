###### MY CODE ######
def strip(string):
    x = ""
    x = string.strip()
    return x

###### INSTRUCTOR CODE #######
def remove_leading_whitespace(string):
    my_index = None
    for x in range(0, len(string)):
        if string[x] != " ":
            my_index = x
            break
    # Slice the string from that index to the end
    new_string = string[my_index::]
    return new_string
