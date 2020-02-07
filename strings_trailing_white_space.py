###### MY CODE ######
def trailing_whitespace(string):
    my_index = None
    y = None
    for x in range(0, len(string)):
        if string[x] != " ":
            my_index = x
            continue
    # Slice the string from that index to the end
    new_string = string[:my_index+1:]
    return new_string

print (trailing_whitespace("  Hello       "))

###### INSTRUCTOR CODE ######
def remove_trailing_whitespace(string):
    my_index = None
    i = len(string)
    while i > 0:
        if string[i-1] != " ":
            my_index = i
            break
        i = i - 1
    # Slice the string from 0 to that index
    new_string = string[:my_index]X85
    return new_string
