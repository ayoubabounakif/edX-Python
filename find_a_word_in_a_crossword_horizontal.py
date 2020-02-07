###### INSTRUCTOR CODE ######
def find_word_horizontal(crosswords, word):
    if not crosswords or not word: # If empty then return None
        return None
    for index, row in enumerate(crosswords):
        print (index, row)
        temp_str = ''.join(row)
        print (temp_str)
        if temp_str.find(word) >= 0:
            print (crosswords)
            return [index,temp_str.find(word)]
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_horizontal(crosswords,word))
