def preserve_reverse(string):
    string = string.split()
    output = ""
    for x in range(0, len(string)):
        string[x] = string[x][::-1]
    for x in range(0, len(string)):
        output += string[x] + " "
    output = output.strip()
    return output
