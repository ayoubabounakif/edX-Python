
###### INSTRUCTOR CODE ######
def find_word_vertical(crosswords,word):
    if not crosswords or not word:
        return None
    for col_index in range(len(crosswords[0])):
        str = ''
        for row_index in range(len(crosswords)):
            str = str + crosswords[row_index][col_index]
        if str.find(word) >= 0:
            return [str.find(word), col_index]

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_vertical(crosswords,word))

###### STACKOVERFLOW ######
def find_word_vertical(crosswords,word):
    columns = []
    finished = []
    for col in range(len(crosswords[0])):
        columns.append([crosswords[row][col] for row in
        range(len(crosswords))])
    for a in range(0, len(crosswords)):
        column = [crosswords[x][a] for x in range(len(crosswords))]
        finished.append(column)
    for row in finished:
        r=finished.index(row)
        whole_row = ''.join(row)
        found_at = whole_row.find(word)
        if found_at >=0:
            return([found_at, r])
