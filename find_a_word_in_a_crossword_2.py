#### CODE ####
def find_word_horizontal(crossword, string):
    output_list = []
    if not crossword or not string: # If empty return line 4
        return None
    for index, row in enumerate(crossword):
        temp_string = ''.join(row)
        #print (temp_string)
        #print (crosswords)
        if temp_string.find(string) >= 0:
            output_list = [index, temp_string.find(string)]
    return output_list

def find_word_vertical(crossword, string):
    output_list = []
    if not crossword or not string: # If empty return line 4
        return None
    for col_index in range(len(crossword[0])):
        #print (col_index)
        temp_string = ''
        for row_index in range(len(crossword)):
            temp_string += crossword[row_index][col_index]
            #print (temp_string)
        if temp_string.find(string) >= 0:
            output_list = [temp_string.find(string), col_index]
        return output_list

def capitalize_word_crossword(crossword, string):
    if not crossword or not string:
        return None
    found_pos = find_word_horizontal(crossword, string)
    if found_pos:
        for k in range(len(string)):
            crossword[found_pos[0]][found_pos[1]+k] = crossword[found_pos[0]][found_pos[1]+k].upper()
        return crossword
    found_pos = find_word_vertical(crossword, string)
    if found_pos:
        for k in range(len(string)):
            crossword[found_pos[0]+k][found_pos[1]] = crossword[found_pos[0]+k][found_pos[1]].upper()
        return crossword

"""def capitalize_word_in_crossword(crossword,word):
    if not crossword or not word:
        return None
    found_position= find_word_horizontal(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]][found_position[1]+k]=crossword[found_position[0]][found_position[1]+k].upper()
        return crossword
    found_position= find_word_vertical(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]+k][found_position[1]]=crossword[found_position[0]+k][found_position[1]].upper()
    return crossword"""


crossword = [['s', 'd', 'o', 'g'], ['c', 'u', 'c', 'm'], ['a', 'c', 'a', 't'], ['t', 'e', 't', 'k'],
['c', 'b', 'a', 'g'], ['b', 'h', 'z', 'k'], ['a', 'b', 'c', 'd'], ['b', 'l', 'o', 'o'],
['v', 'z', 't', 'k'], ['s', 'x', 'e', 'u']]
string = input('Please enter a valid string: ')
print (find_word_horizontal(crossword, string))
print (find_word_vertical(crossword, string))
print (capitalize_word_crossword(crossword, string))

#[['s', 'd', 'o', 'g'], ['x', 'u', 'c', 'm'], ['a', 'x', 'a', 't'], ['t', 'e', 't', 'k']]
