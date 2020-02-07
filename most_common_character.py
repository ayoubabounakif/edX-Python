###### MY CODE ######
def most_common_char(string):
    string = string.replace(" ", "").lower()
    max_count = 0
    char = None
    for x in string:
        char_count = string.count(x)
        if char_count >= max_count:
            max_count = char_count
            char = x
    return char

print (most_common_char("Ayouuuuub"))

            ### ALGORITHM ###
# Remove all white spaces & Convert to lower case
# Iterate through the given string and for each character
# set a count, among these counts,  return the character whose count is maximum
# On case of tie, return the last character that occurs that has the most count
