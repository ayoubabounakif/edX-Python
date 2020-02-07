def dict_letter_count(string):
    output_dict = {}
    string = string.replace(" ", "") # Remove all white spaces
    string = string.lower() # Convert the string to lower case
    for x in string: # Iterate through the string
         output_dict[x] = string.count(x) # Set each x as a key of the dictionary and its count as the value
    return output_dict

print (dict_letter_count('Hardcoooooooooooooded'))
# {'a': 1, 'c': 1, 'e': 1, 'd': 3, 'h': 1, 'o': 13, 'r': 1}
