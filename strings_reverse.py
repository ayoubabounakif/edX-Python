###### CODE - ALGORITHM 1 ######
def reverse_string(string):
    output = ""
    for char in string:
        output = char + output

    return output


###### CODE - ALGORITHM 2 ######
def reverse_string_v2(string):
    output = ""
    for k in range(len(string)-1, -1, -1):
        #print (k)
        #print (string[k])
        output = output + string[k]

    return output

