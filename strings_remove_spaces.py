###### MY CODE ######
def rm_spaces(string):
    output = ""
    for x in range(0, len(string)):
        if string[x] != " ":
            output += string[x]

    return output

print (rm_spaces("    Ayoub    "))

