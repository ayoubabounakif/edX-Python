def count_words_starting_char(string, char):
    count = 0
    string = string.lower().split()
    char = char.lower()
    for str in string:
        if str[0] == char:
            count = count + 1

    return count

