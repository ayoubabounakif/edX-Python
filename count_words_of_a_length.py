def count_words_len(string):
    count = 0
    string = string.lower().split()
    for str in string:
        if len(str) > 4:
            count = count + 1
    return count

