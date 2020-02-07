###### MY CODE ######
def find_longest_word(string):
    string = string.split()
    longest_word = ""
    for char in string:
        if len(char) > len(longest_word):
            longest_word = char
        elif len(char) == len(longest_word):
            longest_word = (longest_word + " " + char).split()[-1:]
            longest_word = ''.join(longest_word)
    return longest_word

################### INSTRUCTOR CODE ###################
def longest_word_sample(input_string):
    splitted_string = input_string.split()
    maximum_length = len(splitted_string[0])
    longest_word = splitted_string[0]
    for string in splitted_string:
        string_length = len(string)
        if string_length >= maximum_length:
            longest_word = string
    return longest_word
