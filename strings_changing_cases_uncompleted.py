###### INSTRUCTOR CODE ######
def my_Swap(s):
    output_string=""
    for char in s:
        if (ord(char)<= 90) and (ord(char)>=65) :
            x = chr(ord(char)+32)
            output_string = output_string + x

        elif (ord(char)<= 122) and (ord(char)>=97):
            x = chr(ord(char)-32)
            output_string = output_string + x

        else:
            output_string = output_string + char

    return output_string

print (my_Swap("HeLLO"))

###### MY CODE (Uncompleted) ######
def swap(string):
    output = ""
    for char in string:
        x = char.isupper()
        if x == True:
            y = char.lower()
            output = output + y
        elif x == False:
            y = char.upper()
            output = output + y
    return output

print (swap("HeLLO"))
