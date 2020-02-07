def find_word_horizontal(crosswords, word):
    if not crosswords or not word: # If empty then return None
        return None
    for index, row in enumerate(crosswords):
        temp_str = ''.join(row)
        if temp_str.find(word) >= 0:
            return [index,temp_str.find(word)]

def find_word_vertical(crosswords,word):
    if not crosswords or not word: # If empty then return None
        return None
    for col_index in range(len(crosswords[0])):
        temp_str = ''
        for row_index in range(len(crosswords)):
            temp_str = temp_str + crosswords[row_index][col_index]
        if temp_str.find(word) >= 0:
            return [temp_str.find(word),col_index]

def capitalize_word_in_crossword(crossword,word):
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
    return crossword

###### STACKOVERFLOW ######
"""def capitalize_word_in_crossword(crosswords,word):
     i_v=-1
     j_v=-1
     i_h=-1
     j_h=-1
     index_cap = find_word_horizontal(crosswords,word)
     if index_cap is not None:
        i_h,j_h=index_cap
     else:
        index_cap = find_word_vertical(crosswords,word)
        if index_cap is not None:
           i_v,j_v=index_cap
     for row_index in range(len(crosswords)):
         for col_index in range(len(crosswords[row_index])):
             for w in range(len(word)):
                 if i_h is not -1:
                    if row_index==i_h and col_index==j_h+w:
                       crosswords[row_index][col_index] = (crosswords[row_index][col_index]).upper()
                 if i_v is not -1:
                    if row_index==i_v+w and col_index==j_v:
                       crosswords[row_index][col_index] = (crosswords[row_index][col_index]).upper()
                    else:
                       crosswords[row_index][col_index] = (crosswords[row_index][col_index])
     return (crosswords)"""

print (capitalize_word_in_crossword([['s', 'd', 'o', 'g'], ['x', 'u', 'c', 'm'], ['a', 'x', 'a', 't'], ['t', 'e', 't', 'k']], 'cat'))
